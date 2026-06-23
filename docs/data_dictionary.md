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
| RNDRNG_NPI                    | Number | National provider identifier (Primary Key, Foreign Key to PROVIDER_DEMOGRAPHICS)                                              |
| HCPCS_CD                      | Text   | HCPCS code for the specific service furnished by the provider (Primary Key)                                                   |
| HCPCS_DESC                    | Text   | Short description of the HCPCS code                                                                                           |
| HCPCS_DRUG_IND                | Text   | Is the code listed on the Medicare Part B Drug Average Sales Price (ASP) file.                                                |
| PLACE_OF_SRVC                 | Text   | Place of service: Facility 'F', Non-Facility 'O'                                                                              |
| TOT_BENES                     | Number | Number of distinct Medicare beneficiaries receiving the service for each RNDRNG_NPI, HCPCS_CD and PLACE_OF_SRVC               |
| TOT_BENE_DAY_SRVCS            | Number | Number of distinct Medicare beneficiary/per day services                                                                      |
| RNDRNG_PRVDR_MDCR_PRTCPTG_IND | Text   | Identifies whether the provider participates in Medicare and/or accepts assignment of Medicare allowed amounts.               |
| AVG_SBMTD_CHRG                | Float  | Average of the charges submitted by the provider for the service                                                              |
| AVG_MDCR_ALOWD_AMT            | Float  | Average of the Medicare allowed amount for the service                                                                        |
| AVG_MDCR_PYMT_AMT             | Float  | Average amount paid by Medicare after deductible and coinsurance deducted                                                     |
| AVG_MDCR_STDZD_AMT            | Float  | Average amount paid by Medicare after deductible and coinsurance deducted and after Medicare payment standardization applied. |
| TOT_SRVCS                     | Float  | Number of services provided, metrics used to count may vary between services                                                  |

### PROVIDER_SUMMARY

One row per unique NPI.

