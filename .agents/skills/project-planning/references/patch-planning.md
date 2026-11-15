# Bounded PATCH path

Use this path for a correction to already-approved behavior. It replaces the full B–C analysis and limits D to affected tickets; A's repository/state checks and E–G remain required. Reuse unchanged decisions and evidence without new interviews or approvals.

## A. Eligibility and inputs

Read the bug report and comments, reproducible actual/expected behavior, relevant approved feature criteria, current planning contract/roadmap and matching UX/architecture contracts. Verify scope IDs, source digests, applicable source validators, prior approvals and planning-ready architecture. Inspect the affected code/tests and verified release baseline. Reuse existing canonical references and issue identities.

Proceed on this path only when the correction restores approved behavior, adds no functional scope or incompatible public-contract change, and leaves approved UX/technical decisions valid. Missing or contradictory source evidence leaves a local draft with an explicit planning blocker. New requirements or design decisions return to their owning phase; unresolved eligibility or first-release numbering uses the full B–C path after those blockers are resolved.

## B. Bounded impact check

Record in scratch:

- The failing scenario, approved expected outcome and observable acceptance criteria for the correction.
- Affected FEAT/FLOW/SCREEN/ACT/MOD/IFACE/DATA/CHANGE IDs and relevant dependency edges, following direct and transitive effects until the boundary is justified.
- Relevant code/test/config evidence, regressions to verify, and security, accessibility, data or operational effects where applicable.
- Existing delivered work, open tickets and prerequisites to preserve or update.

**Done:** every discovered affected reference is linked to correction work or has an evidenced no-change rationale; each prerequisite is identified, and no unresolved product/design choice remains. Evidence of a wider change routes back to the owning decision and full planning analysis.

## C. Target and approval

Use the shared SemVer policy to propose a compatible PATCH after the verified baseline, or include the correction in an existing approved unreleased version when appropriate. Review any changed version assignment explicitly. Preserve unrelated release partitions, MVP/stability decisions and delivered records; compare alternatives only when the target has a consequential trade-off.

**Done:** the correction's scope, acceptance, prerequisites and exact target version are explicitly approved. Reuse unaffected prior approvals.

## D–G. Tickets, validation and publication

Apply D's `to-tickets` method and user review to the correction's tickets only; reuse an existing issue through reviewed mapping rather than duplicating it. Each affected change and acceptance criterion must be covered. Reference inherited tickets without redrafting them.

Continue through E–G with the same manifest, validation, approval, authorization, reconciliation and readiness gates. Coverage and partition review concern the correction and its impacts; retain the consolidated ledger and check inherited source/dependency consistency without replanning unrelated work. A local draft ends with blockers recorded and `development_ready: false`; a published handoff meets G's completion criterion.
