# Data Sources

All data is publicly available from the Centers for Medicare & Medicaid Services (CMS) data site. As CMS does not have a standardized reporting period for all data, the source files used in this pipeline come from multiple archives. The analysis period selected was based on the dataset with the longest delay in publication. At the time this project was completed, the latest published provider services data available was for 2023.

## Source Files

### Provider Billing Data

**File:** MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv
**Source:** [Medicare Physician & Other Practitioners - by Provider and Service](https://data.cms.gov/provider-summary-by-type-of-service/medicare-physician-other-practitioners/medicare-physician-other-practitioners-by-provider-and-service)
**Year:** 2023
**Records:** ~9.66 million rows with ~1.17 million unique providers
**Snowflake Tables:** provider_demographics, provider_services

### Hospital General Information

**File:** Hospital_General_Information.csv
**Source:** [Hospitals Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/hospitals)
**Archive Date:** 11/06/2023
**Records:** 5,439 rows/unique facilities
**Snowflake Table:** hospital_general_information

### Facility Affiliation

**File:** Facility_Affiliation.csv
**Source:** [Doctors and Clinicians Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/doctors-clinicians)
**Archive Date:** 12/21/2023
**Records:** ~1.63 million rows, 837,057 unique NPIs, 38,987 unique facilities
**Snowflake Table:** provider_hospital_affiliation

### MIPS Performance

**File:** ec_score_file.csv
**Source:** [Doctors and Clinicians Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/doctors-clinicians)
**Archive Date:** 12/18/2025 (Performance Year 2023)
**Records:** 541,344 rows, 477,587 unique NPIs
**Snowflake Table:** mips_performance

### MIPS Quality Measures

**File:** ec_public_reporting.csv
**Source:** [Doctors and Clinicians Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/doctors-clinicians)
**Archive Date:** 12/18/2025 (Performance Year 2023)
**Records:** 539,928 rows, 36,669 unique NPIs
**Snowflake Table:** mips_metrics

### Complications and Deaths

**File:** Complications_and_Deaths-Hospital.csv
**Source:** [Hospitals Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/hospitals)
**Archive Date:** 11/26/2025
**Records:** 95,820 rows, 4,791 unique facilities
**Snowflake Table:** hospital_complications_deaths

### Unplanned Hospital Visits

**File:** Unplanned_Hospital_Visits-Hospital.csv
**Source:** [Hospitals Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/hospitals)
**Archive Date:** 11/26/2025
**Records:** 67,074 rows, 4,791 unique facilities
**Snowflake Table:** hospital_unplanned_visits

### Healthcare Associated Infections (HAI)

**File:** Healthcare_Associated_Infections.csv
**Source:** [Hospitals Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/hospitals)
**Archive Date:** 10/30/2024
**Records:** 172,044 rows, 4,779 unique facilities
**Snowflake Table:** hospital_hai

### Hospital Consumer Assessment of Healthcare Providers and Systems (HCAHPS)

**File:** HCAHPS-Hospital.csv
**Source:** [Hospitals Archived Data Snapshots](https://data.cms.gov/provider-data/archived-data/hospitals)
**Archive Date:** 10/30/2024
**Records:** 444,447 rows, 4,779 unique facilities
**Snowflake Table:** hospital_hcahps