| Column                           | Type    | Description                                                                                                                                                                                               |
| -------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RNDRNG_NPI                       | Integer | National Provider Identifier (Primary Key, Foreign Key to Provider Demographics)                                                                                                                          |
| RNDRNG_PRVDR_MDCR_PRTCPTG_IND    | Text    | Medicare Participation Indicator                                                                                                                                                                          |
| TOT_HCPCS_CDS                    | Integer | Number of unique HCPCS codes                                                                                                                                                                              |
| TOT_BENES                        | Integer | Total beneficiaries receiving services from the provider                                                                                                                                                  |
| TOT_SRVCS                        | Number  | Total provider services                                                                                                                                                                                   |
| TOT_SBMTD_CHRG                   | Number  | Total charges submitted for all services                                                                                                                                                                  |
| TOT_MDCR_ALOWD_AMT               | Number  | Medicare allowed amount for all services                                                                                                                                                                  |
| TOT_MDCR_PYMT_AMT                | Number  | Amount paid by Medicare after deductible and coinsurance amounts deducted                                                                                                                                 |
| TOT_MDCR_STDZD_AMT               | Number  | Total amount that Medicare paid after deductible and coinsurance amounts deducted and after standardization of the Medicare payment has been applied.                                                     |
| DRUG_SPRSN_IND                   | Text    | Identifies whether the utilization, cost and payment information associated with HCPCS codes for drug services as listed on the Medicare Part B Drug Average Sales Price (ASP) list have been suppressed. |
| DRUG_TOT_HCPCS_CDS               | Integer | Number of HCPCS Associated With Drug Services                                                                                                                                                             |
| DRUG_TOT_BENES                   | Integer | Number of Medicare Beneficiaries With Drug Services                                                                                                                                                       |
| DRUG_TOT_SRVCS                   | Number  | Number of Drug Services                                                                                                                                                                                   |
| DRUG_SBMTD_CHRG                  | Number  | Total Drug Submitted Charge Amount                                                                                                                                                                        |
| DRUG_MDCR_ALOWD_AMT              | Number  | Total Drug Medicare Allowed Amount                                                                                                                                                                        |
| DRUG_MDCR_PYMT_AMT               | Number  | Total Drug Medicare Payment Amount                                                                                                                                                                        |
| DRUG_MDCR_STDZD_AMT              | Number  | Total Drug Medicare Standardized Payment Amount                                                                                                                                                           |
| MED_SPRSN_IND                    | Text    | Identifies whether the utilization, cost and payment information associated with HCPCS codes for Medical (non-ASP) services have been suppressed                                                          |
| MED_TOT_HCPCS_CDS                | Integer | Number of HCPCS Associated With Medical Services                                                                                                                                                          |
| MED_TOT_BENES                    | Integer | Number of Medicare Beneficiaries with Medical Services                                                                                                                                                    |
| MED_TOT_SRVCS                    | Number  | Number of Medical Services                                                                                                                                                                                |
| MED_SBMTD_CHRG                   | Number  | Total Medical Submitted Charge Amount                                                                                                                                                                     |
| MED_MDCR_ALOWD_AMT               | Number  | Total Medical Medicare Allowed Amount                                                                                                                                                                     |
| MED_MDCR_PYMT_AMT                | Number  | Total Medical Medicare Payment Amount                                                                                                                                                                     |
| MED_MDCR_STDZD_AMT               | Number  | Total Medical Medicare Standardized Payment Amount                                                                                                                                                        |
| BENE_AVG_AGE                     | Integer | Average Age of Beneficiaries                                                                                                                                                                              |
| BENE_AGE_LT_65_CNT               | Integer | Number of Beneficiaries Age Less Than 65                                                                                                                                                                  |
| BENE_AGE_65_74_CNT               | Integer | Number of Beneficiaries Age 65 to 74                                                                                                                                                                      |
| BENE_AGE_75_84_CNT               | Integer | Number of Beneficiaries Age 75 to 84                                                                                                                                                                      |
| BENE_AGE_GT_85_CNT               | Integer | Number of Beneficiaries Age Greater Than 84                                                                                                                                                               |
| BENE_FEML_CNT                    | Integer | Number of Female Beneficiaries                                                                                                                                                                            |
| BENE_MALE_CNT                    | Integer | Number of Male Beneficiaries                                                                                                                                                                              |
| BENE_RACE_WHT_CNT                | Integer | Number of Non-Hispanic White Beneficia                                                                                                                                                                    |
| BENE_RACE_BLACK_CNT              | Integer | Number of Black or African American Beneficiaries                                                                                                                                                         |
| BENE_RACE_API_CNT                | Integer | Number of Asian Pacific Islander Beneficiaries                                                                                                                                                            |
| BENE_RACE_HSPNC_CNT              | Integer | Number of Hispanic Beneficiaries                                                                                                                                                                          |
| BENE_RACE_NATIND_CNT             | Integer | Number of American Indian/Alaska Native Beneficiaries                                                                                                                                                     |
| BENE_RACE_OTHR_CNT               | Integer | Number of Beneficiaries With Race Not Elsewhere Classified                                                                                                                                                |
| BENE_DUAL_CNT                    | Integer | Number of Beneficiaries With Medicare & Medicaid Entitlement                                                                                                                                              |
| BENE_NDUAL_CNT                   | Integer | Number of Beneficiaries With Medicare Only Entitlement                                                                                                                                                    |
| BENE_AVG_RISK_SCRE               | Number  | Average HCC Risk Score of Beneficiaries                                                                                                                                                                   |
| BENE_CC_BH_ADHD_OTHCD_V1_PCT     | Float   | Percent (%) Of Beneficiaries Identified With ADHD and Other Conduct Disorders                                                                                                                             |
| BENE_CC_BH_ALCOHOL_DRUG_V1_PCT   | Float   | Percent (%) Of Beneficiaries Identified With Alcohol and Drug Use Disorders                                                                                                                               |
| BENE_CC_BH_TOBACCO_V1_PCT        | Float   | Percent (%) Of Beneficiaries Identified With Tobacco Use Disorders                                                                                                                                        |
| BENE_CC_BH_ALZ_NONALZDEM_V2_PCT  | Float   | Percent (%) Of Beneficiaries Identified With Alzheimer's Disease and Non-Alzheimer's Dementia                                                                                                             |
| BENE_CC_BH_ANXIETY_V1_PCT        | Float   | Percent (%) Of Beneficiaries Identified With Anxiety Disorders                                                                                                                                            |
| BENE_CC_BH_BIPOLAR_V1_PCT        | Float   | Percent (%) Of Beneficiaries Identified With Bipolar Disorder                                                                                                                                             |
| BENE_CC_BH_MOOD_V2_PCT           | Float   | Percent (%) Of Beneficiaries Identified With Depression, Bipolar, Or Other Depressive Mood Disorders                                                                                                      |
| BENE_CC_BH_DEPRESS_V1_PCT        | Float   | Percent (%) Of Beneficiaries Identified With Major Depressive Affective Disorder                                                                                                                          |
| BENE_CC_BH_PD_V1_PCT             | Float   | Percent (%) Of Beneficiaries Identified With Personality Disorders                                                                                                                                        |
| BENE_CC_BH_PTSD_V1_PCT           | Float   | Percent (%) Of Beneficiaries Identified With Post-Traumatic Stress Disorder                                                                                                                               |
| BENE_CC_BH_SCHIZO_OTHPSY_V1_PCT  | Float   | Percent (%) Of Beneficiaries Identified With Schizophrenia and Other Psychotic Disorders                                                                                                                  |
| BENE_CC_PH_ASTHMA_V2_PCT         | Float   | Percent (%) Of Beneficiaries Identified With Asthma                                                                                                                                                       |
| BENE_CC_PH_AFIB_V2_PCT           | Float   | Percent (%) Of Beneficiaries Identified With Atrial Fibrillation and Flutter                                                                                                                              |
| BENE_CC_PH_CANCER6_V2_PCT        | Float   | Percent (%) Of Beneficiaries Identified With Combined Cancer Flag for 6 Cancer Indicators                                                                                                                 |
| BENE_CC_PH_CKD_V2_PCT            | Float   | Percent (%) Of Beneficiaries Identified With Chronic Kidney Disease                                                                                                                                       |
| BENE_CC_PH_COPD_V2_PCT           | Float   | Percent (%) Of Beneficiaries Identified With Chronic Obstructive Pulmonary Disease                                                                                                                        |
| BENE_CC_PH_DIABETES_V2_PCT       | Float   | Percent (%) Of Beneficiaries Identified With Diabetes                                                                                                                                                     |
| BENE_CC_PH_HF_NONIHD_V2_PCT      | Float   | Percent (%) Of Beneficiaries Identified With Heart Failure And Non-Ischemic Heart Disease                                                                                                                 |
| BENE_CC_PH_HYPERLIPIDEMIA_V2_PCT | Float   | Percent (%) Of Beneficiaries Identified With Hyperlipidemia                                                                                                                                               |
| BENE_CC_PH_HYPERTENSION_V2_PCT   | Float   | Percent (%) Of Beneficiaries Identified With Hypertension                                                                                                                                                 |
| BENE_CC_PH_ISCHEMICHEART_V2_PCT  | Float   | Percent (%) Of Beneficiaries Identified With Ischemic Heart Disease                                                                                                                                       |
| BENE_CC_PH_OSTEOPOROSIS_V2_PCT   | Float   | Percent (%) Of Beneficiaries Identified With Osteoporosis                                                                                                                                                 |
| BENE_CC_PH_PARKINSON_V2_PCT      | Float   | Percent (%) Of Beneficiaries Identified With Parkinson's Disease And Secondary Parkinsonism                                                                                                               |
| BENE_CC_PH_ARTHRITIS_V2_PCT      | Float   | Percent (%) Of Beneficiaries Identified With Rheumatoid Arthritis / Osteoarthritis                                                                                                                        |
| BENE_CC_PH_STROKE_TIA_V2_PCT     | Float   | Percent (%) Of Beneficiaries Identified With Stroke / Transient Ischemic Attack                                                                                                                           |

