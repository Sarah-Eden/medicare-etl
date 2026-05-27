import logging
from transforms.utils import create_snowflake_connection, df_to_snowflake
from transforms.transforms import transform_data

PROVIDER_SERVICE_DATA = 'data/MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv'
HOSPITAL_GENERAL_INFORMATION = 'data/Hospital_General_Information.csv'
FACILITY_AFFILIATION_DATA = 'data/Facility_Affiliation.csv'
MIPS_PERFORMANCE_DATA = 'data/ec_score_file.csv'
MIPS_METRICS_DATA = 'data/ec_public_reporting.csv'
UNPLANNED_VISIT_DATA = 'data/Unplanned_Hospital_Visits-Hospital.csv'
HAI_DATA = 'data/Healthcare_Associated_Infections_Hospital.csv'
HCAHPS_DATA = 'data/HCAHPS-Hospital.csv'
HOSPITAL_COMPLICATIONS_DATA = 'data/Complications_and_Deaths-Hospital.csv'

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

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

snow_conn = create_snowflake_connection()

try:
    logger.info('Starting file processing.')

    demographics_df, services_df = transform_data(
        PROVIDER_SERVICE_DATA,
        specify_dtype={'Rndrng_Prvdr_Zip5': str, 'Rndrng_Prvdr_State_FIPS': str},
        split_data=PROVIDER_DEMOGRAPHICS_SERVICES_COLUMN_SPLIT,
    )

    demographics_df.drop_duplicates(inplace=True)
    if demographics_df.shape[0] != services_df['RNDRNG_NPI'].nunique():
        raise ValueError('Duplicate NPIs in demographics after duplicates dropped.')

    df_to_snowflake(snow_conn, demographics_df, 'PROVIDER_DEMOGRAPHICS')
    df_to_snowflake(snow_conn, services_df, 'PROVIDER_SERVICES')
    logger.info(
        'Provider demographics and service data uploaded to Snowflake. (Tables 1 & 2/10)'
    )

    hospital_info_df = transform_data(
        HOSPITAL_GENERAL_INFORMATION,
        specify_dtype={'ZIP Code': str, 'Hospital overall rating footnote': str},
    )
    df_to_snowflake(snow_conn, hospital_info_df, 'HOSPITAL_GENERAL_INFORMATION')
    logger.info('Hospital General Information uploaded to Snowflake. (Table 3/10)')

    affiliation_df = transform_data(
        FACILITY_AFFILIATION_DATA,
        filter_rows={'facility_type': 'Hospital'},
        keep_columns=['NPI', 'Facility Affiliations Certification Number'],
        drop_duplicates=True,
    )
    df_to_snowflake(snow_conn, affiliation_df, 'PROVIDER_HOSPITAL_AFFILIATION')
    logger.info(
        'Provider facility affiliation data uploaded to Snowflake. (Table 4/10)'
    )

    mips_performance_df = transform_data(
        MIPS_PERFORMANCE_DATA, specify_dtype={'Org_PAC_ID': str}
    )
    df_to_snowflake(snow_conn, mips_performance_df, 'MIPS_PERFORMANCE')
    logger.info('MIPS performance data uploaded to Snowflake. (Table 5/10)')

    mips_metrics_df = transform_data(
        MIPS_METRICS_DATA, specify_dtype={'Ind_PAC_ID': str}
    )
    df_to_snowflake(snow_conn, mips_metrics_df, 'MIPS_METRICS')
    logger.info('MIPS scores data uploaded to Snowflake. (Table 6/10)')

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
    logger.info('Hospital HCAHPS data uploaded to Snowflake. (Table 7/10)')

    hai_df = transform_data(HAI_DATA, specify_dtype={'ZIP Code': str, 'Footnote': str})
    df_to_snowflake(snow_conn, hai_df, 'HOSPITAL_HAI')
    logger.info('Hospital HAI data uploaded to Snowflake. (Table 8/10)')

    unplanned_visit_df = transform_data(
        UNPLANNED_VISIT_DATA, specify_dtype={'ZIP Code': str, 'Footnote': str}
    )
    df_to_snowflake(snow_conn, unplanned_visit_df, 'HOSPITAL_UNPLANNED_VISITS')
    logger.info('Hospital unplanned visit data uploaded to Snowflake. (Table 9/10)')

    complications_df = transform_data(
        HOSPITAL_COMPLICATIONS_DATA, specify_dtype={'ZIP Code': str, 'Footnote': str}
    )
    df_to_snowflake(snow_conn, complications_df, 'HOSPITAL_COMPLICATIONS_DEATHS')
    logger.info('Hospital complications data uploaded to Snowflake. (Table 10/10)')

except Exception as e:
    logger.error(f'Error: {e}')

finally:
    snow_conn.close()
