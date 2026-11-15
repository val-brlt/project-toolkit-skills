---
name: project-planning
description: "Plan approved scope and architecture into incremental SemVer deliveries and agent-ready tickets, then publish the approved plan to GitHub."
disable-model-invocation: true
---

# Project Planning

Run only on explicit request. Act as the planning-phase orchestrator: convert approved functional scope, UX and technical design into a realistic release roadmap and executable vertical tickets. The AI recommends; the human decides. Read [shared conventions](../project-scoping/references/versioning.md) first; load the other references at the steps that use them. Communicate and write user-facing deliverables in French by default; keep machine fields and stable identifiers in English.

**Not this phase:** repeat approved interviews, redesign UX or architecture, implement production code, create detailed implementation plans, execute tickets, close issues, create GitHub Releases/tags, invent delivery evidence, or automatically commit/push. Never assume a version from a legacy document identity.

The planner owns release allocation, traceability, reviewed ticket content and readiness. Delegate tracker reads and GitHub publication to the target project's configured GitHub agent, following its AGENTS.md and issue-tracker reference. Publication authorization is obtained in E; the agent executes the approved batch in F.

## A. Discover and resume

1. Locate the actual target repo, DOCS_ROOT, stable functional scope ID and approved source paths. Read existing scratch state first; distinguish the toolkit repository from an application target. Inspect `git status`, remote, `AGENTS.md`, tracker/label/domain references, actual code/tests/config and existing planning documents. Obtain relevant existing issues/milestones/projects through read-only discovery by the GitHub agent.
2. Resolve the exact target repository, configured readiness label and selected Project or explicit waiver with that agent. Identify whether it can handle the requested milestones and Project operations; issue-tracker conventions alone do not establish those capabilities. Unresolved targets or unavailable operations leave a bounded local draft with publication blockers. Never silently choose a different repository or project.
3. For bug-fix requests, first check the eligibility and inputs in the [bounded PATCH path](references/patch-planning.md). For other work, read the approved functional scope, PROJECT/MVP/backlog, canonical FEAT cards, glossary/ADRs, UX summary/contract and applicable approved mockups (or approved no-UI exception), technical design and architecture contract. Validate the actual source formats with their existing validators. Require approved planning-ready architecture, no blocking questions, compatible scope/IDs and consistent shared delivery records. Legacy contracts remain readable; do not invent missing delivery metadata. If an approved source cannot be validated or conflicts, retain a partial draft and block development readiness.
4. Record source paths/digests, actual approval/delivery evidence, current scope, prior planning approvals, remote identifiers and unresolved blockers in `.scratch/project-planning/<scope-id>/state.md` (reuse an existing workspace). No secrets; never infer approval from silence. Existing approved decisions are reused.

## B. Establish planning inputs and dependencies

For an eligible bug fix, use the PATCH reference's B–C checks in place of the full B–C analysis, then apply D to the affected tickets. All paths continue through E–G.

- Consolidate the approved scope and shared delivery records. Distinguish indispensable MVP, selected approved evolution, supporting changes and future-only work; check actual code and existing tickets. Do not create a competing functional backlog.
- Build the change and dependency graph from existing FEAT/FLOW/SCREEN/ACT/MOD/IFACE/DATA/CHANGE references. Preserve direction, reasons and decision evidence. Distinguish genuine blocking edges from preferred order and potential merge conflicts. Detect cycles; route actual design/product contradictions to their owning phase, not a guessed fix.
- Identify independently verifiable outcomes, existing delivered work, required foundations, crosscutting security/accessibility/testing/operations and risks. Avoid arbitrary horizontal layers or fabricated estimates. Ask only decisions that genuinely require human judgment.

## C. Propose and approve releases

Read [release planning](references/release-planning.md). Propose the minimum viable release partition, dependencies, version bumps, changes, acceptance criteria and MVP milestone. Compare genuinely different options only when consequential. Present a French review and obtain explicit approval of release assignments and the scope they cover. Keep approved-but-unscheduled work visible. Never write approved planned_versions before approval; never change development or delivery state based on planning. First version and stability criteria are human decisions. No new release tags or GitHub Releases.

## D. Delegate ticket design and review