### HOSPITAL_GENERAL_INFORMATION

Hospital demographic information and group measure performance data.

| Column                                                | Type | Description                                           |
| ----------------------------------------------------- | ---- | ----------------------------------------------------- |
| FACILITY_ID                                           | Text | Facility ID (Primary Key)                             |
| FACILITY_NAME                                         | Text | Facility name                                         |
| ADDRESS                                               | Text | Street address                                        |
| CITY_TOWN                                             | Text | City                                                  |
| STATE                                                 | Text | State                                                 |
| ZIP_CODE                                              | Text | Zip Code, zero padded                                 |
| COUNTY_PARISH                                         | Text | County/Parish                                         |
| TELEPHONE_NUMBER                                      | Text | Telephone Number                                      |
| HOSPITAL_TYPE                                         | Text | Hospital Type                                         |
| HOSPITAL_OWNERSHIP                                    | Text | Hospital Ownership                                    |
| EMERGENCY_SERVICES                                    | Text | Emergency Services                                    |
| MEETS_CRITERIA_FOR_PROMOTING_INTEROPERABILITY_OF_EHRS | Text | Meets criteria for promoting interoperability of EHRs |
| MEETS_CRITERIA_FOR_BIRTHING_FRIENDLY_DESIGNATION      | Text | Meets criteria for birthing friendly designation      |
| HOSPITAL_OVERALL_RATING                               | Text | Overall Rating                                        |
| HOSPITAL_OVERALL_RATING_FOOTNOTE                      | Text | Footnote codes                                        |
| MORT_GROUP_MEASURE_COUNT                              | Text | Mortality Group Measure Coun                          |
| COUNT_OF_FACILITY_MORT_MEASURES                       | Text | Count of Facility Mortality Measures                  |
| COUNT_OF_MORT_MEASURES_BETTER                         | Text | Count of Facility Mortality Measures Better           |
| COUNT_OF_MORT_MEASURES_NO_DIFFERENT                   | Text | Count of Facility Mortality Measures No Different     |
| COUNT_OF_MORT_MEASURES_WORSE                          | Text | Count of Facility Mortality Measures Worse            |
| MORT_GROUP_FOOTNOTE                                   | Text | Mortality Group Footnote                              |
| SAFETY_GROUP_MEASURE_COUNT                            | Text | Safety Group Measure Count                            |
| COUNT_OF_FACILITY_SAFETY_MEASURES                     | Text | Count of Facility Safety Measures                     |
| COUNT_OF_SAFETY_MEASURES_BETTER                       | Text | Count of Facility Safety Measures Better              |
| COUNT_OF_SAFETY_MEASURES_NO_DIFFERENT                 | Text | Count of Facility Safety Measures No Different        |
| COUNT_OF_SAFETY_MEASURES_WORSE                        | Text | Count of Facility Safety Measures Worse               |
| SAFETY_GROUP_FOOTNOTE                                 | Text | Safety Group Footnote                                 |
| READM_GROUP_MEASURE_COUNT                             | Text | Readmission Group Measure Count                       |
| COUNT_OF_FACILITY_READM_MEASURES                      | Text | Count of Facility Readmission Measures                |
| COUNT_OF_READM_MEASURES_BETTER                        | Text | Count of Facility Readmission Measures Better         |
| COUNT_OF_READM_MEASURES_NO_DIFFERENT                  | Text | Count of Facility Readmission Measures No Different   |
| COUNT_OF_READM_MEASURES_WORSE                         | Text | Count of Facility Readmission Measures Worse          |
| READM_GROUP_FOOTNOTE                                  | Text | Readmission Group Footnote                            |
| PT_EXP_GROUP_MEASURE_COUNT                            | Text | Patient Experience Group Measure Count                |
| COUNT_OF_FACILITY_PT_EXP_MEASURES                     | Text | Count of Facility Patient Experience Measures         |
| PT_EXP_GROUP_FOOTNOTE                                 | Text | Patient Experience Group Footnote                     |
| TE_GROUP_MEASURE_COUNT                                | Text | Timely and Efficient Care Group Measure Count         |
| COUNT_OF_FACILITY_TE_MEASURES                         | Text | Count of Facility Timely and Efficient Care Measures  |
| TE_GROUP_FOOTNOTE                                     | Text | Timely and Efficient Care Group Footnote              |

