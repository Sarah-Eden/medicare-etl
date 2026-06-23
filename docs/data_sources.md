# Data Sources

All data is publicly available from the Centers for Medicare & Medicaid Services (CMS) data site. As CMS does not have a standardized reporting period for all data, the source files used in this pipeline come from multiple archives. The analysis period selected was based on the dataset with the longest delay in publication. At the time this project was completed, the latest published provider services data available was for 2023.

## Source Files

### Provider Billing Data

**File:** MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv
**Source:** [Medicare Physician & Other Practitioners - by Provider and Service](https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service)
**Year:** 2023
**Snowflake Tables:** PROVIDER_DEMOGRAPHICS, PROVIDER_SERVICES

### Provider Practice Data

**File:** Medicare_Physician_Other_Practitioners_by_Provider_2023.csv
**Source:** [Medicare Physician & Other Practitioners - by Provider](https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider)
**Year:** 2023
**Snowflake Table:** PROVIDER_SUMMARY

### Hospital General Information

**File:** Hospital_General_Information.csv
**Source:** [Hospitals Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/hospitals)
**Archive Date:** 11/06/2023
**Snowflake Table:** HOSPITAL_GENERAL_INFORMATION

### Facility Affiliation

**File:** Facility_Affiliation.csv
**Source:** [Doctors and Clinicians Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/doctors-clinicians)
**Archive Date:** 12/21/2023
**Snowflake Table:** PROVIDER_HOSPITAL_AFFILIATION

### MIPS Performance

**File:** ec_score_file.csv
**Source:** [Doctors and Clinicians Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/doctors-clinicians)
**Archive Date:** 12/18/2025 (Performance Year 2023)
**Snowflake Table:** MIPS_PERFORMANCE

### MIPS Quality Measures

**File:** ec_public_reporting.csv
**Source:** [Doctors and Clinicians Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/doctors-clinicians)
**Archive Date:** 12/18/2025 (Performance Year 2023)
**Snowflake Table:** MIPS_METRICS

### Complications and Deaths

**File:** Complications_and_Deaths-Hospital.csv
**Source:** [Hospitals Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/hospitals)
**Archive Date:** 11/26/2025
**Snowflake Table:** HOSPITAL_COMPLICATIONS_DEATHS

### Unplanned Hospital Visits

**File:** Unplanned_Hospital_Visits-Hospital.csv
**Source:** [Hospitals Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/hospitals)
**Archive Date:** 11/26/2025
**Snowflake Table:** HOSPITAL_UNPLANNED_VISITS

### Healthcare Associated Infections (HAI)

**File:** Healthcare_Associated_Infections_Hospital.csv
**Source:** [Hospitals Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/hospitals)
**Archive Date:** 10/30/2024
**Snowflake Table:** HOSPITAL_HAI

### Hospital Consumer Assessment of Healthcare Providers and Systems (HCAHPS)

**File:** HCAHPS-Hospital.csv
**Source:** [Hospitals Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/hospitals)
**Archive Date:** 10/30/2024
**Snowflake Table:** HOSPITAL_HCAHPS

### RUCA Zip Code Categories

**File:** RUCA-codes-2020-zipcode.csv
**Source:** [USDA Rural-Urban Commuting Area Codes](https://www.ers.usda.gov/data-products/rural-urban-commuting-area-codes)
**Snowflake Table:** RUCA_ZIP_CODES
