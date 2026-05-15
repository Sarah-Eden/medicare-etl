import pandas as pd
from transforms.utils import (
    load_data,
    standardize_zipcode,
    standardize_footnotes,
    standardize_column_names,
)


def transform_hcahps_data(file_path):
    """Cleans and standardizes HCAHPS data for Snowflake upload.

    Standardizes column names to uppercase with underscores, converts zipcodes to 5
    digits, and converts footnote columns to strings to preserve comma-separated values.

    Args:
        file_path (str): Relative path to the source CSV file.

    Returns:
        hcahps_df (DataFrame): Cleaned & Standardized HCAHPS data.
    """

    hcahps_df = load_data(file_path)

    hcahps_df = standardize_column_names(hcahps_df)

    hcahps_df['ZIP_CODE'] = standardize_zipcode(hcahps_df['ZIP_CODE'])

    footnote_cols = [col for col in hcahps_df.columns if '_FOOTNOTE' in col]

    hcahps_df = standardize_footnotes(hcahps_df, footnote_cols)

    return hcahps_df
