import logging
from transforms.utils import create_snowflake_connection, df_to_snowflake
from transforms.transforms import transform_data
from create_views_constraints import run_scripts

PROVIDER_SERVICE_DATA = 'data/MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv'
HOSPITAL_GENERAL_INFORMATION = 'data/Hospital_General_Information.csv'
FACILITY_AFFILIATION_DATA = 'data/Facility_Affiliation.csv'
MIPS_PERFORMANCE_DATA = 'data/ec_score_file.csv'
MIPS_METRICS_DATA = 'data/ec_public_reporting.csv'
UNPLANNED_VISIT_DATA = 'data/Unplanned_Hospital_Visits-Hospital.csv'
HAI_DATA = 'data/Healthcare_Associated_Infections_Hospital.csv'
HCAHPS_DATA = 'data/HCAHPS-Hospital.csv'
HOSPITAL_COMPLICATIONS_DATA = 'data/Complications_and_Deaths-Hospital.csv'
RUCA_ZIP_CODES = 'data/RUCA-codes-2020-zipcode.csv'
PROVIDER_SUMMARY_DATA = (
    'data/Medicare_Physician_Other_Practitioners_by_Provider_2023.csv'
)

PROVIDER_DEMOGRAPHICS_SERVICES_COLUMN_SPLIT = [
    [
        'Rndrng_NPI',
        'Rndrng_Prvdr_Last_Org_Name',
        'Rndrng_Prvdr_First_Name',
        'Rndrng_Prvdr_MI',
        'Rndrng_Prvdr_Crdntls',
        'Rndrng_Prvdr_Ent_Cd',
        'Rndrng_Prvdr_St1',
        'Rndrng_Prvdr_St2',
        'Rndrng_Prvdr_City',
        'Rndrng_Prvdr_State_Abrvtn',
        'Rndrng_Prvdr_State_FIPS',
        'Rndrng_Prvdr_Zip5',
        'Rndrng_Prvdr_RUCA',
        'Rndrng_Prvdr_RUCA_Desc',
        'Rndrng_Prvdr_Cntry',
        'Rndrng_Prvdr_Type',
    ],
    [
        'Rndrng_NPI',
        'HCPCS_Cd',
        'HCPCS_Desc',
        'HCPCS_Drug_Ind',
        'Place_Of_Srvc',
        'Tot_Benes',
        'Tot_Bene_Day_Srvcs',
        'Rndrng_Prvdr_Mdcr_Prtcptg_Ind',
        'Avg_Sbmtd_Chrg',
        'Avg_Mdcr_Alowd_Amt',
        'Avg_Mdcr_Pymt_Amt',
        'Avg_Mdcr_Stdzd_Amt',
        'Tot_Srvcs',
    ],
]

