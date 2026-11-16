---
name: project-ux
description: "Design and validate the global MVP UX and progressive deliveries through HTML mockups, a distinctive visual system, anti-AI-slop review, a UX contract and separate human approvals."
disable-model-invocation: true
---

# MVP UX/UI and progressive delivery

This is a **user-started workflow**, not a production implementation agent. Run after the MVP or requested functional change is approved with `project-scoping`. Preserve a coherent UX for the **whole MVP**, with progressive delivery subsets when already approved. Talk **in French** and follow `AGENTS.md`. Read `references/document-formats.md`, `references/visual-quality.md` and [shared versioning conventions](../project-scoping/references/versioning.md) before writing; the shared reference owns path, backlog, progress and re-entry rules.

**UX artifact policy:** For scopes with UI, the user reviews **interactive HTML mockups**. Produce these complementary outputs:

1. Validated, browser-viewable HTML/CSS/JavaScript mockups when the scope has UI: the visual reference.
2. A short French `UX-SUMMARY.md`: human-readable design rationale, main journeys/navigation, roadmap awareness, and links.
3. `UX-CONTRACT.json`: the **machine-readable UX handoff** for architecture, issue planning and implementation, with feature/flow/screen/interaction/preview links.
4. A lightweight, shared visual system: `DESIGN-GUIDELINES.md` and `DESIGN-TOKENS.json` for an approved web UI, maintained only when needed. The visual-quality reference defines their complementary roles, canonical paths and compatibility. Do not create them for an entirely no-UI project.

Add a separate pattern explanation only when a complex decision requires context beyond the HTML, contract and summary; link it from the summary. For earlier UX documents, apply the Existing documentation section of [document formats](references/document-formats.md). The visual-quality reference supplements its artifact list without changing the UX contract schema.

## Skills and tool compatibility

- Use `grilling` for **targeted** unanswered UX questions, not a repeat of the functional scoping interview. Use `domain-modeling` only when needed for terminology.
- Use the installed `frontend-design` guidance for direction and HTML mockups, `design-system-management` to establish or extend the shared visual system, and `design-critique` to review rendered screens before user review and after substantial visual changes.
- Use `impeccable` for product-specific design quality and anti-AI-slop review (`critique`, `audit` and the detector as applicable). Apply targeted refinements such as `distill` or `polish` when supported by findings. Follow the installed skill's current instructions; see `references/visual-quality.md` for sequencing, context and boundaries. Assume external skills are installed; do not introduce dependency-installation checks or install them within this workflow.
- Matt Pocock's `prototype` can inform narrowly scoped exploratory variants if needed. Its optional branch/commit procedure does **not** grant Git permission in this workflow. Do not run speculative prototype branches/commits automatically.
- Codex may not offer a callable `Skill` tool. Read the installed skills' `SKILL.md` files and apply the guidance directly instead of failing or claiming to have called an unavailable tool. If an external skill requires user-only invocation, use its documented guidance directly within this workflow when supported; otherwise explain the limitation and ask for the specific manual action, without falsely reporting a completed audit.
- The orchestrator owns scope, scratch isolation, canonical outputs and approval gates. External skills do not authorize production edits, network installations, hooks, publication or Git actions. Do not let their suggestions silently change approved functionality or visual identity.

## Inputs and boundaries

Determine `DOCS_ROOT` by locating the project's **existing authoritative** approved documentation, e.g. `docs/docs-project/` or `docs/docs-projet/`; never create both. Read:
- `PROJECT.md`, `MVP.md` and the canonical backlog for global product context; distinguish existing approved features outside this change from future-only needs.
- The authoritative approved scope (`MVP.md`, an existing `versions/<baseline>/VERSION.md`, or an approved change scope) and linked canonical feature cards. Read release plans only if already approved; no release number is required for global design.
- UX outputs and mockups from earlier versions, when present, and any approved design system, brand assets, constraints and target devices.

