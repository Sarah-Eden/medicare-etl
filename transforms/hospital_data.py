import pandas as pd
from transforms.utils import (
    load_data,
    standardize_zipcode,
    standardize_footnotes,
    standardize_column_names,
)


def transform_hospital_data(file_path):
    """Cleans and standardizes hospital data for Snowflake upload.

    Standardizes column names to uppercase with underscores, converts zipcodes to 5
    digits, and converts footnote columns to strings to preserve comma-separated values.

    Args:
        file_path (str): Relative path to the source CSV file.

    Returns:
        hospital_df (DataFrame): Cleaned & Standardized hospital data.
    """

    hospital_df = load_data(file_path)

    hospital_df = standardize_column_names(hospital_df)
    hospital_df.columns = [col.replace('/', '_') for col in hospital_df.columns]

    hospital_df['ZIP_CODE'] = standardize_zipcode(hospital_df['ZIP_CODE'])

    footnote_cols = [c for c in hospital_df.columns if '_FOOTNOTE' in c]

    hospital_df = standardize_footnotes(hospital_df, footnote_cols)

    return hospital_df
