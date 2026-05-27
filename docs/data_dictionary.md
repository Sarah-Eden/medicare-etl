# Data Dictionary

## Tables

### PROVIDER_DEMOGRAPHICS

One row per unique NPI, split from the provider billing data source file.

| Column                     | Type   | Description                                             |
| -------------------------- | ------ | ------------------------------------------------------- |
| RNDRNG_NPI                 | Number | National Provider Identifier (Primary Key)              |
| RNDRNG_PRVDR_LAST_ORG_NAME | Text   | Last name or organization name                          |
| RNDRNG_PRVDR_FIRST_NAME    | Text   | First name, null for organizations                      |
| RNDRNG_PRVDR_MI            | Text   | Middle initial, null for organizations                  |
| RNDRNG_PRVDR_CRDNTLS       | Text   | Provider Credentials, free text, null for organizations |
| RNDRNG_PRVDR_ENT_CD        | Text   | Entity Code: Individual 'I', Organization 'O'           |
| RNDRNG_PRVDR_ST1           | Text   | Street address line 1                                   |
| RNDRNG_PRVDR_ST2           | Text   | Street address line 2                                   |
| RNDRNG_PRVDR_CITY          | Text   | City                                                    |
| RNDRNG_PRVDR_STATE_ABRVTN  | Text   | State abbreviation                                      |
| RNDRNG_PRVDR_STATE_FIPS    | Text   | State FIPS Code                                         |
| RNDRNG_PRVDR_ZIP5          | Text   | 5-digit zip code, zero padded                           |
| RNDRNG_PRVDR_RUCA          | Number | Rural Urban Classification (RUCA)                       |
| RNDRNG_PRVDR_RUCA_DESC     | Text   | RUCA Description                                        |
| RNDRNG_PRVDR_CNTRY         | Text   | Country Code                                            |
| RNDRNG_PRVDR_TYPE          | Text   | Provider specialty                                      |

### PROVIDER_SERVICES

One row per provider NPI + service code billed.

| Column                        | Type   | Description                                                                                                                   |
| ----------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| RNDRNG_NPI                    | Number | National provider identifier (Primary Key)                                                                                    |
| HCPCS_CD                      | Text   | HCPCS code for the specific service furnished by the provider                                                                 |
| HCPCS_DESC                    | Text   | Short description of the HCPCS code                                                                                           |
| HCPCS_DRUG_IND                | Text   | Is the code listed on the Medicare Part B Drug Average Sales Price (ASP) file.                                                |
| PLACE_OF_SRVC                 | Text   | Place of service: Facility 'F', Non-Facility 'O'                                                                              |
| TOT_BENES                     | Number | Number of distinct Medicare beneficiaries receiving the service for each RNDRNG_NPI, HCPCS_CD and PLACE_OF_SRVC               |
| TOT_BENE_DAY_SRVCS            | Number | Number of distinct Medicare beneficiary/per day services                                                                      |
| RNDRNG_PRVDR_MDCR_PRTCPTG_IND | Text   | Identifies whether the provider participates in Medicare and/or accepts assignment of Medicare allowed amounts.               |
| AVG_SBMTD_CHRG                | Float  | Average of the charges submitted by the provider for the service                                                              |
| AVG_MDCR_ALOWD_AMT            | Float  | Average of the Medicare allowed amount for the service                                                                        |
| AVG_MDCR_PYMT_AMT             | Float  | Average amount paid by Medicare after deductable and coinsurance deducted                                                     |
| AVG_MDCR_STDZD_AMT            | Float  | Average amount paid by Medicare after deductable and coinsurance deducted and after Medicare payment standardization applied. |
| TOT_SRVCS                     | Float  | Number of services provided, metrics used to count may vary between services                                                  |

### HOSPITAL_GENERAL_INFORMATION

Hospital demographic information and group measure performance data.