Use backlog entries as navigation context according to their actual status. Distinguish reused, changed and new screens. UX `covered` means designed; record FEAT/FLOW/SCREEN/ACT progress and incremental slices using the shared model.

In scope: journeys, navigation, screen responsibilities, content and visual hierarchy, interaction patterns, error/empty/loading/success states, accessibility, responsive expectations and mockups. Out of scope: backend/API/schema/framework selection, production code, development tickets and GitHub publication. The UX contract specifies **observable behavior**, not implementation design.

### Functional refinements discovered during UX

UX review often reveals a legitimate feature change. **Do not treat the earlier scope as frozen against a new, explicit user decision.** When the user requests a new or changed behavior:

1. Identify affected FEAT, module, canonical MVP/change scope and living indexes. Explain the functional change and scope; clarify only unresolved ambiguity. **Obtain explicit functional approval before recording a change as approved.** Visual approval alone does not approve novel functional behavior.
2. For an **approved refinement to undelivered behavior**, update the affected canonical requirements/acceptance, module, MVP/change scope and relevant indexes **in place**. Keep existing historical headings and stable FEAT IDs; do not invent version sections or release assignments. Only create a FEAT for a separate concept.
3. Integrate the approved behavior into the ordinary canonical sections. Fold any redundant appendix for this same refinement into those sections and remove its duplicate paragraph/link; removing an underlying source file or affecting other references requires reviewed cleanup approval. Explain provenance in the conversation and scoped diff. Preserve the original approved `SCOPING-SUMMARY.md` unless a correction is explicitly approved.
4. Apply shared preservation rules to delivered behavior and slices. Escalate broad unresolved functional scope to `project-scoping`.
5. Update the UX gallery, `UX-CONTRACT.json` and `UX-SUMMARY.md` to match the now-approved functional scope. Reconfirm affected visuals when their design changes. Do not mark a proposal approved until its functional decision and visual review (if applicable) are explicit.

These edits are **regular canonical documentation changes**. The final documents should describe the **current accepted behavior**, not the process by which it was discovered. Do not leave contradictory old text elsewhere in the feature or module.

## Workflow

### 0. Load context and resume

Identify the approved functional scope, existing document baseline and any verified release context. Read MVP, roadmap, prior UX, existing visual system and scratch state. Reuse `.scratch/project-ux/<project-slug>/<scope-id>/` (including existing version-named workspaces). Show MVP-wide journeys and currently approved delivery subsets separately. Never repeat approved discovery or create future-phase dummy routes. Reuse approvals only for the exact scope, visual direction and gallery revision previously approved; a request to edit does not approve the result.

### 1. Resolve UX questions and structure the experience

Ask only questions needed for journeys, information architecture, interaction or visual decisions. Use `grilling` when helpful. Handle any user-requested **functional** changes through the canonical-update process above, before locking the corresponding UX choices. Establish a small set of main journeys/screens, a navigation structure that can accommodate documented later phases and low-fidelity wireframes for new or materially changed layouts before high-fidelity design. Derive the structure from user tasks, not a generic dashboard template. Keep sketches and intermediate notes in scratch; do not request a mandatory wireframe-by-wireframe review.

**No-UI path:** if every scoped feature genuinely has no UI, obtain explicit approval of each `no_ui` justification, skip steps 2–3 (including direction, tokens, visual review) and the visual promotion in step 4, then write the summary and contract. Use empty `flows`/`screens`, one `no_ui` coverage record per FEAT with empty screen/flow references, and FEAT-only delivery items. Under the summary's `Maquettes validées` heading explain that no mockup is applicable and link the approved functional source. Create no gallery or placeholder screen. **Done:** all no-UI justifications are approved, the audit passes and both documents can be marked approved. A scope with unchanged existing UI instead reuses its approved HTML and existing visual system; mixed scopes still review their UI normally.

### 2. Choose a direction, build and critique interactive mockups

Follow [visual quality and anti-AI-slop guidance](references/visual-quality.md).

