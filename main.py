import logging
from transforms.utils import create_snowflake_connection, df_to_snowflake
from transforms.affiliation_data import transform_affiliation_data
from transforms.hcahps_data import transform_hcahps_data
from transforms.hospital_data import transform_hospital_data
from transforms.hospital_quality_data import transform_hospital_quality_data
from transforms.mips_data import transform_mips_data
from transforms.provider_data import transform_provider_data

PROVIDER_SERVICE_DATA = 'data/MUP_PHY_R25_P05_V20_D23_Prov_Svc.csv'
HOSPITAL_GENERAL_INFORMATION = 'data/Hospital_General_Information.csv'
FACILITY_AFFILIATION_DATA = 'data/Facility_Affiliation.csv'
MIPS_PERFORMANCE_DATA = 'data/ec_score_file.csv'
MIPS_METRICS_DATA = 'data/ec_public_reporting.csv'
UNPLANNED_VISIT_DATA = 'data/Unplanned_Hospital_Visits-Hospital.csv'
HAI_DATA = 'data/Healthcare_Associated_Infections_Hospital.csv'
HCAHPS_DATA = 'data/HCAHPS-Hospital.csv'
HOSPITAL_COMPLICATIONS_DATA = 'data/Complications_and_Deaths-Hospital.csv'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

snow_conn = create_snowflake_connection()

try:
    logger.info('Starting file processing.')

    demographics_df, services_df = transform_provider_data(PROVIDER_SERVICE_DATA)
    df_to_snowflake(snow_conn, demographics_df, 'PROVIDER_DEMOGRAPHICS')
    df_to_snowflake(snow_conn, services_df, 'PROVIDER_SERVICES')
    logger.info(
        'Provider demographics and service data uploaded to Snowflake. (Tables 1 & 2/10)'
    )

    hospital_info_df = transform_hospital_data(HOSPITAL_GENERAL_INFORMATION)
    df_to_snowflake(snow_conn, hospital_info_df, 'HOSPITAL_GENERAL_INFORMATION')
    logger.info('Hospital General Information uploaded to Snowflake. (Table 3/10)')

    affiliation_df = transform_affiliation_data(FACILITY_AFFILIATION_DATA)
    df_to_snowflake(snow_conn, affiliation_df, 'PROVIDER_HOSPITAL_AFFILIATION')
    logger.info(
        'Provider facility affiliation data uploaded to Snowflake. (Table 4/10)'
    )

    mips_performance_df = transform_mips_data(MIPS_PERFORMANCE_DATA)
    df_to_snowflake(snow_conn, mips_performance_df, 'MIPS_PERFORMANCE')
    logger.info('MIPS performance data uploaded to Snowflake. (Table 5/10)')

    mips_metrics_df = transform_mips_data(MIPS_METRICS_DATA)
    df_to_snowflake(snow_conn, mips_metrics_df, 'MIPS_METRICS')
    logger.info('MIPS scores data uploaded to Snowflake. (Table 6/10)')

    hcahps_df = transform_hcahps_data(HCAHPS_DATA)
    df_to_snowflake(snow_conn, hcahps_df, 'HOSPITAL_HCAHPS')
    logger.info('Hospital HCAHPS data uploaded to Snowflake. (Table 7/10)')

    hai_df = transform_hospital_quality_data(HAI_DATA)
    df_to_snowflake(snow_conn, hai_df, 'HOSPITAL_HAI')
    logger.info('Hospital HAI data uploaded to Snowflake. (Table 8/10)')

    unplanned_visit_df = transform_hospital_quality_data(UNPLANNED_VISIT_DATA)
    df_to_snowflake(snow_conn, unplanned_visit_df, 'HOSPITAL_UNPLANNED_VISITS')
    logger.info('Hospital unplanned visit data uploaded to Snowflake. (Table 9/10)')

    complications_df = transform_hospital_quality_data(HOSPITAL_COMPLICATIONS_DATA)
    df_to_snowflake(snow_conn, complications_df, 'HOSPITAL_COMPLICATIONS_DEATHS')
    logger.info('Hospital complications data uploaded to Snowflake. (Table 10/10)')

except Exception as e:
    logger.error(f'Error: {e}')

finally:
    snow_conn.close()
