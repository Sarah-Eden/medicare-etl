# Medicare Provider & Hospital Quality ETL Pipeline

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=fff)](#)
[![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?logo=snowflake&logoColor=fff)](#)

## Project Overview

An ETL pipeline that loads CMS Medicare public data into Snowflake for provider and hospital quality analysis. Nine source files are cleaned, standardized, and loaded into ten tables with referential integrity. Snowflake views combine provider demographics, MIPS performance scores, hospital affiliations, and hospital quality measures into a unified data layer for dashboard development.

## Data

- **Source:** [CMS Provider Data Catalog](https://data.cms.gov)
- **Analysis Period:** 2023
- **Scope:** 1.17M providers, 5,400 hospitals, 478K MIPS-scored clinicians
- **Tables:** 10 base tables, 5 views
  Source files come from multiple CMS archives to align on the 2023 analysis period. See [docs/data_sources.md](docs/data_sources.md) for download links and archive selection rationale.

## Pipeline

`main.py` orchestrates the full pipeline. A single transform function in `transforms/transforms.py` handles all source files through parameterized cleaning: dtype overrides, row filtering, column selection, and column name standardization. The provider billing file is split into demographics (one row per NPI) and services (one row per NPI + HCPCS code) tables.

Data is loaded into Snowflake using `write_pandas` with `auto_create_table=True`. Primary and foreign key constraints are applied via `sql/constraints.sql`.

## Schema

The pipeline produces two provider tables, one hospital demographics table, one provider-hospital affiliation table, two MIPS tables, and four hospital quality tables.

Provider tables link to hospital data through the affiliation table, which maps NPI to facility certification number. MIPS tables link to providers on NPI.

Five views were created from the base tables:

- **provider_profile_view** — one row per individual provider with best MIPS score
- **provider_hospital_info_view** — provider-hospital affiliations with hospital name and rating
- **hospital_quality_summary_view** — complications, unplanned visits, and HAI measures with standardized comparison categories
- **hcahps_summary_view** — patient experience star ratings by domain
- **hcahps_detailed_view** — patient experience survey response percentages

## Project Structure

```
medicare-etl/
├── main.py
├── requirements.txt
├── transforms/
│   ├── transforms.py
│   └── utils.py
├── sql/
│   ├── constraints.sql
│   └── views.sql
└── docs/
    ├── data_sources.md
    ├── data_dictionary.md
    └── transform_notes.md
```

## Limitations

- This data covers Medicare fee-for-service only. Commercial and Medicaid billing are not represented.
- MIPS scores are available for approximately 43% of individual providers. Coverage is limited by MIPS eligibility thresholds.
- Submitted charges are provider-set and not meaningful for cost comparison. Standardized amounts should be used instead.
- No unique patient count is derivable from this data.
- The pipeline uses drop-and-recreate loading. Incremental loading is not implemented.

## How To Run

```bash
git clone https://github.com/Sarah-Eden/medicare-etl.git
cd medicare-etl
pip install -r requirements.txt
```

Create a `.env` file with Snowflake credentials:

```
SF_ACCOUNT=your_account
SF_USER=your_user
SF_PASSWORD=your_password
SF_ROLE=your_role
SF_DATABASE=your_database
SF_SCHEMA=your_schema
SF_WAREHOUSE=your_warehouse
```

Download source files from CMS (see [docs/data_sources.md](docs/data_sources.md)) and place them in a `data/` directory.

```bash
python main.py
```

After loading, run `sql/constraints.sql` and `sql/views.sql` in Snowflake to apply keys and create views.