### PROVIDER_HOSPITAL_AFFILIATION

Provides the link between provider-hospital tables.

| Column                                     | Type   | Description                                              |
| ------------------------------------------ | ------ | -------------------------------------------------------- |
| NPI                                        | Number | Primary Key, Foreign Key to PROVIDER_DEMOGRAPHICS        |
| FACILITY_AFFILIATIONS_CERTIFICATION_NUMBER | Text   | Primary Key, Foreign Key to HOSPITAL_GENERAL_INFORMATION |

### MIPS_PERFORMANCE

Publicly reported final scores and performance category scores for clinicans that participate in the Merit-based Incentive Payment System (MIPS). A null value in any performance category indicates it did not contribute to the final score.

| Column                                      | Type   | Description                                                                      |
| ------------------------------------------- | ------ | -------------------------------------------------------------------------------- |
| NPI                                         | Number | National provider identifier (Primary Key, Foreign Key to PROVIDER_DEMOGRAPHICS) |
| ORG_PAC_ID                                  | Text   | PECOS Group ID of the group this person participated in (Primary Key)            |
| PROVIDER_LAST_NAME                          | Text   | Last Name                                                                        |
| PROVIDER_FIRST_NAME                         | Text   | First Name                                                                       |
| SOURCE                                      | Text   | Method by which the clinician was scored                                         |
| FACILITY_BASED_SCORING_CERTIFICATION_NUMBER | Float  | All null, no facility based clinicians in 2023                                   |
| FACILITY_NAME                               | Float  | All null, no facility based clinicians in 2023                                   |
| QUALITY_CATEGORY_SCORE                      | Float  | Quality performance category score                                               |
| PI_CATEGORY_SCORE                           | Float  | Promoting Interoperability performance category score                            |
| IA_CATEGORY_SCORE                           | Float  | Improvement Activities performance category score                                |
| COST_CATEGORY_SCORE                         | Float  | Cost performance category score                                                  |
| FINAL_MIPS_SCORE_WITHOUT_CPB                | Float  | MIPS Final Score without the Complex Patient Bonus (CPB)                         |
| FINAL_MIPS_SCORE                            | Float  | MIPS Final Score with the CPB                                                    |

