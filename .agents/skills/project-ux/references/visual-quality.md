# Visual quality, design system and anti-AI-slop review

Apply this reference to new/changed UI. It supplements `document-formats.md`; its existing UX contract schema, delivery model and validators remain unchanged. Follow shared versioning and the orchestrator's approval gates. Instructions are in English; user-facing boards, gallery UI, rationale and human-readable token descriptions are in French.

## 1. Product-specific design before decoration

Read approved product context, audience, workflows, target platforms, density/usage constraints, existing UI and future navigation implications. Choose hierarchy by task importance and usage frequency. Make low-fidelity layouts in scratch before adding visual style. Use existing approved brand guidance if available.

For a new visual identity or explicitly approved redesign, show two or three distinct, comparable directions on the same representative surface, with palette, type, density, information hierarchy, component shapes and a short rationale. Use `frontend-design` and relevant Impeccable shaping guidance. A moodboard may be an HTML board with local examples, references and swatches; do not require image generation or internet access. If references are used, note their source, use them as inspiration rather than copying, and never depend on remote resources in final mockups. Explain trade-offs and request explicit selection or requested adjustments before high-fidelity work. If the user already approved an identity, reuse it without a redundant gate.

## 2. Lightweight shared visual system

Use `design-system-management` to capture actual approved conventions rather than generating a generic component catalogue. Preserve the existing canonical location. For a new MVP use `<DOCS_ROOT>/ux/DESIGN-GUIDELINES.md` and `<DOCS_ROOT>/ux/DESIGN-TOKENS.json`. If the project has an authoritative equivalent, reuse it and link it instead of creating competing systems; follow reviewed migration and history rules. For scope-specific designs, reference the shared system from `UX-SUMMARY.md` using relative links. Keep drafts and experiments under scratch; promote only the values approved through the direction and gallery review. Do not overwrite a historical design baseline or silently restyle unchanged approved screens.

`DESIGN-GUIDELINES.md` is a concise French reference: product intent, chosen visual direction and rationale, hierarchy and density, navigation patterns, reusable components and their variants/states, responsive behavior, accessibility and motion conventions, and justified exceptions. Link to the tokens and approved gallery. Do not repeat the full UX contract.

`DESIGN-TOKENS.json` is the machine-readable source for approved visual values (not behavior). Use a small, consistent object of semantic tokens; reuse any existing approved token format, otherwise use the following **illustrative** shape (values are examples, not defaults or a palette recommendation):

```json
{
  "schemaVersion": 1,
  "tokens": {
    "color": {"background": "#FFFFFF", "text": "#17232A", "actionPrimary": "#145A64", "onActionPrimary": "#FFFFFF"},
    "typography": {"familyBody": "system-ui, sans-serif", "sizeBody": "1rem", "lineHeightBody": 1.5},
    "spacing": {"small": "0.5rem", "medium": "1rem"},
    "radius": {"control": "0.25rem"},
    "border": {"width": "1px"},
    "shadow": {"overlay": "none"},
    "motion": {"durationFast": "120ms"}
  }
}
```

Record actual semantic colors (including feedback and focus where used), typography/weights, spacing, radii, borders, elevation and motion as applicable. Add layout/breakpoint values when approved. Use explicit units and real values, not placeholders. CSS custom properties should implement these tokens consistently; include local font assets only if available and permitted, with reliable fallbacks. Avoid gratuitous token proliferation and production framework choices. Parse JSON and compare with the gallery's actual CSS/appearance before finalizing. The current UX validator is independent of this supplemental check. Link the visual reference from the summary; do not add unsupported fields to `UX-CONTRACT.json`.

## 3. Impeccable integration without duplicate documentation

Use the locally installed `impeccable` guidance and relevant references for shaping/new work, critique, audit and targeted correction. Follow actual installed command syntax. Impeccable reads product/design context (`PRODUCT.md`, `DESIGN.md` and possible companion files); `PROJECT.md`, approved functional scope and the existing visual system remain the project's canonical inputs. Reuse an existing Impeccable context if present, checking it against approved facts. If the installed tool needs native context for this mockup, prepare derived context in the isolated scratch project, following its supported context resolution; do not assume a custom `DESIGN-TOKENS.json` is understood by its detector. Never invent audience, brand or implementation facts, overwrite production context or generate competing permanent root documents automatically. If native context cannot be loaded for the target, provide the approved context directly to the qualitative review, attempt supported detector scans, and disclose which context-dependent checks were unavailable.

