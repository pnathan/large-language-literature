# Gilgameš Edition — project briefing

## What this is
An original English translation of the complete Epic of Gilgameš, made line-by-line against
the Akkadian of the electronic Babylonian Library (eBL) critical editions, delivered as
self-contained HTML in a lapis-and-gold design. Three published forms:

- `out/gilgamesh-complete.html` — the Standard Babylonian epic entire (12 tablets,
  2,683 lines), parallel Akkadian/English, tablet-end apparatus.
- `out/gilgamesh-old-babylonian.html` — all 14 OB witnesses (882 lines), with a
  three-panel synopsis against the SB text.
- `out/gilgamesh-reader.html` — the crown piece. Talmudic daf layout: 156 titled
  pericopes down the center; inner margin = philological glosses; outer margin =
  discursive notes + a slate-blue "resonance" register (≈) for Akkadian wordplay the
  English misses; four "partings of the ways" where the page splits into OB|SB columns;
  seven museum plates embedded base64.
- `out/gilgamesh-reader-web.html` — identical, but plates hotlinked from Wikimedia
  Commons (698 KB vs 2.2 MB) for publishing.

## Build pipeline (Python 3, stdlib + Pillow only)
- `src/SB_*.json`, `src/OB_*.json` — raw eBL chapter editions.
  Refetch: `https://www.ebl.lmu.de/api/texts/L/1/4/chapters/Standard%20Babylonian/{I..XII}`
  and `.../Old%20Babylonian/{II,III,UM,Schøyen₁..₃,Nippur,Harmal₁..₂,Ishchali,IM,VA+BM,CUNES,SM}`
  (URL-encode the fancy names).
- `src/tr_*.tsv`, `src/obtr_*.tsv` — the translations. Format: `number<TAB>English`.
  Numbers must match eBL number strings exactly (`208a`, `a+1'`, `12-13`, primes).
  Lines absent from a TSV render as `[ ... ]`.
- `src/meta.py` — SB tablet titles, headnotes, apparatus.
- `src/perimeta.py` — pericope boundaries/captions, note-side assignment, OB
  cross-notes, split-spread definitions.
- `src/resmeta.py` — resonance notes (RES) and plate captions/credits (FIGCAP).
- `src/style.css` — the extracted lapis design (a full `<style>` block).
- `src/figc_*.jpg` — recompressed plates (Wikimedia Commons, credits in FIGCAP).
- Builders: `src/build.py` (complete), `src/obbuild.py` (OB), `src/readerbuild.py`
  (reader; env `EMBED_PLATES=0` → hotlinked `-web` variant).
  All write into `/mnt/user-data/outputs/` — **change the output paths to `../out/`**
  (they were written for a sandbox; this is the one required edit before first build).

## Editorial rules (do not violate)
1. The English is original. Never substitute A. R. George's or eBL's translations.
2. `[Bracketed]` English translates restored Akkadian only; keep bracket discipline.
3. Refrains are standardized across tablets (journey formula, cheeks-hollow
   interrogation, "swift mule" apostrophe, wall-circuit I 18–23 = XI 323–328).
   Change one instance and you must change all.
4. Tablet XII stays an appendix with its contradiction of VIII stated.
5. Šiduri's carpe-diem speech is OB-only; it must never migrate into the SB text.
   Its home is the OB file and the Tablet X parting in the reader.
6. Plates are real artifacts with credits — no synthetic imagery.

## Known state / open tasks
- The reader renders correctly as a standalone page in any browser; the claude.ai
  mobile artifact viewer struggles with it (size + sticky-margin grid). Likely first
  task: publish properly — e.g. `git init`, push to GitHub Pages / Netlify / Vercel
  as a static site (no build step needed; the HTML is complete).
- Possible refinements: fold the sticky margins into <details> on narrow screens;
  split the reader into per-tablet pages with prev/next nav for lighter loads;
  add an index of resonances; print stylesheet tuning for a PDF edition.
- Verification helpers exist inline in the builders (counts of pericopes=156,
  partings=4, res notes=15, plates=7, SB rows=2683, OB rows=882).

## Provenance
eBL retrieved 25–26 Aug 2026. Design thesis: the page is the lapis tablet of SB I 27
(*išâm-ma ṭuppi uqnî šitassi*). Colophon: *kīma labīrīšu šaṭir-ma bari*.