| Column                                                | Type | Description                             |
| ----------------------------------------------------- | ---- | --------------------------------------- |
| FACILITY_ID                                           | Text | Primary Key                             |
| FACILITY_NAME                                         | Text | Facility name                           |
| ADDRESS                                               | Text | Street address                          |
| CITY_TOWN                                             | Text | City                                    |
| STATE                                                 | Text | State                                   |
| ZIP_CODE                                              | Text | Zip Code, zero padded                   |
| COUNTY_PARISH                                         | Text | County/Parish                           |
| TELEPHONE_NUMBER                                      | Text | Telephone Number                        |
| HOSPITAL_TYPE                                         | Text | Hospital Type                           |
| HOSPITAL_OWNERSHIP                                    | Text | Hospital Ownership                      |
| EMERGENCY_SERVICES                                    | Text | Emergency Services                      |
| MEETS_CRITERIA_FOR_PROMOTING_INTEROPERABILITY_OF_EHRS | Text |                                         |
| MEETS_CRITERIA_FOR_BIRTHING_FRIENDLY_DESIGNATION      | Text |                                         |
| HOSPITAL_OVERALL_RATING                               | Text | Overall Rating                          |
| HOSPITAL_OVERALL_RATING_FOOTNOTE                      | Text | Footnote codes                          |
| MORT_GROUP_MEASURE_COUNT                              | Text | Mortality measure group                 |
| COUNT_OF_FACILITY_MORT_MEASURES                       | Text |                                         |
| COUNT_OF_MORT_MEASURES_BETTER                         | Text |                                         |
| COUNT_OF_MORT_MEASURES_NO_DIFFERENT                   | Text |                                         |
| COUNT_OF_MORT_MEASURES_WORSE                          | Text |                                         |
| MORT_GROUP_FOOTNOTE                                   | Text |                                         |
| SAFETY_GROUP_MEASURE_COUNT                            | Text | Safety of Care measure group            |
| COUNT_OF_FACILITY_SAFETY_MEASURES                     | Text |                                         |
| COUNT_OF_SAFETY_MEASURES_BETTER                       | Text |                                         |
| COUNT_OF_SAFETY_MEASURES_NO_DIFFERENT                 | Text |                                         |
| COUNT_OF_SAFETY_MEASURES_WORSE                        | Text |                                         |
| SAFETY_GROUP_FOOTNOTE                                 | Text |                                         |
| READM_GROUP_MEASURE_COUNT                             | Text | Readmission measure group               |
| COUNT_OF_FACILITY_READM_MEASURES                      | Text |                                         |
| COUNT_OF_READM_MEASURES_BETTER                        | Text |                                         |
| COUNT_OF_READM_MEASURES_NO_DIFFERENT                  | Text |                                         |
| COUNT_OF_READM_MEASURES_WORSE                         | Text |                                         |
| READM_GROUP_FOOTNOTE                                  | Text |                                         |
| PT_EXP_GROUP_MEASURE_COUNT                            | Text | Patient Experience Measures             |
| COUNT_OF_FACILITY_PT_EXP_MEASURES                     | Text |                                         |
| PT_EXP_GROUP_FOOTNOTE                                 | Text |                                         |
| TE_GROUP_MEASURE_COUNT                                | Text | Timely and Efficient Care Measure Group |
| COUNT_OF_FACILITY_TE_MEASURES                         | Text |                                         |
| TE_GROUP_FOOTNOTE                                     | Text |                                         |

### PROVIDER_HOSPITAL_AFFILIATION

Provides the link between provider-hospital tables.

| Column                                     | Type   | Description |
| ------------------------------------------ | ------ | ----------- |
| NPI                                        | Number | Primary Key |
| FACILITY_AFFILIATIONS_CERTIFICATION_NUMBER | Text   | Primary Key |

### MIPS_PERFORMANCE

Publicaly reported final scores and performance category scores for clinicans that participate in the Merit-based Incentive Payment System (MIPS). A null value in any performance category indicates it did not contribute to the final score.

| Column                                      | Type   | Description                                              |
| ------------------------------------------- | ------ | -------------------------------------------------------- |
| NPI                                         | Number | National provider identifier (Primary Key)               |
| ORG_PAC_ID                                  | Text   | PECOS Group ID of the group this person participated in  |
| PROVIDER_LAST_NAME                          | Text   | Last Name                                                |
| PROVIDER_FIRST_NAME                         | Text   | First Name                                               |
| SOURCE                                      | Text   | Method by which the clinician was scored                 |
| FACILITY_BASED_SCORING_CERTIFICATION_NUMBER | Float  | All null, no facility based clinicians in 2023           |
| FACILITY_NAME                               | Float  | All null, no facility based clinicians in 2023           |
| QUALITY_CATEGORY_SCORE                      | Float  | Quality performance category score                       |
| PI_CATEGORY_SCORE                           | Float  | Promoting Interoperability performance category score    |
| IA_CATEGORY_SCORE                           | Float  | Improvement Activities performance category score        |
| COST_CATEGORY_SCORE                         | Float  | Cost performance category score                          |
| FINAL_MIPS_SCORE_WITHOUT_CPB                | Float  | MIPS Final Score without the Complex Patient Bonus (CPB) |
| FINAL_MIPS_SCORE                            | Float  | MIPS Final Score with the CPB                            |

