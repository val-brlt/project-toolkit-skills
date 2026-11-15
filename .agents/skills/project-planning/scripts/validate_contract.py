#!/usr/bin/env python3
"""Read-only planning contract checks; Python stdlib and shared validator only."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / 'references/planning-contract.schema.json'
sys.path.insert(0, str(ROOT.parent / 'project-scoping/scripts'))


def semantic_errors(data, docs_root=None):
    """Called only after schema and shared delivery validation succeeded."""
    errors = []
    delivery = data['delivery']
    def index(values, key, label):
        out = {}
        for value in values:
            ref = value[key]
            if ref in out:
                errors.append(f'{label}: duplicate {ref}')
            out[ref] = value
        return out
    def version(value):
        return tuple(map(int, value.split('.')))
    releases = index(delivery['releases'], 'version', 'releases')
    details = index(data['release_details'], 'version', 'release_details')
    tickets = index(data['tickets'], 'key', 'tickets')
    items = index(delivery['items'], 'ref', 'items')
    changes = {c['id']: (r['version'], c) for r in releases.values() for c in r['changes']}
    if set(details) != set(releases):
        errors.append('release_details must match the release ledger exactly')
    coverage = {cid: set() for cid in changes}
    used_issues = set()
    repo = data['tracker']['repository'].lower()
    for key, ticket in tickets.items():
        target = ticket['version']
        if target not in releases or details.get(target, {}).get('detail') != 'detailed':
            errors.append(f'{key}: ticket needs a detailed release')
        allowed = set()
        for cid in ticket['change_refs']:
            if cid not in changes or changes[cid][0] != target:
                errors.append(f'{key}: invalid or cross-release change {cid}')
                continue
            coverage[cid].add(key)
            allowed.update(changes[cid][1]['item_refs'])
        for ref in ticket['item_refs']:
            item = items.get(ref)
            if ref not in allowed or not item or item['scope'] == 'future' or item['decision_status'] != 'approved':
                errors.append(f'{key}: invalid or unapproved item {ref}')
        for cid in ticket['change_refs']:
            if cid in changes and not set(ticket['item_refs']).intersection(changes[cid][1]['item_refs']):
                errors.append(f'{key}: no item traceability for {cid}')
        for dep in ticket['depends_on']:
            if dep not in tickets or dep == key:
                errors.append(f'{key}: invalid ticket prerequisite {dep}')
            elif version(tickets[dep]['version']) > version(target):
                errors.append(f'{key}: prerequisite in a later release {dep}')
        for url in ticket['external_blockers']:
            if not re.fullmatch(r'https://github\.com/[^/]+/[^/]+/issues/[1-9][0-9]*', url):
                errors.append(f'{key}: invalid external blocker URL {url}')
        issue = ticket['issue']
        if issue:
            expected = f'https://github.com/{repo}/issues/{issue["number"]}'
            if issue['number'] < 1 or issue['url'].lower() != expected:
                errors.append(f'{key}: issue URL/number/repository mismatch')
            if issue['number'] in used_issues:
                errors.append(f'{key}: duplicate GitHub issue number')
            used_issues.add(issue['number'])
    for v, detail in details.items():
        release = releases.get(v)
        if not release:
            continue
        if detail['detail'] == 'historical' and release['status'] not in {'developed','delivered'}:
            errors.append(f'{v}: historical detail requires developed/delivered evidence')
        if detail['detail'] == 'detailed':
            for c in release['changes']:
                cid = c['id']
                if not coverage[cid]:
                    errors.append(f'{cid}: detailed change lacks ticket coverage')
                traced = {ref for k in coverage[cid] for ref in tickets[k]['item_refs']}
                if not set(c['item_refs']) <= traced:
                    errors.append(f'{cid}: detailed change lacks item coverage')
    # Iterative graph check, including long dependency chains.
    graph = {k: set(t['depends_on']) & tickets.keys() for k,t in tickets.items()}
    remaining = {k: len(d) for k,d in graph.items()}
    children = {k: [] for k in graph}
    for k, deps in graph.items():
        for dep in deps:
            children[dep].append(k)
    frontier = [k for k,n in remaining.items() if not n]
    order = []
    while frontier:
        k = frontier.pop()
        order.append(k)
        for child in children[k]:
            remaining[child] -= 1
            if not remaining[child]:
                frontier.append(child)
    if len(order) != len(graph):
        errors.append('Cyclic ticket dependency')
    # Change prerequisites must be respected by ticket edges unless fulfilled
    # historically or inside the same independently verifiable ticket.
    predecessors = {}
    for k in order:
        predecessors[k] = set(graph[k])
        for dep in graph[k]:
            predecessors[k].update(predecessors[dep])
    if len(order) == len(graph):
        for cid, (v, change) in changes.items():
            for dep in change['depends_on']:
                if dep not in changes or not coverage[cid]:
                    continue
                dep_version = changes[dep][0]
                if releases[dep_version]['status'] in {'developed','delivered'}:
                    continue
                if not coverage[dep]:
                    errors.append(f'{cid}: prerequisite {dep} is not detailed')
                    continue
                for k in coverage[cid]:
                    if k in coverage[dep]:
                        continue
                    if not coverage[dep] <= predecessors[k]:
                        errors.append(f'{k}: missing blocking path for change prerequisite {dep}')
    source_paths = set()
    source_roles = set()
    for source in data['sources']:
        path = source['path']
        source_roles.add(source['role'])
        if path in source_paths:
            errors.append(f'duplicate source {path}')
        source_paths.add(path)
        if Path(path).is_absolute() or re.search(r'(^|[\\/])\.\.([\\/]|$)',path) or '\\' in path or re.match(r'^[A-Za-z]:',path):
            errors.append(f'source path escapes DOCS_ROOT: {path}')
            continue
        if docs_root is not None:
            try:
                root = docs_root.resolve()
                actual = (root / path).resolve()
                actual.relative_to(root)
                digest = hashlib.sha256(actual.read_bytes()).hexdigest()
                if digest != source['sha256']:
                    errors.append(f'source digest changed: {path}')
            except (OSError, ValueError) as exc:
                errors.append(f'source unavailable: {path}: {exc}')
    if not {'functional','ux','architecture'} <= source_roles:
        errors.append('functional, UX and architecture source roles required')
    if delivery['scope']['path'] not in {s['path'] for s in data['sources'] if s['role']=='functional'}:
        errors.append('functional source must include delivery.scope.path')
    approval, pub, tracker, handoff = (data[k] for k in ('approval','publication','tracker','handoff'))
    if approval['status'] == 'approved' and not all(approval[k] for k in ('evidence_ref','reviewed_digest')):
        errors.append('approved package requires evidence and reviewed digest')
    if pub['status'] != 'not_requested' and not pub['authorization_ref']:
        errors.append('publication requires separate authorization evidence')
    if tracker['project_mode'] == 'enabled' and not tracker['project_url']:
        errors.append('enabled Project requires actual URL')
    if tracker['project_mode'] == 'waived' and tracker['project_url']:
        errors.append('waived Project must not have URL')
    if pub['status'] == 'complete':
        if approval['status'] != 'approved' or not pub['verified_evidence_ref']:
            errors.append('complete publication requires approved package and verification evidence')
        if tracker['project_mode'] == 'pending':
            errors.append('complete publication requires Project choice')
        if any(not t['issue'] for t in tickets.values()):
            errors.append('complete publication requires every detailed ticket issue reference')
        if any(releases.get(t['version'],{}).get('status') == 'proposed' for t in tickets.values()):
            errors.append('cannot publish proposed release tickets')
    if handoff['development_ready']:
        if approval['status'] != 'approved' or pub['status'] != 'complete' or handoff['blockers']:
            errors.append('development_ready requires approved package, complete publication and zero planning blockers')
        active = sorted((v for v,r in releases.items() if r['status']=='planned'),key=version)
        if not active or details.get(active[0],{}).get('detail') != 'detailed':
            errors.append('development_ready requires nearest planned release detailed')
        elif not any(t['version']==active[0] and t['agent_ready'] for t in tickets.values()):
            errors.append('development_ready requires an agent-ready ticket in nearest planned release')
    return errors


def validate(data, docs_root=None):
    from validate_delivery import delivery_errors, schema_errors
    schema = json.loads(SCHEMA.read_text(encoding='utf-8'))
    errors = schema_errors(data, schema, SCHEMA)
    if errors:
        return errors
    errors = delivery_errors(data['delivery'])
    return errors or semantic_errors(data, docs_root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('contract',type=Path)
    parser.add_argument('--docs-root',type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.contract.read_text(encoding='utf-8'))
        errors = validate(data, args.docs_root)
    except (OSError, ValueError, ImportError, KeyError) as exc:
        print(f'ERROR: {exc}')
        return 1
    for error in errors:
        print('ERROR:',error)
    print(f'Planning checks: {len(errors)} error(s); verify semantic coverage, approvals and remote evidence manually')
    if args.docs_root is None:
        print('NOTICE: source file digests were not checked; pass --docs-root for that check')
    return int(bool(errors))

if __name__ == '__main__':
    sys.exit(main())
