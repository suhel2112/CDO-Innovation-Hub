# dbt Analytics Lakehouse Demo (CI/CD + Environments)

This project demonstrates **dbt analytics engineering** with:
- **CI/CD** using GitHub Actions (PR checks + main deploy)
- **Environment switching** via `DBT_TARGET` (`dev`, `stage`, `prod`)
- dbt **materializations**: `view`, `table`, `ephemeral`, `incremental`
- Tests: `unique`, `not_null`, `relationships`
- Artifacts uploaded from CI: `manifest.json`, `run_results.json`, `catalog.json`

## Quickstart (Windows / Conda)
```bat
conda activate dbt-demo
pip install -r requirements.txt

cd analytics
set DBT_TARGET=dev
dbt deps
dbt seed --full-refresh
dbt build --fail-fast