### MIPS_METRICS

Individual measure-level detail for MIPS quality reporting.

| Column              | Type   | Description                                                                                                                                          |
| ------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| NPI                 | Number | PK, FK to PROVIDER_DEMOGRAPHICS                                                                                                                      |
| IND_PAC_ID          | Text   | Individual PECOS Associate Control ID                                                                                                                |
| PROVIDER_LAST_NAME  | Text   |                                                                                                                                                      |
| PROVIDER_FIRST_NAME | Text   |                                                                                                                                                      |
| APM_AFFL_1          | Text   | Alternative Payment Model affiliation 1                                                                                                              |
| APM_AFFL_2          | Text   | APM affiliation 2                                                                                                                                    |
| APM_AFFL_3          | Text   | APM affiliation 3                                                                                                                                    |
| APM_AFFL_4          | Float  | APM affiliation 4, all null in PY2023                                                                                                                |
| MEASURE_CD          | Text   | Measure code (PK)                                                                                                                                    |
| MEASURE_TITLE       | Text   | Measure description                                                                                                                                  |
| INVS_MSR            | Text   | Inverse measure indicator (Y/N)                                                                                                                      |
| ATTESTATION_VALUE   | Text   | Attestation response for yes/no measures                                                                                                             |
| PRF_RATE            | Float  | Performance rate                                                                                                                                     |
| PATIENT_COUNT       | Float  | Number of patients included in the measure denominator                                                                                               |
| STAR_VALUE          | Float  | Star rating assigned based on performance at the measure, stratum, collection type, and entity type level                                            |
| FIVE_STAR_BENCHMARK | Float  | The established ABC™ benchmark used to assign a five-star rating for a given measure and collection type                                             |
| COLLECTION_TYPE     | Text   | ATT for Web Attestation, CLM for Claims, EHR for Electronic Health Record, QCDR for Qualified Clinical Data Registry, and REG for Qualified Registry |
| CCXP_IND            | Text   | Complex care experience indicator (Y/N)                                                                                                              |

### HOSPITAL_COMPLICATIONS_DEATHS

Complication and mortality measures by hospital.

| Column               | Type | Description                                |
| -------------------- | ---- | ------------------------------------------ |
| FACILITY_ID          | Text | PK, FK to HOSPITAL_GENERAL_INFORMATION     |
| FACILITY_NAME        | Text |                                            |
| ADDRESS              | Text |                                            |
| CITY_TOWN            | Text |                                            |
| STATE                | Text |                                            |
| ZIP_CODE             | Text | 5-digit zip code                           |
| COUNTY_PARISH        | Text |                                            |
| TELEPHONE_NUMBER     | Text |                                            |
| MEASURE_ID           | Text | PK                                         |
| MEASURE_NAME         | Text |                                            |
| COMPARED_TO_NATIONAL | Text | Performance vs national rate/value         |
| DENOMINATOR          | Text | Cases in the denominator                   |
| SCORE                | Text | Measure score, may contain "Not Available" |
| LOWER_ESTIMATE       | Text | Lower bound of confidence interval         |
| HIGHER_ESTIMATE      | Text | Upper bound of confidence interval         |
| FOOTNOTE             | Text | Footnote codes, may be comma-separated     |
| START_DATE           | Text | Measurement period start                   |
| END_DATE             | Text | Measurement period end                     |

### HOSPITAL_UNPLANNED_VISITS

Readmission and return visit measures by hospital. Same structure as HOSPITAL_COMPLICATIONS_DEATHS with two additional columns.

