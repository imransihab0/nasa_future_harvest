# Prompt: scaffold the Future Harvest repo for NASA Space Apps

Paste everything below the line into your AI coding agent. Put the file `nasa_data_and_schema.md` (the one with the Mermaid diagrams) in the project folder first, or attach it to the chat.

Before you paste, fill in the three placeholders in square brackets: [TEAM NAME], [CHALLENGE NAME], [GITHUB USERNAME].

---

You are a senior engineer setting up a hackathon repository. Build the full repository for **Future Harvest**, a NASA Space Apps Challenge project. Read `nasa_data_and_schema.md` completely first. It is the single source of truth for the data sources, tools, database schema, fetch flow, failure handling and scoring. Do not contradict it.

## Project facts

- **Name:** Future Harvest
- **Tagline:** NASA Earth data turned into resilient crop rotations for Bangladeshi farmers.
- **Team:** [TEAM NAME]
- **Challenge:** [CHALLENGE NAME]
- **Description:** An AI agent that helps smallholder farmers in Bangladesh decide what to plant next. The farmer describes a field in Bangla or English, for example "2 acres in Bogura, clay-loam, limited water". The agent geocodes the location, pulls NASA Earth observation data, derives climate and vegetation features, and ranks crop rotations with a deterministic Python scorer (resilience score 0 to 100, weighted by the farmer's priorities). Every ranking ships with an evidence trace. Stale or missing data is flagged, never hidden.
- **NASA sources (these four only are called "NASA data"):**
  - NASA POWER: T2M, T2M_MAX, T2M_MIN, PRECTOTCORR, ALLSKY_SFC_SW_DWN (no login)
  - NASA SMAP: surface and root-zone soil moisture (Earthdata login)
  - NASA GPM IMERG: daily precipitation (Earthdata login)
  - NASA MODIS / VIIRS: NDVI, EVI (Earthdata login, LP DAAC or AppEEARS)
- **Non-NASA supporting sources (always labelled as such):** Open-Meteo (geocoding, 14-day forecast), SRDI soil rasters, BRRI / IRRI AWD maps.

## Theme

Use a clear NASA Space Apps theme in naming and docs: mission-style language ("Mission", "Data Sources", "Flight Plan", "Telemetry"), a dark navy and white palette with one warm accent, and a space-to-field story. Keep it professional. Do **not** copy or recreate the NASA logo, the Space Apps logo or the NASA "meatball". Use a text wordmark only, and add a short "Acknowledgments" section crediting NASA data providers.

## Repository layout

Create this structure (adjust only if the md file requires it):

```
future-harvest/
  README.md
  LICENSE                  (MIT)
  .gitignore
  .env.example             (EARTHDATA_USERNAME, EARTHDATA_PASSWORD or token, LLM key, DB path)
  docs/
    mission.md             (problem, users, why it matters)
    data-sources.md        (table from the md, access, auth, refresh cadence, status)
    architecture.md        (all Mermaid diagrams from the md, copied exactly)
    schema.md              (ER diagram and table notes)
    scoring.md             (variable-to-score mapping, formulas, assumptions)
    failure-handling.md    (cache, retry, stale, no-data rules)
    demo-script.md         (the 5-step live demo and the backup plan)
    verification-checklist.md  (endpoints and variables to confirm before the demo)
    acknowledgments.md
  backend/
    app/
      main.py              (FastAPI, streamed responses)
      agent/               (agent loop, tool registry, prompts)
      tools/               (geocode, nasa_climate_profile, vegetation_trend,
                            lookup_soil_texture, lookup_awd, get_weather_forecast,
                            rotation_planner)
      nasa/                (one client per source: power.py, smap.py, imerg.py,
                            modis_viirs.py, plus normalizer.py)
      cache/               (SQLite cache, cache key, freshness rules)
      scoring/             (features.py, score_rotation.py)
      db/                  (SQLAlchemy models for every table in the ER diagram, migrations)
    tests/
    pyproject.toml
  frontend/
    (chat and map dashboard; ranked rotations, season plan, evidence trace panel)
  data/
    sample/                (small clearly labelled sample files for offline demo)
    crops.json             (CROP table seed)
    scenarios.json         (CLIMATE_SCENARIO seed)
  scripts/
    prewarm_cache.py       (fetch and cache data for the demo field)
    check_endpoints.py     (hits each planned endpoint and reports pass or fail)
  .github/
    ISSUE_TEMPLATE/
    workflows/ci.yml
```

## Rules you must follow

1. **Never invent facts.** Endpoints, dataset names and variable names are the planned ones from the md file. Mark every one as `TODO: verify` in the code and in `docs/verification-checklist.md`. Do not claim a call works unless you ran it.
2. **No fabricated data.** Any sample or fixture data must live in `data/sample/`, be labelled "sample", and never appear in the UI as real NASA output. The UI must show source, `fetched_at` and `quality_flag` for every value.
3. **Normalized shape.** All four NASA sources reduce to the observation shape in section 7 of the md file. Cache key is `(field_id, source_id, variable, obs_date)`. Refresh: POWER and IMERG daily, SMAP every few days, MODIS/VIIRS every 8 to 16 days.
4. **Failure handling exactly as in section 4:** cache first, fetch on miss or stale, retry, fall back to stale cache with a stale flag, otherwise return "no data" and let the agent say so. Never guess.
5. **Scoring is deterministic Python.** The language model chooses which tools to call and writes the explanation. It never computes or alters scores. Same inputs must give the same ranking. Store the evidence as `evidence_json` on every score.
6. **Bangla and English** are both supported in the chat input and output. Keep UI strings in a translation file.
7. **Secrets** go only in `.env`. Never commit credentials. Provide `.env.example`.
8. Mark the scoring weights and thresholds as heuristics pending agronomist validation, in `docs/scoring.md` and in the README.
9. Be honest about limits in the README: SMAP is coarse, so field-level moisture is an estimate; the forecast comes from Open-Meteo, not NASA.

## README.md contents

Write a polished README with, in order: title and tagline; one-paragraph mission; "What it does" with a 4-step flow (Ask, Locate, Observe, Rank); NASA data sources table (with the four NASA sources clearly separated from supporting sources); architecture diagram (the Mermaid flowchart from the md); quick start (install, `.env`, prewarm cache, run backend, run frontend); demo walkthrough; project structure; honest limitations; roadmap (Now, Next, Pilot); team; acknowledgments; license.

## Optional innovation (build as stubs with docs, do not block the main build)

- **Season Replay:** re-run each ranked rotation on the last five seasons of cached NASA data and report whether it would have survived the worst dry spell.
- **Confidence Badge:** High, Medium or Low per score, computed from `quality_flag`, data freshness and source coverage.
Create the interfaces, a doc page for each in `docs/`, and mark them "proposed" until implemented.

## Working method

1. Show me a short plan and the file tree first, then wait for my go-ahead.
2. Build in stages: repo skeleton and docs, then database and cache, then NASA clients, then tools and agent loop, then scoring, then frontend, then tests and CI.
3. After each stage, run what can be run (tests, linters, `check_endpoints.py`) and report results truthfully, including failures and anything that could not be verified.
4. Use clear commit messages, one commit per stage.
5. At the end, list everything still marked `TODO: verify` and everything that needs my credentials.
