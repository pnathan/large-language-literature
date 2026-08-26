# Large-Language Literature

Original editions and redactions of ancient and classical texts, published as
self-contained HTML pages on GitHub Pages.

Live site: `https://pnathan.github.io/large-language-literature/`

## Repository structure

```
docs/                   ← GitHub Pages root (deployed on push to trunk)
  index.html            ← neutral top-level landing page (links to each work)
  gilgamesh/            ← published Gilgameš editions
  faerie-queene/        ← published Faerie Queene edition
gilgamesh/              ← Gilgameš source: eBL data, translations, Python builders
faerie-queene/          ← Faerie Queene source: README, provenance notes
.github/workflows/      ← Pages deployment workflow
```

Each work follows the same pattern:
- **`<work>/`** at the repo root holds source material (data files, build scripts,
  editorial metadata). See the subfolder's own `CLAUDE.md` for details.
- **`docs/<work>/`** holds the published HTML and assets, served by GitHub Pages.
- **`docs/index.html`** has a card linking to each work.

## Branching and deployment

- Default branch: **`trunk`**
- GitHub Pages deploys from `docs/` on every push to `trunk` that touches `docs/**`
  (see `.github/workflows/pages.yml`). Manual dispatch is also enabled.
- No build step is needed for deployment — the HTML files in `docs/` are complete
  and self-contained (or use relative-pathed assets in their own subfolder).

## Top-level index design

`docs/index.html` is a **layout-neutral** landing page — light/dark theme-aware
(CSS custom properties, `prefers-color-scheme`, `data-theme` attribute), using
Cormorant Garamond + Inter. It does not adopt any single work's visual identity.

When adding a new work, add a card inside the `.works` div matching the existing
pattern (sigil, title, language/author line, description, stats).

## Adding a new work

1. Create `<work>/` at the repo root with source files and a `CLAUDE.md`.
2. Create `docs/<work>/` with the published HTML and any assets (images, fonts).
3. Add a back link in the work's page pointing to `../` (the parent index).
4. Add a card to `docs/index.html`.
5. Push to `trunk` (or merge a PR) — Pages deploys automatically.

## Working practices for new translation works

- **One PR per work.** All commits for a given work — scaffolding, sourced witness
  data, translations, the published page — land on a single branch/PR from start to
  finish. Don't split one work's development across multiple PRs; open the next PR
  only when starting the next work.
- **Model/effort tiers for subagents.** Default to the cheapest tier that can do the
  job: Haiku for mechanical work (fetching, formatting, list compilation); Sonnet at
  low effort for translation and source-verification agents (literary/philological
  judgment still needs Sonnet-class capability, but rarely needs high effort).
  Reserve higher tiers/effort only when a task demonstrably needs it. The Fable
  review pass (below) is chosen for an independent voice, not swapped for cost
  reasons.
- **No existing translations.** Translate only from primary-source witnesses
  (manuscripts, papyri, testimonia, or equivalent) fetched and cited for real —
  never from a model's memory of the source text, and never by consulting an
  existing published translation. Record every distinct witness/recension and its
  variants rather than silently collapsing to one "best" text. Each work's own
  `CLAUDE.md` documents its specific source landscape; this is the shared baseline.
- **Fable review.** Every subagent-produced translation gets an independent review
  pass on the Fable model, checking fidelity to the source and flagging any
  suspicious resemblance to a known published translation (a sign of memorization
  leakage rather than genuine translation).

## Current works

| Work | Source | Language | Scale |
|------|--------|----------|-------|
| The Epic of Gilgameš | eBL critical editions (Akkadian) | Akkadian → English | 2,683 SB lines, 882 OB lines, 3 editions |
| The Faerie Queene | J. C. Smith, Clarendon 1909 | Early Modern English → modernized | 3,856 stanzas, 75 cantos, 38 plates |
