# Planning deliverables

Discover and reuse existing canonical paths. Default for initial scope:

```text
<DOCS_ROOT>/planning/ROADMAP.md
<DOCS_ROOT>/planning/PLANNING-CONTRACT.json
.scratch/project-planning/<scope-id>/state.md
.scratch/project-planning/<scope-id>/release-options.md
.scratch/project-planning/<scope-id>/draft-tickets/<key>.md
```

Keep one global ROADMAP and one current contract per functional scope. When an independent change scope needs a separate contract, reuse its existing scope location or propose `planning/<scope-id>/PLANNING-CONTRACT.json` without overwriting the MVP contract. Use the global roadmap to link scope-specific plans and the consolidated version ledger, not competing assignments. If scopes share a release, consolidate compatible changes in the reviewed ledger and ensure every projection agrees on common changes, status and evidence; do not silently merge incompatible scope IDs. Record cross-scope prerequisites through actual known issue references and source context. Promote to a wider contract format only through explicit review; no fake FEAT IDs.

ROADMAP.md (French): scope/source links; known release baseline; goals and approved/proposed version ledger with change IDs and dependencies; MVP milestone/criteria independent of stability; release detail status; coverage, unscheduled approved work, risks; links to published issues and project. No copied feature catalogues or operational status replicas. Summarize progress only as of verified evidence and let GitHub manage live issue status.

Contract schema v1.0: `delivery` is the unchanged shared schema. `sources` names canonical scoped functional/UX/architecture documents, relative to DOCS_ROOT (and optional additional approved sources). Each SHA-256 matches the current source file; the validator checks files/hashes when --docs-root is passed. The review manifest below preserves the original reviewed sources and exact approved projections. `release_details` is a per-version ticket-detail index. `tickets` indexes stable internal keys, outcome, acceptance, change/ref mappings, dependencies, optional external blockers (actual issue URLs), agent eligibility and actual remote number. GitHub issue is canonical after publication; draft content is reviewed in scratch. `tracker` records exact repo and project choice; `publication` records authorization ref and state; `approval` records package decision evidence and manifest digest; `handoff` records readiness and blockers as defined in G. Store no fabricated evidence or credentials. Source paths must not escape DOCS_ROOT.

Do not add extensions to the shared delivery object. In current UX/architecture contracts, project only release changes and item assignments that belong to that phase's actual known refs, preserving common change identity, relevant shared metadata and documented differences in phase-specific item_refs. If a prerequisite or shared record cannot be represented by existing schema without inventing refs, report and resolve with reviewed schema/contract change before claiming readiness. Do not mutate delivered snapshots or invalidate approved design contents just to align planning. Retain attributable prior approval evidence; validate projections with the existing validators. Compare each common change's version, status/approval, common refs and prerequisites; reconcile discrepancies explicitly. Never rewrite another phase's approval.

The contract is a structured handoff, not the live issue tracker. It cannot prove human authority or actual remote state from JSON alone. Validate the actual approved source files, content digests, ticket semantic coverage, remote state and source projection compatibility manually/in the orchestrator. A successful validator run is not approval, publication, development or shipment.

## Review manifest

### Freeze in E

Create a review directory at `.scratch/project-planning/<scope-id>/reviews/<batch-key>/`. Save exact-byte review copies of the source documents read, proposed ROADMAP and planning contract, ticket bodies, every proposed source projection, and a `remote-batch.json` describing all intended GitHub operations. Each batch operation has a stable key, exact target or creation specification, expected prior state, desired changes and references to ticket/operation keys for IDs not yet allocated. Declare any URL/ID placeholders and their exact insertion locations in ROADMAP links, ticket links or remote operations here before review; keep source projections literal.

In the planning-contract review copy only, set `approval` to `draft` with null `evidence_ref` and `reviewed_digest`, `publication` to `not_requested` with null evidence references, and `handoff.development_ready` to false. Preserve known issue identities and actual blockers. Keep prior approvals/publication evidence in the existing state history. This copy describes the new batch; retries reuse it unchanged.

Write `review-manifest.json` with `schema_version: "1.0"` and a `files` array. Each entry has `role` (`source`, `output`, `ticket`, `projection`, or `batch`), `target` (repo-relative path), `snapshot` (review-directory-relative copy path), and lowercase `sha256` of that copy's exact bytes. Entries are unique and sorted by `(role, target)`; include the before-source and proposed projection separately when they share a target. Save the manifest as UTF-8 without BOM, with LF endings. Keep the manifest and copies immutable after review; a revised package gets a new batch key.

`approval.reviewed_digest` is the lowercase SHA-256 of the saved manifest's exact bytes. The manifest contains neither itself nor its own digest. Compute it with:

```text
python -c "import hashlib,pathlib,sys; print(hashlib.sha256(pathlib.Path(sys.argv[1]).read_bytes()).hexdigest())" <path-to-review-manifest.json>
```

Record this digest and the review directory in scratch state. Tie package approval and separate publication authorization to it; write their evidence and the digest to the current contract only. Hashes cover frozen copies, so recording approval introduces no self-reference.

### Permitted finalization changes

Compare current outputs with the frozen copies before F, on retry and after G. The only permitted differences are:

- Planning-contract `approval`: draft to approved, with actual approval evidence and this manifest digest.
- `publication`: not_requested to partial to complete (or directly complete), with actual authorization/read-back evidence; `handoff` blockers updated with evidenced resolution/failure, and readiness set only under G.
- `tickets[].issue`: null filled with the verified issue identity for that ticket key. Existing issue identities remain unchanged.
- `tracker.project_mode`/`project_url`: pending to enabled with a verified URL only for an explicitly approved Project creation. An existing Project or waiver remains unchanged.
- `sources[].sha256`: align with the current canonical bytes, either the original reviewed source or its exact approved projection. Reconcile these two known states after an interrupted G before validation; any other source content blocks continuation. Preserve both copies.
- URL/ID placeholders at the locations declared in the batch: resolve only from verified operation results. These substitutions may fill document links or native dependency targets; ticket wording, acceptance, scope and version remain unchanged.

All other outputs must match their review copies; source updates must match their exact approved projections. Changes outside this list require a new reviewed package and affected approvals before further publication. Preserve both review histories and any actual partial remote results. The contract validator does not verify this manifest procedure; the orchestrator checks hashes, diffs and evidence.
