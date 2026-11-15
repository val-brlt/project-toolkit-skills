"""Planning regression checks. Run from repository root with Python 3.9+."""
import copy
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

SKILL = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('planning_checks', SKILL / 'scripts/validate_contract.py')
V = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(V)
SHARED = SKILL.parent / 'project-scoping/scripts/validate_delivery.py'


def fixture():
    def item(ref):
        return dict(ref=ref, scope='mvp', decision_status='approved', acceptance_criteria=['Critère vérifiable'], planned_versions=['0.1.0'], development_status='not_started', delivery_status='not_delivered', delivered_versions=[], evidence_refs=[])
    def change(n, deps):
        return dict(id=f'CHANGE-{n}',kind='feature',compatibility='compatible',item_refs=[f'FEAT-{n}'],summary='Comportement',acceptance_criteria=['Critère vérifiable'],depends_on=deps)
    def ticket(n,deps):
        return dict(key=f'TICKET-{n}',title=f'Comportement {n}',version='0.1.0',change_refs=[f'CHANGE-{n}'],item_refs=[f'FEAT-{n}'],outcome='Résultat observable',acceptance_criteria=['Critère vérifiable'],depends_on=deps,external_blockers=[],agent_ready=True,issue={'number':int(n),'url':f'https://github.com/example/project/issues/{int(n)}'})
    paths=[('functional','MVP.md'),('ux','ux/UX-CONTRACT.json'),('architecture','architecture/ARCHITECTURE-CONTRACT.json')]
    return dict(schema_version='1.0', sources=[dict(role=role,path=path,sha256=hashlib.sha256(b'approved').hexdigest()) for role,path in paths], delivery=dict(scope=dict(id='mvp',kind='mvp',path='MVP.md',feature_refs=['FEAT-001','FEAT-002']),items=[item('FEAT-001'),item('FEAT-002')],releases=[dict(version='0.1.0',baseline_version=None,status='planned',approval_ref='approval:release',evidence_refs=[],changes=[change('001',[]),change('002',['CHANGE-001'])])],dependencies=[dict(from_ref='FEAT-002',to_ref='FEAT-001',kind='functional',reason='Prérequis',status='confirmed')],milestones=[dict(id='mvp',kind='mvp',criteria=['Critères MVP'],status='open',evidence_refs=[])],public_contracts=[],stability_criteria=[],stability_approval_ref=None),release_details=[dict(version='0.1.0',detail='detailed')],tickets=[ticket('001',[]),ticket('002',['TICKET-001'])],tracker=dict(repository='example/project',project_mode='enabled',project_url='https://github.com/users/example/projects/1',ready_label='ready-for-agent'),approval=dict(status='approved',evidence_ref='approval:package',reviewed_digest='a'*64),publication=dict(status='complete',authorization_ref='approval:publish',verified_evidence_ref='verification:remote'),handoff=dict(development_ready=True,blockers=[]))


class PlanningChecks(unittest.TestCase):
    def setUp(self):
        self.data=fixture()
    def check(self, text):
        self.assertTrue(any(text in msg for msg in V.semantic_errors(self.data)), V.semantic_errors(self.data))
    def test_valid(self):
        self.assertEqual(V.semantic_errors(self.data),[])
    def test_cycle(self):
        self.data['tickets'][0]['depends_on']=['TICKET-002']; self.check('Cyclic ticket')
    def test_missing_dependency(self):
        self.data['tickets'][1]['depends_on']=[]; self.check('missing blocking path')
    def test_unknown_dependency(self):
        self.data['tickets'][1]['depends_on']=['TICKET-999']; self.check('invalid ticket prerequisite')
    def test_coverage(self):
        self.data['tickets'].pop(); self.check('lacks ticket coverage')
    def test_unapproved_item(self):
        self.data['delivery']['items'][0]['decision_status']='proposed'; self.check('invalid or unapproved item')
    def test_duplicate_issue(self):
        self.data['tickets'][1]['issue']=copy.deepcopy(self.data['tickets'][0]['issue']); self.check('duplicate GitHub issue')
    def test_wrong_repo(self):
        self.data['tickets'][0]['issue']['url']='https://github.com/another/repo/issues/1'; self.check('repository mismatch')
    def test_partial_publication(self):
        self.data['publication']['status']='partial'; self.check('development_ready requires')
    def test_missing_issue(self):
        self.data['tickets'][0]['issue']=None; self.check('requires every detailed ticket')
    def test_no_permission(self):
        self.data['publication']['authorization_ref']=None; self.check('separate authorization')
    def test_project_pending(self):
        self.data['tracker']['project_mode']='pending'; self.check('requires Project choice')
    def test_deferred_release(self):
        self.data['release_details'][0]['detail']='deferred'; self.check('nearest planned release detailed')
    def test_source_digests(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for source in self.data['sources']:
                path=root/source['path']; path.parent.mkdir(parents=True,exist_ok=True); path.write_bytes(b'approved')
            self.assertEqual(V.semantic_errors(self.data,root),[])
            (root/'MVP.md').write_bytes(b'changed')
            self.assertIn('source digest changed: MVP.md',V.semantic_errors(self.data,root))
    def test_path_traversal(self):
        self.data['sources'][0]['path']='../MVP.md'; self.check('source path escapes')
    def test_no_side_effect(self):
        original=copy.deepcopy(self.data)
        V.semantic_errors(self.data)
        self.assertEqual(original,self.data)
    def test_cross_release(self):
        self.data['tickets'][0]['version']='0.2.0'; self.check('prerequisite in a later release')
    def test_proposed_cannot_publish(self):
        self.data['delivery']['releases'][0]['status']='proposed'; self.check('cannot publish proposed')
    def test_draft_unpublished(self):
        self.data['approval'].update(status='draft',evidence_ref=None,reviewed_digest=None)
        self.data['publication'].update(status='not_requested',authorization_ref=None,verified_evidence_ref=None)
        for t in self.data['tickets']:t['issue']=None
        self.data['handoff']['development_ready']=False
        self.assertEqual(V.semantic_errors(self.data),[])


@unittest.skipUnless(SHARED.is_file(),'Shared existing repository validator not available in isolated bundle')
class SharedIntegration(unittest.TestCase):
    def test_shared_valid(self):
        self.assertEqual(V.validate(fixture()),[])
    def test_schema_error(self):
        d=fixture();d['tickets'][0]['version']='v1';self.assertTrue(V.validate(d))
    def test_delivery_truth(self):
        d=fixture();d['delivery']['items'][0]['delivery_status']='delivered';self.assertTrue(V.validate(d))
    def test_bad_semver(self):
        d=fixture();d['delivery']['releases'][0]['version']='0.0.1';d['delivery']['releases'][0]['baseline_version']='0.0.0';self.assertTrue(V.validate(d))
    def test_legacy_not_implicitly_versioned(self):
        d=fixture();d['delivery']['releases'][0]['version']='v1';self.assertTrue(V.validate(d))

if __name__=='__main__':
    unittest.main(verbosity=2)
