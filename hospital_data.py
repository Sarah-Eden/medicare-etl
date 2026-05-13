import pandas as pd
import numpy as np
from utils import load_data, standardize_zipcode


def transform_hospital_data(file_path):
    """Cleans and standardizes hospital data for Snowflake upload.

    Standardizes column names to uppercase with underscores, converts zipcodes to 5
    digits, converts numeric columns from mixed types to numeric, and converts footnote
    columns to strings to preserve comma-separated values.

    Args:
        file_path (str): Relative path to the source CSV file.

    Returns:
        DataFrame: Cleaned & Standardized hospital data.
    """

    hospital_df = load_data(file_path)

    hospital_df.columns = [
        col.upper().replace(' ', '_').replace('/', '_') for col in hospital_df.columns
    ]

    hospital_df['ZIP_CODE'] = standardize_zipcode(hospital_df['ZIP_CODE'])

    hospital_df.replace('Not Available', np.nan, inplace=True)

    num_col = [
        'HOSPITAL_OVERALL_RATING',
        'MORT_GROUP_MEASURE_COUNT',
        'COUNT_OF_FACILITY_MORT_MEASURES',
        'COUNT_OF_MORT_MEASURES_BETTER',
        'COUNT_OF_MORT_MEASURES_NO_DIFFERENT',
        'COUNT_OF_MORT_MEASURES_WORSE',
        'SAFETY_GROUP_MEASURE_COUNT',
        'COUNT_OF_FACILITY_SAFETY_MEASURES',
        'COUNT_OF_SAFETY_MEASURES_BETTER',
        'COUNT_OF_SAFETY_MEASURES_NO_DIFFERENT',
        'COUNT_OF_SAFETY_MEASURES_WORSE',
        'READM_GROUP_MEASURE_COUNT',
        'COUNT_OF_FACILITY_READM_MEASURES',
        'COUNT_OF_READM_MEASURES_BETTER',
        'COUNT_OF_READM_MEASURES_NO_DIFFERENT',
        'COUNT_OF_READM_MEASURES_WORSE',
        'PT_EXP_GROUP_MEASURE_COUNT',
        'COUNT_OF_FACILITY_PT_EXP_MEASURES',
        'TE_GROUP_MEASURE_COUNT',
        'COUNT_OF_FACILITY_TE_MEASURES',
    ]

    hospital_df[num_col] = hospital_df[num_col].apply(pd.to_numeric)

    footnote_col = [c for c in hospital_df.columns if '_FOOTNOTE' in c]

    for col in footnote_col:
        not_null = hospital_df[col].notna()
        hospital_df.loc[not_null, col] = hospital_df.loc[not_null, col].astype(str)

    return hospital_df
