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
  guest-house/          ← published Guest-House (Masnavi V) edition
gilgamesh/              ← Gilgameš source: eBL data, translations, Python builders
faerie-queene/          ← Faerie Queene source: README, provenance notes
guest-house/            ← Guest-House source: translation, source research
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

## Current works

| Work | Source | Language | Scale |
|------|--------|----------|-------|
| The Epic of Gilgameš | eBL critical editions (Akkadian) | Akkadian → English | 2,683 SB lines, 882 OB lines, 3 editions |
| The Faerie Queene | J. C. Smith, Clarendon 1909 | Early Modern English → modernized | 3,856 stanzas, 75 cantos, 38 plates |
| The Guest-House passages | Nicholson critical edition (Masnavi V) | Classical Persian → English | 35 couplets, 2 passages + framing |