### MIPS_METRICS

Individual measure-level detail for MIPS quality reporting.

| Column              | Type   | Description                                                                                                                      |
| ------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------- |
| NPI                 | Number | National Provider Identifier (Primary Key, Foreign Key to PROVIDER_DEMOGRAPHICS)                                                 |
| IND_PAC_ID          | Text   | Individual PECOS Associate Control ID                                                                                            |
| PROVIDER_LAST_NAME  | Text   | Last Name                                                                                                                        |
| PROVIDER_FIRST_NAME | Text   | First Name                                                                                                                       |
| APM_AFFL_1          | Text   | Alternative Payment Model affiliation 1                                                                                          |
| APM_AFFL_2          | Text   | APM affiliation 2                                                                                                                |
| APM_AFFL_3          | Text   | APM affiliation 3                                                                                                                |
| APM_AFFL_4          | Float  | APM affiliation 4, all null in PY2023                                                                                            |
| MEASURE_CD          | Text   | Measure code (PK)                                                                                                                |
| MEASURE_TITLE       | Text   | Measure description                                                                                                              |
| INVS_MSR            | Text   | Inverse measure indicator (Y/N)                                                                                                  |
| ATTESTATION_VALUE   | Text   | Attestation response for yes/no measure                                                                                          |
| PRF_RATE            | Float  | Performance rate                                                                                                                 |
| PATIENT_COUNT       | Float  | Number of patients included in the measure denominator                                                                           |
| STAR_VALUE          | Float  | Star rating assigned based on performance at the measure, stratum, collection type, and entity type level                        |
| FIVE_STAR_BENCHMARK | Float  | The established ABC™ benchmark used to assign a five-star rating for a given measure and collection type                         |
| COLLECTION_TYPE     | Text   | ATT: Web Attestation, CLM: Claims, EHR: Electronic Health Record, QCDR: Qualified Clinical Data Registry, REG Qualified Registry |
| CCXP_IND            | Text   | Complex care experience indicator (Y/N)                                                                                          |