| Column                      | Type | Description                                 |
| --------------------------- | ---- | ------------------------------------------- |
| FACILITY_ID                 | Text | PK, FK to HOSPITAL_GENERAL_INFORMATION      |
| FACILITY_NAME               | Text |                                             |
| ADDRESS                     | Text |                                             |
| CITY_TOWN                   | Text |                                             |
| STATE                       | Text |                                             |
| ZIP_CODE                    | Text | 5-digit zip code                            |
| COUNTY_PARISH               | Text |                                             |
| TELEPHONE_NUMBER            | Text |                                             |
| MEASURE_ID                  | Text | PK                                          |
| MEASURE_NAME                | Text |                                             |
| COMPARED_TO_NATIONAL        | Text | Performance vs national rate/value/expected |
| DENOMINATOR                 | Text | Cases in the denominator                    |
| SCORE                       | Text | Measure score, may contain "Not Available"  |
| LOWER_ESTIMATE              | Text | Lower bound of confidence interval          |
| HIGHER_ESTIMATE             | Text | Upper bound of confidence interval          |
| NUMBER_OF_PATIENTS          | Text | Total patients                              |
| NUMBER_OF_PATIENTS_RETURNED | Text | Patients who returned                       |
| FOOTNOTE                    | Text | Footnote codes, may be comma-separated      |
| START_DATE                  | Text | Measurement period start                    |
| END_DATE                    | Text | Measurement period end                      |

### HOSPITAL_HAI

Healthcare-associated infection measures by hospital.

| Column               | Type | Description                                     |
| -------------------- | ---- | ----------------------------------------------- |
| FACILITY_ID          | Text | PK, FK to HOSPITAL_GENERAL_INFORMATION          |
| FACILITY_NAME        | Text |                                                 |
| ADDRESS              | Text |                                                 |
| CITY_TOWN            | Text |                                                 |
| STATE                | Text |                                                 |
| ZIP_CODE             | Text | 5-digit zip code                                |
| COUNTY_PARISH        | Text |                                                 |
| TELEPHONE_NUMBER     | Text |                                                 |
| MEASURE_ID           | Text | PK                                              |
| MEASURE_NAME         | Text |                                                 |
| COMPARED_TO_NATIONAL | Text | Performance vs national benchmark               |
| SCORE                | Text | Standardized Infection Ratio or component value |
| FOOTNOTE             | Text | Footnote codes, may be comma-separated          |
| START_DATE           | Text | Measurement period start                        |
| END_DATE             | Text | Measurement period end                          |

### HOSPITAL_HCAHPS

Hospital Consumer Assessment of Healthcare Providers and Systems survey results.

| Column                                | Type | Description                                                |
| ------------------------------------- | ---- | ---------------------------------------------------------- |
| FACILITY_ID                           | Text | PK, FK to HOSPITAL_GENERAL_INFORMATION                     |
| FACILITY_NAME                         | Text |                                                            |
| ADDRESS                               | Text |                                                            |
| CITY_TOWN                             | Text |                                                            |
| STATE                                 | Text |                                                            |
| ZIP_CODE                              | Text | 5-digit zip code                                           |
| COUNTY_PARISH                         | Text |                                                            |
| TELEPHONE_NUMBER                      | Text |                                                            |
| HCAHPS_MEASURE_ID                     | Text | PK                                                         |
| HCAHPS_QUESTION                       | Text | Survey question or measure category                        |
| HCAHPS_ANSWER_DESCRIPTION             | Text | Response label                                             |
| PATIENT_SURVEY_STAR_RATING            | Text | 1-5 star rating, "Not Applicable" for non-star rows        |
| PATIENT_SURVEY_STAR_RATING_FOOTNOTE   | Text |                                                            |
| HCAHPS_ANSWER_PERCENT                 | Text | Response percentage, "Not Applicable" for star/linear rows |
| HCAHPS_ANSWER_PERCENT_FOOTNOTE        | Text |                                                            |
| HCAHPS_LINEAR_MEAN_VALUE              | Text | Linear mean score for the measure domain                   |
| NUMBER_OF_COMPLETED_SURVEYS           | Text | Completed surveys for this facility                        |
| NUMBER_OF_COMPLETED_SURVEYS_FOOTNOTE  | Text |                                                            |
| SURVEY_RESPONSE_RATE_PERCENT          | Text | Survey response rate                                       |
| SURVEY_RESPONSE_RATE_PERCENT_FOOTNOTE | Text |                                                            |
| START_DATE                            | Text | Measurement period start                                   |
| END_DATE                              | Text | Measurement period end                                     |

