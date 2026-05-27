import pandas as pd


def transform_data(
    file_path,
    specify_dtype=None,
    filter_rows=None,
    keep_columns=None,
    drop_duplicates=False,
    split_data=None,
):
    """Function to clean and standardize raw CMS data from CSV files for upload into Snowflake.

    Args:
        file_path (str): Relative path to CSV file.
        specify_dtype (Dictionary, optional): Dictionary with column names as keys and data type as value to override defaults on import. Defaults to None.
        filter_rows (Dictionary, optional): Dictionary with column names as keys and value on which to filter as value. Defaults to None.
        keep_columns (List, optional): List of column names to keep in DataFrame. Defaults to None.
        drop_duplicates (bool, optional): Will drop any rows where all values are duplicated. Defaults to False.
        split_data (List, optional): List for splitting data into multiple tables. Each item in list is a list of columns for one table. Defaults to None.

    Returns:
        DataFrame | List of DataFrames if split_data is not None: Standardized data for upload into Snowflake.
    """
    data = pd.read_csv(
        file_path, low_memory=False, skipinitialspace=True, dtype=specify_dtype
    )

    if filter_rows is not None:
        for col, value in filter_rows.items():
            data = data.loc[data[col] == value]

    if keep_columns is not None:
        data = data[keep_columns].copy()

    if drop_duplicates:
        data = data.drop_duplicates()

    if split_data is not None:
        df_list = [data[cols].copy() for cols in split_data]
        for df in df_list:
            df.columns = [
                col.upper().replace(' ', '_').replace('/', '_').replace('-', '_')
                for col in df.columns
            ]
        return df_list

    data.columns = [
        col.upper().replace(' ', '_').replace('/', '_').replace('-', '_')
        for col in data.columns
    ]

    return data