### HOSPITAL_COMPLICATIONS_DEATHS

Complication and mortality measures by hospital.

| Column               | Type | Description                                                            |
| -------------------- | ---- | ---------------------------------------------------------------------- |
| FACILITY_ID          | Text | Facility ID (Primary Key, Foreign Key to HOSPITAL_GENERAL_INFORMATION) |
| FACILITY_NAME        | Text | Facility Name                                                          |
| ADDRESS              | Text | Address                                                                |
| CITY_TOWN            | Text | City / Town                                                            |
| STATE                | Text | State                                                                  |
| ZIP_CODE             | Text | 5-digit zip code                                                       |
| COUNTY_PARISH        | Text | County / Parish                                                        |
| TELEPHONE_NUMBER     | Text | Telephone Number                                                       |
| MEASURE_ID           | Text | Measure ID (Primary Key)                                               |
| MEASURE_NAME         | Text | Measure Name                                                           |
| COMPARED_TO_NATIONAL | Text | Performance vs national rate/value                                     |
| DENOMINATOR          | Text | Cases in the denominator                                               |
| SCORE                | Text | Measure score                                                          |
| LOWER_ESTIMATE       | Text | Lower estimate                                                         |
| HIGHER_ESTIMATE      | Text | Higher estimates                                                       |
| FOOTNOTE             | Text | Footnote codes, may be comma-separated                                 |
| START_DATE           | Text | Measurement period start                                               |
| END_DATE             | Text | Measurement period end                                                 |

### HOSPITAL_UNPLANNED_VISITS

Readmission and return visit measures by hospital. Same structure as HOSPITAL_COMPLICATIONS_DEATHS with two additional columns.

| Column                      | Type | Description                                                            |
| --------------------------- | ---- | ---------------------------------------------------------------------- |
| FACILITY_ID                 | Text | Facility ID (Primary Key, Foreign Key to HOSPITAL_GENERAL_INFORMATION) |
| FACILITY_NAME               | Text | Facility Name                                                          |
| ADDRESS                     | Text | Address                                                                |
| CITY_TOWN                   | Text | City / Town                                                            |
| STATE                       | Text | State                                                                  |
| ZIP_CODE                    | Text | 5-digit zip code                                                       |
| COUNTY_PARISH               | Text | County / Parish                                                        |
| TELEPHONE_NUMBER            | Text | Telephone Number                                                       |
| MEASURE_ID                  | Text | Measure ID (Primary Key)                                               |
| MEASURE_NAME                | Text | Measure Name                                                           |
| COMPARED_TO_NATIONAL        | Text | Performance vs national rate/value/expected                            |
| DENOMINATOR                 | Text | Cases in the denominator                                               |
| SCORE                       | Text | Measure score                                                          |
| LOWER_ESTIMATE              | Text | Lower estimate                                                         |
| HIGHER_ESTIMATE             | Text | Higher estimate                                                        |
| NUMBER_OF_PATIENTS          | Text | Total patients                                                         |
| NUMBER_OF_PATIENTS_RETURNED | Text | Patients who returned                                                  |
| FOOTNOTE                    | Text | Footnote codes, may be comma-separated                                 |
| START_DATE                  | Text | Measurement period start                                               |
| END_DATE                    | Text | Measurement period end                                                 |

### HOSPITAL_HAI

Healthcare-associated infection measures by hospital.