Use the external skills as complementary guidance: `frontend-design` for distinctive visual craft, `design-system-management` for consistency, `design-critique` for usability, Impeccable for visual specificity and evidence-based audit. Do not automatically install a plugin, enable hooks, call unrelated external services or change production code. Keep audit snapshots, derived context and temporary assets in scratch, not in the final gallery. If an installed skill requires a separate manual action, tell the user rather than pretending it was invoked. No fabricated reports or scores.

## 4. Review the actual HTML, not just its source

Open the gallery in a browser; use available browser tools or a locally served preview if needed. Review representative screens and states at the device sizes supported by the product (e.g. 1440, 768, 390 CSS px for a general responsive web product, plus intermediate widths). Do not invent a mobile product requirement for a desktop-only scope: record agreed limitations. Check the flow with realistic French copy and representative content including long text and empty, loading, error, success and disabled states where applicable. Test main actions, keyboard navigation, focus order/visibility, semantic headings and controls, labels, feedback, overflow/reflow and reduced motion. Aim for WCAG AA on applicable web interfaces: ordinary text 4.5:1 contrast, large text 3:1, non-text UI contrast where required; aim for comfortable touch targets (44 CSS px when appropriate), and distinguish design targets from formal conformance claims. Check actual colors and rendered geometry, not estimated scores. Real user testing is separate; never claim it was performed unless it was.

Use `design-critique` and Impeccable `critique` and `audit` as applicable to the rendered gallery. Attempt a deterministic scan against the actual scratch preview (e.g. `npx impeccable detect <preview-path>` using the installed CLI or supported local equivalent; a locally served URL can also be scanned if browser review is available). Do not silently trigger an installation or network download. Follow the installed skill's review orchestration where supported, including any required independent review and degraded-mode reporting. A source scan complements but does not substitute for inspecting rendered design. If browser or detector checks cannot run, record the exact limitation and the verification actually performed; do not claim that missing checks passed. Do not treat automated findings as approval or proof of accessibility.

## 5. Anti-AI-slop quality floor

Assess whether the interface looks like it was intentionally designed for this audience and product, rather than being interchangeable with a generic AI-generated template. Check and correct:

- Generic composition: unnecessary card grids, card nesting, repetitive icon tiles, oversized headings or landing-page decoration on working tools. Choose layouts and density that support the task.
- Arbitrary aesthetics: unmotivated gradients, glow, blur, excessive rounding/shadows, stray colors, default type or multiple competing accents. Keep intentional choices that fit the approved identity; these patterns are not automatically forbidden by the orchestrator (respect applicable external skill guidance and explain conflicts).
- Weak hierarchy: unclear primary action, competing controls, unaligned elements, inconsistent spacing, typography that fails at real content lengths, and decorative elements with no function.
- Placeholder product thinking: fabricated metrics, generic marketing copy, fake testimonials, fake controls, invented features, misleading future functionality and repetitive filler. Use clearly mock data grounded in the approved product domain.
- Fragile UI: inconsistent components, inaccessible color-only feedback, nonfunctional controls, overflow, mobile layouts that hide core actions, motion without purpose and missing interaction states.
- Design drift: compare the rendered preview with the approved direction, semantic tokens, recurring patterns, earlier approved surfaces and actual use case.

Prioritize defects by user harm and quality impact. Fix substantive problems before presenting the gallery, then rerun the affected checks; use targeted Impeccable refinements such as `distill`, `polish` or other applicable installed playbooks only when justified. Document intentional exceptions, remaining limitations and review status in scratch. Do not rewrite approved behavior or an established identity just to satisfy a heuristic. Do not claim the design is AI-slop-free based only on a detector; qualitative review and the user's explicit approval remain necessary.

## 6. Visual approval is a hard gate

The orchestrator's step 3 owns the actual user-facing request and stop condition. Present the real working HTML path, describe how to test it, and explicitly ask in French to validate the maquettes or write requested modifications. A new direction approval is not gallery approval; a critique score is not gallery approval. No final promotion before explicit feedback. Repeat the same request after each material revision. Approve only the shown revision and approved scope; final documentation links to exactly those visuals and tokens. Existing unchanged approved galleries do not require a fresh review solely to add release records or documentation.