Read `to-tickets` and apply its gather/explore/draft/review steps (1–4) and ticket template to the reviewed scope, planned changes, source contracts, actual code and relevant existing issues. Its publication step is handled by the GitHub agent in F. Include cross-release blockers and required verification; respect its wide-refactor exception. Each ticket has a concise outcome and acceptance checklist, linked to one or more changes and relevant stable source IDs, with one target version. Keep private implementation details for development. Preserve existing issue identity; no mandatory parent and no duplicate TASK prefix in title. Draft one file per ticket under the scratch workspace, with stable planning keys used only to reconcile publication.

Present the ticket breakdown, blocking edges and delivery outcome using `to-tickets`' review process. Ask for explicit approval of the exact detailed tickets. If the partition changes, reopen C only for affected decisions. Detail the nearest active release first, optionally further releases when requested; mark undetailed releases explicitly and do not call them agent-ready. Keep future-only scope excluded.

## E. Validate and approve the package

Read [deliverables and review manifest](references/deliverables.md) and the [GitHub handoff](references/github-projects.md). Prepare the actual French ROADMAP.md and machine-readable PLANNING-CONTRACT.json at discovered canonical paths. Draft exact ticket bodies, the batch for the GitHub agent, contract projections and scoped diffs. Freeze the review package using the manifest procedure. Run from target repo root:

`python .agents/skills/project-planning/scripts/validate_contract.py <path-to-PLANNING-CONTRACT.json> --docs-root <DOCS_ROOT>`

Use `py` on Windows or the installed script path. Run the source validators for affected source contracts. Check the exact package against approved source facts, every selected change and acceptance criterion, confirmed dependencies, real existing issue identities, release assignments, permissions and current state. The validator checks structure and references; human/agent review checks evidence, semantic coverage and remote reality. If unavailable, disclose and do not report a passed audit.

Show the manifest, diffs, release/ticket coverage, checks, risks, blockers, pending release details, target repository/project, and all intended remote actions. Ask for explicit approval of the exact package and a separate explicit authorization of the exact GitHub publication/update batch, both tied to the manifest digest. Record the evidence and digest in the current contract and scratch state; keep the review copies unchanged. Content changes reopen the affected gates under the manifest rules. Approval never authorizes delivery or Git writes.

## F. Delegate the approved GitHub batch

Verify the frozen manifest and compare current files with its review copies under the permitted finalization changes. Give the configured GitHub agent the approved batch and its explicit publication authorization using the [handoff contract](references/github-projects.md#approved-handoff). Accept only the verified results defined there; record partial outcomes and blockers before stopping or retrying. The GitHub agent handles tracker commands and reconciliation without changing the reviewed plan.

## G. Finalize and hand off

Record actual remote references and publication outcome, approved release assignments, and applicable reviewed projections into current UX/architecture contracts; preserve historic sources/digests of the design approval. Rerun affected validators, check projection consistency, remote read-back and the exact final diff against the manifest's permitted finalization changes.

`handoff.blockers` contains unresolved planning blockers: source/design conflicts, missing approvals, or incomplete publication/reconciliation. Mark `development_ready` only when the package is approved, that list is empty, publication is complete for the detailed batch, and the nearest planned release is detailed with at least one agent-ready ticket. Valid dependencies between tickets may remain open; compute the runnable frontier separately using the tracker rules. Later undetailed releases remain out of execution scope. Do not mark tasks implemented or versions delivered.

Present a French handoff: plan, detailed releases, available ticket frontier, blocked/deferred work, URLs, validation and remaining uncertainties. Show scoped git status/diff and unrelated changes. Stage only explicitly approved planning files and reviewed source updates. Request separate commit permission and then separate push permission (remote/branch). Declined permissions preserve the worktree. Development only begins on a new explicit request.

## Re-entry

Match scope, existing stable refs/change IDs, exact versions, ticket keys and verified issue URLs. Preserve closed issues and delivered baselines; default to no changes when inputs unchanged. Re-plan only affected unshipped work, including work in already-published open tickets. Retain their ticket keys and issue identities; show proposed remote updates/removals individually, never silently close or delete. Resume a partially published batch from its frozen manifest and verified remote IDs before creating anything. Maintain one current canonical plan per scope and one global roadmap where appropriate. If the source or approved ticket content materially changes, invalidate only affected readiness and reopen approvals; a new version alone does not invalidate design evidence.