| Column               | Type | Description                                                            |
| -------------------- | ---- | ---------------------------------------------------------------------- |
| FACILITY_ID          | Text | Facility ID (Primary Key, Foreign Key to HOSPITAL_GENERAL_INFORMATION) |
| FACILITY_NAME        | Text | Facility Name                                                          |
| ADDRESS              | Text | Address                                                                |
| CITY_TOWN            | Text | City / Town                                                            |
| STATE                | Text | State                                                                  |
| ZIP_CODE             | Text | 5-digit zip code                                                       |
| COUNTY_PARISH        | Text | County / Parish                                                        |
| TELEPHONE_NUMBER     | Text | Telephone Number                                                       |
| MEASURE_ID           | Text | Measure ID (Primary Key)                                               |
| MEASURE_NAME         | Text | Measure Name                                                           |
| COMPARED_TO_NATIONAL | Text | Performance vs national rate/value/expected                            |
| SCORE                | Text | Measure Score                                                          |
| FOOTNOTE             | Text | Footnote codes, may be comma-separated                                 |
| START_DATE           | Text | Measurement period start                                               |
| END_DATE             | Text | Measurement period end                                                 |

### HOSPITAL_HCAHPS

Hospital Consumer Assessment of Healthcare Providers and Systems survey results.

| Column                                | Type | Description                                                            |
| ------------------------------------- | ---- | ---------------------------------------------------------------------- |
| FACILITY_ID                           | Text | Facility ID (Primary Key, Foreign Key to HOSPITAL_GENERAL_INFORMATION) |
| FACILITY_NAME                         | Text | Facility Name                                                          |
| ADDRESS                               | Text | Address                                                                |
| CITY_TOWN                             | Text | City / Town                                                            |
| STATE                                 | Text | State                                                                  |
| ZIP_CODE                              | Text | 5-digit zip code                                                       |
| COUNTY_PARISH                         | Text | County / Parish                                                        |
| TELEPHONE_NUMBER                      | Text | Telephone Number                                                       |
| HCAHPS_MEASURE_ID                     | Text | Measure ID (Primary Key)                                               |
| HCAHPS_QUESTION                       | Text | Survey question or measure category                                    |
| HCAHPS_ANSWER_DESCRIPTION             | Text | Response label                                                         |
| PATIENT_SURVEY_STAR_RATING            | Text | 1-5 star rating, "Not Applicable" for non-star rows                    |
| PATIENT_SURVEY_STAR_RATING_FOOTNOTE   | Text | Star Rating Footnote                                                   |
| HCAHPS_ANSWER_PERCENT                 | Text | Response percentage, "Not Applicable" for star/linear rows             |
| HCAHPS_ANSWER_PERCENT_FOOTNOTE        | Text | Answer Percent Footnote                                                |
| HCAHPS_LINEAR_MEAN_VALUE              | Text | Linear mean score for the measure domain                               |
| NUMBER_OF_COMPLETED_SURVEYS           | Text | Completed surveys for this facility                                    |
| NUMBER_OF_COMPLETED_SURVEYS_FOOTNOTE  | Text | Number of Completed Surveys Footnote                                   |
| SURVEY_RESPONSE_RATE_PERCENT          | Text | Survey response rate                                                   |
| SURVEY_RESPONSE_RATE_PERCENT_FOOTNOTE | Text | Survey response rate footnote                                          |
| START_DATE                            | Text | Measurement period start                                               |
| END_DATE                              | Text | Measurement period end                                                 |

### RUCA_ZIP_CODES

Rural-Urban Commuting Area (RUCA) codes by zip code. Published by the USDA, RUCA codes classify areas by urbanization, population density, and commuting patterns.

| Column      | Type    | Description |
| ----------- | ------- | ----------- |
| ZIPCODE     | Text    | PK          |
| PRIMARYRUCA | Integer | RUCA Code   |

## Views

### PROVIDER_PROFILE_VIEW

One row per individual provider. Combines demographics with best individual MIPS score.

