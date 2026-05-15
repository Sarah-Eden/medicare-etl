import pandas as pd
from transforms.utils import (
    load_data,
    standardize_zipcode,
    standardize_footnotes,
    standardize_column_names,
)


def transform_hospital_quality_data(file_path):
    """Cleans and standardizes hospital quality data for Snowflake upload.

    Standardizes column names to uppercase with underscores, converts zipcodes to 5
    digits, and converts footnote columns to strings to preserve comma-separated values.

    Args:
        file_path (str): Relative path to the source CSV file.

    Returns:
        quality_df (DataFrame): Cleaned & Standardized data.
    """

    quality_df = load_data(file_path)

    quality_df = standardize_column_names(quality_df)

    quality_df['ZIP_CODE'] = standardize_zipcode(quality_df['ZIP_CODE'])

    quality_df = standardize_footnotes(quality_df, 'FOOTNOTE')

    return quality_df