- **New project / explicit redesign:** explore 2–3 genuinely different, product-appropriate artistic directions with comparable visual samples and short rationales (e.g. an offline HTML direction board in scratch). Ask the user to approve a direction or specify changes; stop before building the full high-fidelity gallery. Skip this gate only when a sufficiently specific direction has already been explicitly approved for the scope. Do not force a moodboard or a refonte on an established project.
- **Existing project:** reuse the approved visual system, adapt only the impacted patterns, and ask for approval before any intentional global design-system change that affects already approved surfaces.
- Establish or extend the lightweight visual system in scratch with `design-system-management`. Use semantic tokens and the actual CSS; plan responsive behavior for target devices and accessibility from the beginning.

Build a **real, offline-capable HTML/CSS/JavaScript gallery** under the same scratch scope's `preview/`. Use stable `id="SCREEN-001"` containers and `href="#SCREEN-001"` navigation, meaningful in-memory clicks/forms/states and French copy. Apply `frontend-design` and the relevant Impeccable new-work guidance before editing. Images and inspiration boards may support design exploration but cannot replace the functional HTML gallery.

- **First design:** create the approved scope's screens and journeys.
- **Modification:** inventory the existing gallery, local assets and approved contracts that reference it. Start the preview from a copy of that gallery and its assets; change only approved new/modified behavior. Retain unchanged screen containers, anchors, navigation and assets wherever the same canonical files will be replaced. Reused screens hosted in other approved galleries keep their existing links. Retained context adds no new feature coverage or approval claim.
- **Historical baseline:** when an existing gallery must remain immutable, prepare a distinct scope-specific UX location in the reviewed manifest, with its contract and new gallery together; retain links to the original gallery for reused screens.

Review actual rendered pages and important states using `design-critique` and Impeccable `critique`/`audit`; attempt deterministic detector scans against the preview and a local rendered URL where appropriate. Correct material findings, retest affected journeys, and keep a concise review record in scratch. Report any unavailable check or degraded review explicitly. No critical accessibility, interaction or design-quality blocker may be silently waived. Do not mistake a clean scan for human approval or real user testing.

**Done:** the complete resulting gallery works offline, all retained references resolve, the visual review covers affected journeys, and the approved design system is reflected in the preview. Screen removals or asset changes affecting an approved reference require an explicit reviewed decision.

### 3. Show the real HTML and explicitly request visual approval — STOP

Present the working gallery path/URL and revision, covered journeys, how to navigate/test representative interactions, and how navigation accommodates known future phases **without implementing them**. Review by **journey group** when there are many screens, not file by file. Mention material audit limitations or remaining non-blocking issues. Revisit functional documentation only when a separately approved functional scope change is needed.

For every new or materially revised gallery, **end the current turn with an explicit French request**, for example:

```markdown
> Les maquettes HTML sont prêtes à être consultées : [ouvrir les maquettes](<actual path or URL>). Teste les parcours et les interactions. **Valide les maquettes en écrivant « Je valide les maquettes », ou écris les modifications que tu souhaites.** Je ne finaliserai les livrables UX qu'après ta validation.
```

Use the actual accessible path or URL, never the placeholder. Ask the user to approve the whole displayed revision (or explicitly named journey groups, with all in-scope groups covered before completion). Preserve pending review state in scratch: preview revision, design-system revision, applicable scope, approved groups and outstanding comments. Silence, a vague acknowledgment, a modification request, or approval of an older revision does not validate the current revision. Accept any unambiguous explicit approval; the example phrase is not a required password.

**Stop and wait at this gate.** Do not promote the gallery, mark contracts/summaries approved, finalize canonical design files, commit, push or proceed to the next phase before approval. If the user requests changes, apply them in scratch, handle any functional change through the separate approval procedure, rerun the affected reviews, present the updated gallery and explicitly ask again for validation or modifications. Preserve untouched approved groups only if their actual visuals and interactions have not changed. A previously explicitly approved unchanged gallery can be reused without asking for redundant approval; show which approval is reused. No mandatory per-screen Markdown review.