PROVIDER_SUMMARY_KEEP_COLUMNS = [
    'Rndrng_NPI',
    'Rndrng_Prvdr_Mdcr_Prtcptg_Ind',
    'Tot_HCPCS_Cds',
    'Tot_Benes',
    'Tot_Srvcs',
    'Tot_Sbmtd_Chrg',
    'Tot_Mdcr_Alowd_Amt',
    'Tot_Mdcr_Pymt_Amt',
    'Tot_Mdcr_Stdzd_Amt',
    'Drug_Sprsn_Ind',
    'Drug_Tot_HCPCS_Cds',
    'Drug_Tot_Benes',
    'Drug_Tot_Srvcs',
    'Drug_Sbmtd_Chrg',
    'Drug_Mdcr_Alowd_Amt',
    'Drug_Mdcr_Pymt_Amt',
    'Drug_Mdcr_Stdzd_Amt',
    'Med_Sprsn_Ind',
    'Med_Tot_HCPCS_Cds',
    'Med_Tot_Benes',
    'Med_Tot_Srvcs',
    'Med_Sbmtd_Chrg',
    'Med_Mdcr_Alowd_Amt',
    'Med_Mdcr_Pymt_Amt',
    'Med_Mdcr_Stdzd_Amt',
    'Bene_Avg_Age',
    'Bene_Age_LT_65_Cnt',
    'Bene_Age_65_74_Cnt',
    'Bene_Age_75_84_Cnt',
    'Bene_Age_GT_84_Cnt',
    'Bene_Feml_Cnt',
    'Bene_Male_Cnt',
    'Bene_Race_Wht_Cnt',
    'Bene_Race_Black_Cnt',
    'Bene_Race_API_Cnt',
    'Bene_Race_Hspnc_Cnt',
    'Bene_Race_NatInd_Cnt',
    'Bene_Race_Othr_Cnt',
    'Bene_Dual_Cnt',
    'Bene_Ndual_Cnt',
    'Bene_Avg_Risk_Scre',
    'Bene_CC_BH_ADHD_OthCD_V1_Pct',
    'Bene_CC_BH_Alcohol_Drug_V1_Pct',
    'Bene_CC_BH_Tobacco_V1_Pct',
    'Bene_CC_BH_Alz_NonAlzdem_V2_Pct',
    'Bene_CC_BH_Anxiety_V1_Pct',
    'Bene_CC_BH_Bipolar_V1_Pct',
    'Bene_CC_BH_Mood_V2_Pct',
    'Bene_CC_BH_Depress_V1_Pct',
    'Bene_CC_BH_PD_V1_Pct',
    'Bene_CC_BH_PTSD_V1_Pct',
    'Bene_CC_BH_Schizo_OthPsy_V1_Pct',
    'Bene_CC_PH_Asthma_V2_Pct',
    'Bene_CC_PH_Afib_V2_Pct',
    'Bene_CC_PH_Cancer6_V2_Pct',
    'Bene_CC_PH_CKD_V2_Pct',
    'Bene_CC_PH_COPD_V2_Pct',
    'Bene_CC_PH_Diabetes_V2_Pct',
    'Bene_CC_PH_HF_NonIHD_V2_Pct',
    'Bene_CC_PH_Hyperlipidemia_V2_Pct',
    'Bene_CC_PH_Hypertension_V2_Pct',
    'Bene_CC_PH_IschemicHeart_V2_Pct',
    'Bene_CC_PH_Osteoporosis_V2_Pct',
    'Bene_CC_PH_Parkinson_V2_Pct',
    'Bene_CC_PH_Arthritis_V2_Pct',
    'Bene_CC_PH_Stroke_TIA_V2_Pct',
]