| Column                    | Source                                           | Description                                            |
| ------------------------- | ------------------------------------------------ | ------------------------------------------------------ |
| NPI                       | PROVIDER_DEMOGRAPHICS RNDRNG_NPI                 | National Provider Identifier                           |
| LAST_NAME                 | PROVIDER_DEMOGRAPHICS RNDRNG_PRVDR_LAST_ORG_NAME | Last Name                                              |
| FIRST_NAME                | PROVIDER_DEMOGRAPHICS RNDRNG_PRVDR_FIRST_NAME    | First Name                                             |
| CREDENTIALS               | PROVIDER_DEMOGRAPHICS RNDRNG_PRVDR_CRDNTLS       | Credentials, free text, raw                            |
| PROVIDER_TYPE             | PROVIDER_DEMOGRAPHICS RNDRNG_PRVDR_TYPE          | Provider type: mixed medical specialty and role values |
| ADDRESS                   | PROVIDER_DEMOGRAPHICS RNDRNG_PRVDR_ST1           | Address                                                |
| CITY                      | PROVIDER_DEMOGRAPHICS RNDRNG_PRVDR_CITY          | City                                                   |
| STATE                     | PROVIDER_DEMOGRAPHICS RNDRNG_PRVDR_STATE_ABRVTN  | State                                                  |
| ZIP_CODE                  | PROVIDER_DEMOGRAPHICS RNDRNG_PRVDR_ZIP5          | 5-digit zip code                                       |
| RUCA                      | PROVIDER_DEMOGRAPHICS RNDRNG_PRVDR_RUCA          | Rural-Urban Commuting Area Code                        |
| RUCA_DESC                 | PROVIDER_DEMOGRAPHICS RNDRNG_PRVDR_RUCA_DESC     | Rural-Urban Commuting Area Description                 |
| MAX_INDIVIDUAL_MIPS_SCORE | MIPS_PERFORMANCE SOURCE = "Individual"           | MAX(FINAL_MIPS_SCORE) per NPI                          |

### HOSPITAL_QUALITY_SUMMARY_VIEW

One row per facility-measure. Combines data from HOSPITAL_COMPLICATIONS_DEATHS, HOSPITAL_HAI, and HOSPITAL_UNPLANNED_VISITS into a single view. HAI filtered to SIR summary measures only.

| Column                        | Source        | Description                                                                            |
| ----------------------------- | ------------- | -------------------------------------------------------------------------------------- |
| FACILITY_ID                   | Source tables | Facility ID                                                                            |
| SOURCE                        | Derived       | Table of origin: "HAI", "Complications Deaths", or "Unplanned Visits"                  |
| MEASURE_ID                    | Source tables | Measure ID                                                                             |
| MEASURE_NAME                  | Source tables | Measure Name                                                                           |
| COMPARED_TO_NATIONAL          | Source tables | Original CMS comparison text                                                           |
| SCORE                         | Source tables | Measure Score                                                                          |
| COMPARED_TO_NATIONAL_CATEGORY | Derived       | Standardized to: Better, Worse, No Different, Not Available, Number of Cases Too Small |

### HCAHPS_SUMMARY_VIEW

One row per facility per star rating domain. Contains star ratings and survey response rates.

| Column                       | Source          | Description                    |
| ---------------------------- | --------------- | ------------------------------ |
| FACILITY_ID                  | HOSPITAL_HCAHPS | Facility ID                    |
| HCAHPS_MEASURE_ID            | HOSPITAL_HCAHPS | Measure ID                     |
| HCAHPS_QUESTION              | HOSPITAL_HCAHPS | Measure Question / Description |
| PATIENT_SURVEY_STAR_RATING   | HOSPITAL_HCAHPS | Patient Star Rating            |
| NUMBER_OF_COMPLETED_SURVEYS  | HOSPITAL_HCAHPS | Number of Completed Surveys    |
| SURVEY_RESPONSE_RATE_PERCENT | HOSPITAL_HCAHPS | Survey Response Rate Percent   |

### HCAHPS_DETAILED_VIEW

One row per facility per survey question and answer option. Contains response percentages for each answer choice.

| Column                    | Source          | Description                                        |
| ------------------------- | --------------- | -------------------------------------------------- |
| FACILITY_ID               | HOSPITAL_HCAHPS | Facility ID                                        |
| HCAHPS_MEASURE_ID         | HOSPITAL_HCAHPS | Measure ID                                         |
| HCAHPS_QUESTION           | HOSPITAL_HCAHPS | Measure Question / Rating (Always/sometimes/never) |
| HCAHPS_ANSWER_DESCRIPTION | HOSPITAL_HCAHPS | Answer Description                                 |
| HCAHPS_ANSWER_PERCENT     | HOSPITAL_HCAHPS | Answer percent                                     |