### 4. Promote approved visuals and write the handoff

For scopes with new/changed UI, promote the **exact approved complete gallery** and assets only to the reviewed destination. For a new global MVP use `<DOCS_ROOT>/ux/mockups/`; otherwise follow the existing or reviewed scope-specific location from step 2. Before replacement compare the preview with the baseline inventory: every retained screen, anchor, navigation link and local asset must still resolve. Final docs link to canonical HTML. Keep the original gallery when preserving a historical baseline.

Use the artifact policy above, [document formats](references/document-formats.md) and the visual-quality reference to create or update applicable files at their canonical locations:

```text
<DOCS_ROOT>/
└── ux/                              # or existing versions/<baseline>/ux/, reused in place
    ├── DESIGN-GUIDELINES.md          # shared approved visual/interaction conventions
    ├── DESIGN-TOKENS.json            # shared machine-readable visual values
    ├── UX-SUMMARY.md                 # concise French human-facing synthesis
    ├── UX-CONTRACT.json              # full structured planning handoff
    └── mockups/
        ├── index.html                # approved gallery, if this scope changes UI
        └── ...                       # local CSS, JS, assets
```

The tree illustrates a new MVP; do not duplicate shared design files per scope. Preserve or explicitly review historical design-system changes under the shared conventions. Promote design files that match the approved gallery; link to them from the UX summary. A previously approved shared system is reused for unchanged UI. Do not add fields to the UX contract that its current schema does not allow.

Put approved observable behavior and FEAT/FLOW/SCREEN/ACT traceability in the JSON contract. Use `references/document-formats.md` for coverage records, delivery fields, schema and compatibility.

Do not generate an issue per screen or invent technical solutions. Later architecture and planning combine the functional scope, this JSON contract, the approved HTML, the shared visual system and architecture decisions; the planning skill proposes vertical, testable work items and requests user approval before GitHub Issues publication.

### 5. Validate, report and hand off

Run:

`python .agents/skills/project-ux/scripts/validate_ux_docs.py <DOCS_ROOT> --contract <path-to-UX-CONTRACT.json>`

Legacy `--version <baseline>` and discovery remain supported. Paths passed to `--contract` are relative to the current working directory. When promoting over a shared gallery, also validate every contract identified in the baseline inventory, including contracts outside the current change.

Use `py` on Windows when needed. The script checks JSON shape/references/coverage, feature IDs, local HTML anchors/assets and forbidden scratch paths; it **cannot** decide design quality or confirm user approval and does not validate the new design-token artifact. Separately verify the design-token JSON parses, linked design files exist, and the tokens and guidelines agree with the approved CSS and visual review. Reopen the canonical gallery offline and check anchors, key interactions and target viewport sizes. Correct discrepancies. If the JSON contradicts the approved HTML, correct the JSON; if the actual design needs changing, return to step 3 for renewed explicit visual approval. Ensure any approved functional changes are integrated directly into canonical functional documents and reflected in the JSON. After passing audit and explicit approval of the applicable visuals or no-UI justifications, set UX summary and contract status to `approved` and rerun validation.

Give the user a short French report: approved preview or no-UI justifications, covered journeys/features, relevant future navigation implications, visual-system links, functional documents updated in place (if any), tests actually performed and genuinely unresolved points. Make the full contract available for optional inspection. Show the complete relevant Git diff, including any canonical functional edits, for transparency.

### 6. Git actions: separate explicit approvals

Show `git status`, the relevant diff and unrelated changes. Stage **only** the documents, approved HTML, approved design-system files and functional edits within scope; never `git add -A`. Ask explicit permission to **commit**, then request **independent push permission** with remote and branch confirmation. Declining either action leaves local files intact. No automatic branch creation, commit, push, architecture stage or GitHub Issue publication.
