import os

files_to_create = {
    "README.md": "# Future Harvest\n\nNASA Earth data turned into resilient crop rotations for Bangladeshi farmers.\n\n## Mission\nAn AI agent that helps smallholder farmers in Bangladesh decide what to plant next.\n\n## What it does\n1. Ask\n2. Locate\n3. Observe\n4. Rank\n\n## NASA Data Sources\n- NASA POWER\n- NASA SMAP\n- NASA GPM IMERG\n- NASA MODIS / VIIRS\n\n## Quick Start\n```bash\npip install -r backend/requirements.txt\n```\n",
    "LICENSE": "MIT License\n\nCopyright (c) 2026 DIU_Future_Harvest\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files...",
    ".gitignore": "venv/\n__pycache__/\n*.db\n.env\n.DS_Store\n",
    ".env.example": "EARTHDATA_USERNAME=\nEARTHDATA_PASSWORD=\nLLM_KEY=\nDB_PATH=sqlite:///future_harvest.db\n",
    "docs/mission.md": "# Mission\nHelping Bangladeshi farmers with AI and NASA data.\n",
    "docs/data-sources.md": "# Data Sources\n- NASA POWER (no login)\n- NASA SMAP (Earthdata login)\n- NASA GPM IMERG (Earthdata login)\n- NASA MODIS / VIIRS (Earthdata login, LP DAAC or AppEEARS)\n- Open-Meteo\n- SRDI soil rasters\n- BRRI / IRRI AWD maps\n",
    "docs/architecture.md": "# Architecture\n```mermaid\nflowchart TD\n    A[User] -->|Chat| B(Agent)\n    B --> C{NASA Data}\n```\n",
    "docs/schema.md": "# Schema\n```mermaid\nerDiagram\n    FARM ||--o{ OBSERVATION : has\n```\n",
    "docs/scoring.md": "# Scoring\nHeuristics pending agronomist validation.\n",
    "docs/failure-handling.md": "# Failure Handling\nCache first, fetch on miss or stale, retry, fall back to stale cache with a stale flag, otherwise return 'no data'.\n",
    "docs/demo-script.md": "# Demo Script\n1. Setup\n2. Geocode\n3. Fetch NASA data\n4. Rank\n5. Show evidence trace\n",
    "docs/verification-checklist.md": "# Verification Checklist\n- [ ] NASA POWER (TODO: verify)\n- [ ] NASA SMAP (TODO: verify)\n",
    "docs/acknowledgments.md": "# Acknowledgments\nThanks to NASA Earthdata.\n",
    "backend/app/main.py": "from fastapi import FastAPI\n\napp = FastAPI()\n\n@app.get('/')\ndef read_root():\n    return {'Hello': 'World'}\n",
    "backend/app/agent/agent.py": "# Agent Loop\n",
    "backend/app/agent/tools_registry.py": "# Tool Registry\n",
    "backend/app/agent/prompts.py": "# Prompts\n",
    "backend/app/tools/geocode.py": "# Geocode Tool\n",
    "backend/app/tools/nasa_climate_profile.py": "# NASA Climate Profile Tool\n",
    "backend/app/tools/vegetation_trend.py": "# Vegetation Trend Tool\n",
    "backend/app/tools/lookup_soil_texture.py": "# Soil Texture Tool\n",
    "backend/app/tools/lookup_awd.py": "# AWD Tool\n",
    "backend/app/tools/get_weather_forecast.py": "# Weather Forecast Tool\n",
    "backend/app/tools/rotation_planner.py": "# Rotation Planner Tool\n",
    "backend/app/nasa/power.py": "# NASA POWER Client (TODO: verify)\n",
    "backend/app/nasa/smap.py": "# NASA SMAP Client (TODO: verify)\n",
    "backend/app/nasa/imerg.py": "# NASA IMERG Client (TODO: verify)\n",
    "backend/app/nasa/modis_viirs.py": "# NASA MODIS/VIIRS Client (TODO: verify)\n",
    "backend/app/nasa/normalizer.py": "# Normalizer\n",
    "backend/app/cache/cache.py": "# SQLite Cache\n",
    "backend/app/scoring/features.py": "# Features\n",
    "backend/app/scoring/score_rotation.py": "# Score Rotation\n",
    "backend/app/db/models.py": "# SQLAlchemy Models\n",
    "backend/pyproject.toml": "[tool.poetry]\nname = \"future-harvest\"\nversion = \"0.1.0\"\n",
    "backend/requirements.txt": "fastapi\nuvicorn\nsqlalchemy\n",
    "frontend/index.html": "<!DOCTYPE html>\n<html>\n<body>\n<h1>Future Harvest</h1>\n</body>\n</html>\n",
    "data/sample/demo_data.json": '{"sample": true}\n',
    "data/crops.json": '[]\n',
    "data/scenarios.json": '[]\n',
    "scripts/prewarm_cache.py": "print('Prewarming cache...')\n",
    "scripts/check_endpoints.py": "print('Checking endpoints...')\n",
    ".github/ISSUE_TEMPLATE/bug_report.md": "name: Bug report\nabout: Create a report to help us improve\ntitle: ''\nlabels: ''\nassignees: ''\n",
    ".github/workflows/ci.yml": "name: CI\non: [push]\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n    - uses: actions/checkout@v3\n",
}

for filepath, content in files_to_create.items():
    dir_name = os.path.dirname(filepath)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    with open(filepath, 'w') as f:
        f.write(content)

print("Scaffolding complete.")