## Views

### PROVIDER_PROFILE_VIEW

One row per individual provider. Combines demographics with best MIPS score.

| Column                     | Source                | Description                   |
| -------------------------- | --------------------- | ----------------------------- |
| RNDRNG_NPI                 | PROVIDER_DEMOGRAPHICS |                               |
| RNDRNG_PRVDR_LAST_ORG_NAME | PROVIDER_DEMOGRAPHICS |                               |
| RNDRNG_PRVDR_FIRST_NAME    | PROVIDER_DEMOGRAPHICS |                               |
| RNDRNG_PRVDR_TYPE          | PROVIDER_DEMOGRAPHICS |                               |
| RNDRNG_PRVDR_CITY          | PROVIDER_DEMOGRAPHICS |                               |
| RNDRNG_PRVDR_STATE_ABRVTN  | PROVIDER_DEMOGRAPHICS |                               |
| MAX_MIPS_SCORE             | Derived               | MAX(FINAL_MIPS_SCORE) per NPI |

### PROVIDER_HOSPITAL_INFO_VIEW

One row per provider-hospital pair. Filtered to individual providers only.

| Column                  | Source                       | Description |
| ----------------------- | ---------------------------- | ----------- |
| RNDRNG_NPI              | PROVIDER_DEMOGRAPHICS        |             |
| FACILITY_ID             | HOSPITAL_GENERAL_INFORMATION |             |
| FACILITY_NAME           | HOSPITAL_GENERAL_INFORMATION |             |
| HOSPITAL_OVERALL_RATING | HOSPITAL_GENERAL_INFORMATION |             |

### HOSPITAL_QUALITY_SUMMARY_VIEW

One row per facility-measure. Combines complications/deaths, unplanned visits, and HAI into a single view. HAI filtered to SIR summary measures only.

| Column                        | Source        | Description                                                                            |
| ----------------------------- | ------------- | -------------------------------------------------------------------------------------- |
| FACILITY_ID                   | Source tables |                                                                                        |
| SOURCE                        | Derived       | Table of origin: "HAI", "Complications Deaths", or "Unplanned Visits"                  |
| MEASURE_ID                    | Source tables |                                                                                        |
| MEASURE_NAME                  | Source tables |                                                                                        |
| COMPARED_TO_NATIONAL          | Source tables | Original CMS comparison text                                                           |
| SCORE                         | Source tables |                                                                                        |
| COMPARED_TO_NATIONAL_CATEGORY | Derived       | Standardized to: Better, Worse, No Different, Not Available, Number of Cases Too Small |

### HCAHPS_SUMMARY_VIEW

One row per facility per star rating domain. 11 rows per facility.

| Column                       | Source          | Description     |
| ---------------------------- | --------------- | --------------- |
| FACILITY_ID                  | HOSPITAL_HCAHPS |                 |
| HCAHPS_MEASURE_ID            | HOSPITAL_HCAHPS |                 |
| HCAHPS_QUESTION              | HOSPITAL_HCAHPS |                 |
| PATIENT_SURVEY_STAR_RATING   | HOSPITAL_HCAHPS | 1-5 star rating |
| NUMBER_OF_COMPLETED_SURVEYS  | HOSPITAL_HCAHPS |                 |
| SURVEY_RESPONSE_RATE_PERCENT | HOSPITAL_HCAHPS |                 |

### HCAHPS_DETAILED_VIEW

One row per facility per survey response. 72 rows per facility. Excludes star rating and linear mean score rows.

| Column                       | Source          | Description |
| ---------------------------- | --------------- | ----------- |
| FACILITY_ID                  | HOSPITAL_HCAHPS |             |
| HCAHPS_MEASURE_ID            | HOSPITAL_HCAHPS |             |
| HCAHPS_QUESTION              | HOSPITAL_HCAHPS |             |
| HCAHPS_ANSWER_DESCRIPTION    | HOSPITAL_HCAHPS |             |
| HCAHPS_ANSWER_PERCENT        | HOSPITAL_HCAHPS |             |
| NUMBER_OF_COMPLETED_SURVEYS  | HOSPITAL_HCAHPS |             |
| SURVEY_RESPONSE_RATE_PERCENT | HOSPITAL_HCAHPS |             |
