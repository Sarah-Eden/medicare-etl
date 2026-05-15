import pandas as pd
from transforms.utils import load_data, standardize_column_names


def transform_affiliation_data(file_path):
    """Cleans and standardizes facility affiliation data for Snowflake upload.

    Filters dataset based on facility type and standardizes column names to uppercase with underscores.

    Args:
        file_path (str): Relative path to the source CSV file.

    Returns:
        affiliation_df (DataFrame): Standardized DataFrame for junction table.
    """

    df = load_data(file_path)

    affiliation_df = df.loc[
        df['facility_type'] == 'Hospital',
        ['NPI', 'Facility Affiliations Certification Number'],
    ].copy()

    affiliation_df = standardize_column_names(affiliation_df)

    affiliation_df.drop_duplicates(inplace=True)

    return affiliation_df
