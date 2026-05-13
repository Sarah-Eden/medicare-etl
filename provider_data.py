import pandas as pd
import numpy as np
from utils import load_data, standardize_zipcode

DEMOGRAPHICS_COLUMNS = [
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
]

SERVICES_COLUMNS = [
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
]


def create_demographics_table(df):
    """Creates a new DataFrame for provider demographic data.

    Copies columns in DEMOGRAPHICS_COLUMNS to new DataFrame, converts zipcode and FIPS
    columns to strings and pads with zeroes for consistency. Standardizes column names
    to uppercase with underscores and reduces data to one row per NPI.

    Args:
        df (DataFrame): Raw data from source CSV file

    Raises:
        ValueError: Variations in zipcode or FIPS data with the same NPI.

    Returns:
        demographics_df (DataFrame): Cleaned and standardized provider demographic data. One row per Rndrng_NPI.
    """
    demographics_df = df[DEMOGRAPHICS_COLUMNS].copy()

    demographics_df['Rndrng_Prvdr_Zip5'] = standardize_zipcode(
        demographics_df['Rndrng_Prvdr_Zip5']
    )

    has_fips = demographics_df['Rndrng_Prvdr_State_FIPS'].notna()
    demographics_df.loc[has_fips, 'Rndrng_Prvdr_State_FIPS'] = (
        demographics_df.loc[has_fips, 'Rndrng_Prvdr_State_FIPS']
        .astype(str)
        .str.zfill(2)
    )

    demographics_df.columns = [col.upper() for col in demographics_df.columns]

    demographics_df.drop_duplicates(inplace=True)

    if demographics_df.shape[0] != df['Rndrng_NPI'].nunique():
        raise ValueError(
            f'Variations in zipcode or FIPS data with the same NPI. Please verify data.'
        )

    return demographics_df


def create_services_table(df):
    """Creates a new DataFrame for provider service data.

    Copies columns in SERVICES_COLUMNS to new DataFrame and standardizes column names
    to uppercase with underscores.

    Args:
        df (DataFrame): Raw data from source CSV file

    Returns:
        services_df (DataFrame): Standardized provider service data. One row per NPI and HCPCS code combination.
    """
    services_df = df[SERVICES_COLUMNS].copy()

    services_df.columns = [col.upper() for col in services_df.columns]

    return services_df


def transform_provider_data(file_path):
    """Coordinates the cleaning and transformation of the provided data for Snowflake upload.

    Splits the data from the provided CSV file into demographic and service data tables.

    Args:
        file_path (str): Relative path to the source CSV file.

    Returns:
        demographic_df (DataFrame): Standardized provider demographic data. One row per RNDRNG_NPI.
        services_df aut(DataFrame): Standardized provider service data. One row per NPI and HCPCS code combination.
    """

    provider_df = load_data(file_path)

    demographics_df = create_demographics_table(provider_df)
    services_df = create_services_table(provider_df)

    return demographics_df, services_df
