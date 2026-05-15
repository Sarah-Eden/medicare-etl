import pandas as pd
from transforms.utils import load_data, standardize_column_names


def transform_mips_data(file_path):
    """Cleans and standardizes MIPS data for Snowflake upload.

    Standardizes column names to uppercase with underscores.

    Args:
        file_path (str): Relative path to the source CSV file.

    Returns:
        mips_df (DataFrame): Standardized MIPS data.
    """

    mips_df = load_data(file_path)

    mips_df = standardize_column_names(mips_df)

    return mips_df
