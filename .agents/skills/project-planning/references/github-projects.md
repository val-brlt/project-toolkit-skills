# GitHub publication handoff

The target project's configured GitHub agent executes tracker operations using its AGENTS.md, issue-tracker reference and label conventions. Those are authoritative for commands, authentication and native issue relationships. This reference defines the mapping from the reviewed plan and the result required by the planner.

## Plan mapping

- Publish the reviewed ticket files with their canonical source links and stable traceability IDs. Use the `to-tickets` template already selected in D.
- Include `<!-- project-toolkit:ticket:<scope-id>:<ticket-key> -->` once in each approved ticket body. Preserve existing issue identities through reviewed mappings. Parent relationships require an approved relevant parent.
- Map approved blocking edges to the tracker's native dependencies. A missing capability is a publication blocker; a fallback requires an explicit reviewed decision.
- Map each exact software version to one same-repository milestone without a `v` prefix, reusing existing unambiguous matches. Preserve closed/historical milestones. The MVP milestone remains a functional roadmap goal; milestone assignment does not prove shipment.
- Record the exact Project identity or an explicit waiver. Use issue milestones for target versions and preserve existing Project status fields unless a field change is approved. Require verified capability for each requested Project operation; unsupported views remain disclosed follow-ups as agreed in the batch. Dates require approved scheduling evidence.
- Apply the project's configured readiness label only to fully specified agent tickets. Specification readiness and the runnable frontier are separate: execution also requires an open ticket with no open blockers, no claim/planning conflict and actual prerequisites.

## Approved handoff

Give the GitHub agent the frozen review directory, manifest digest and exact `remote-batch.json` defined in the [review manifest](deliverables.md#review-manifest), plus package approval and separate publication authorization tied to that digest. Include scratch mappings and actual outcomes of any earlier attempt. Reconfirm the target repository and Project choice before execution.

The agent executes only the approved operations, publishing blockers before dependents. Scope, ticket wording, acceptance, release assignments and authorization stay under the planner's review process. A needed change returns to E before further publication. The batch covers planning objects; issue closure, merges, tags, GitHub Releases and delivery claims remain outside this phase.

## Result and retry

Require the agent to persist each actual remote ID immediately against its stable batch operation key and return URLs, verified governed fields, completed/pending operations and any conflicts or failures. Matching identity alone does not establish completion: read-back must match the approved desired state after declared placeholder resolution. Preserve unrelated fields, comments and external issues.

After interruption or timeout, reconcile existing objects from recorded IDs or exact ticket markers across open and closed issues before any creation. Multiple matches or intervening changes to governed fields stop the affected operation for review. Retry only missing operations within the unchanged authorized batch.

**Done:** every detailed ticket and approved dependency, milestone assignment and Project operation has verified read-back, with any Project waiver or agreed view follow-up recorded. A partial result stays partial; the planner uses these results to assess G's readiness criterion.