def main():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    logger.addHandler(stream_handler)

    snow_conn = None
    current_table = ""

    try:
        current_table = "Snowflake Connection"
        snow_conn = create_snowflake_connection()

        logger.info('Starting file processing.')

        current_table = 'Provider Services'
        demographics_df, services_df = transform_data(
            PROVIDER_SERVICE_DATA,
            specify_dtype={'Rndrng_Prvdr_Zip5': str, 'Rndrng_Prvdr_State_FIPS': str},
            split_data=PROVIDER_DEMOGRAPHICS_SERVICES_COLUMN_SPLIT,
        )

        demographics_df.drop_duplicates(inplace=True)
        if demographics_df.shape[0] != demographics_df['RNDRNG_NPI'].nunique():
            raise ValueError('Duplicate NPIs in demographics after duplicates dropped.')

        df_to_snowflake(snow_conn, demographics_df, 'PROVIDER_DEMOGRAPHICS')
        df_to_snowflake(snow_conn, services_df, 'PROVIDER_SERVICES')
        logger.info(
            'Provider demographics and service data uploaded to Snowflake. (Tables 1 & 2/12)'
        )

        current_table = 'Hospital General Information'
        hospital_info_df = transform_data(
            HOSPITAL_GENERAL_INFORMATION,
            specify_dtype={'ZIP Code': str, 'Hospital overall rating footnote': str},
        )
        df_to_snowflake(snow_conn, hospital_info_df, 'HOSPITAL_GENERAL_INFORMATION')
        logger.info('Hospital General Information uploaded to Snowflake. (Table 3/12)')

        current_table = 'Provider Hospital Affiliation'
        affiliation_df = transform_data(
            FACILITY_AFFILIATION_DATA,
            filter_rows={'facility_type': 'Hospital'},
            keep_columns=['NPI', 'Facility Affiliations Certification Number'],
            drop_duplicates=True,
        )
        df_to_snowflake(snow_conn, affiliation_df, 'PROVIDER_HOSPITAL_AFFILIATION')
        logger.info(
            'Provider facility affiliation data uploaded to Snowflake. (Table 4/12)'
        )

        current_table = 'MIPS Performance'
        mips_performance_df = transform_data(
            MIPS_PERFORMANCE_DATA, specify_dtype={'Org_PAC_ID': str}
        )
        df_to_snowflake(snow_conn, mips_performance_df, 'MIPS_PERFORMANCE')
        logger.info('MIPS performance data uploaded to Snowflake. (Table 5/12)')

        current_table = 'MIPS Metrics'
        mips_metrics_df = transform_data(
            MIPS_METRICS_DATA, specify_dtype={'Ind_PAC_ID': str}
        )

        df_to_snowflake(snow_conn, mips_metrics_df, 'MIPS_METRICS')
        logger.info('MIPS scores data uploaded to Snowflake. (Table 6/12)')

        current_table = 'Hospital HCAHPS'
        hcahps_df = transform_data(
            HCAHPS_DATA,
            specify_dtype={
                'ZIP Code': str,
                'Patient Survey Star Rating Footnote': str,
                'HCAHPS Answer Percent Footnote': str,
                'Number of Completed Surveys Footnote': str,
                'Survey Response Rate Percent Footnote': str,
            },
        )
        df_to_snowflake(snow_conn, hcahps_df, 'HOSPITAL_HCAHPS')
        logger.info('Hospital HCAHPS data uploaded to Snowflake. (Table 7/12)')

        current_table = 'Hospital HAI'
        hai_df = transform_data(
            HAI_DATA, specify_dtype={'ZIP Code': str, 'Footnote': str}
        )
        df_to_snowflake(snow_conn, hai_df, 'HOSPITAL_HAI')
        logger.info('Hospital HAI data uploaded to Snowflake. (Table 8/12)')

        current_table = 'Hospital Unplanned Visits'
        unplanned_visit_df = transform_data(
            UNPLANNED_VISIT_DATA, specify_dtype={'ZIP Code': str, 'Footnote': str}
        )
        df_to_snowflake(snow_conn, unplanned_visit_df, 'HOSPITAL_UNPLANNED_VISITS')
        logger.info('Hospital unplanned visit data uploaded to Snowflake. (Table 9/12)')

        current_table = 'Hospital Complications & Deaths'
        complications_df = transform_data(
            HOSPITAL_COMPLICATIONS_DATA,
            specify_dtype={'ZIP Code': str, 'Footnote': str},
        )
        df_to_snowflake(snow_conn, complications_df, 'HOSPITAL_COMPLICATIONS_DEATHS')
        logger.info('Hospital complications data uploaded to Snowflake. (Table 10/12)')

        current_table = "RUCA ZIP Codes"
        ruca_df = transform_data(
            RUCA_ZIP_CODES,
            specify_dtype={'ZIPCode': str},
            keep_columns=['ZIPCode', 'PrimaryRUCA'],
            drop_duplicates=True,
        )
        df_to_snowflake(snow_conn, ruca_df, 'RUCA_ZIP_CODES')
        logger.info('RUCA - ZIP Code data uploaded to Snowflake. (Table 11/12)')

        current_table = 'Provider Summary'
        provider_summary_df = transform_data(
            PROVIDER_SUMMARY_DATA,
            specify_dtype={'Rndrng_NPI': str},
            keep_columns=PROVIDER_SUMMARY_KEEP_COLUMNS,
        )
        df_to_snowflake(snow_conn, provider_summary_df, 'PROVIDER_SUMMARY')
        logger.info('Provider summary data uploaded to Snowflake. (Table 12/12)')

        current_table = "Run Scripts"
        run_scripts(snow_conn, logger)

    except Exception as e:
        logger.error(f'Table: {current_table}, Error: {e}')
        raise

    finally:
        if snow_conn:
            snow_conn.close()


if __name__ == '__main__':
    main()
