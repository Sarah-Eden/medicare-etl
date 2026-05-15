import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from dotenv import load_dotenv
import os
import pandas as pd


def create_snowflake_connection():
    """Creates a connection to snowflake."""
    load_dotenv()

    conn = snowflake.connector.connect(
        account=os.environ.get('SF_ACCOUNT'),
        user=os.environ.get('SF_USER'),
        password=os.environ.get('SF_PASSWORD'),
        role=os.environ.get('SF_ROLE'),
        database=os.environ.get('SF_DATABASE'),
        schema=os.environ.get('SF_SCHEMA'),
        warehouse=os.environ.get('SF_WAREHOUSE'),
    )

    return conn


def df_to_snowflake(conn, df, table_name):
    """Writes a DataFrame to a Snowflake table, creating or overwriting the table if it exists."""
    df = df.reset_index(drop=True)
    write_pandas(conn, df, table_name, auto_create_table=True, overwrite=True)


def load_data(file_path):
    """Loads data from a CSV file to a DataFrame, suppresses mixed datatype warning message."""
    df = pd.read_csv(file_path, low_memory=False, skipinitialspace=True)
    return df


def standardize_column_names(df):
    df.columns = [col.upper().replace(' ', '_') for col in df.columns]
    return df


def standardize_zipcode(zipcode_column):
    return zipcode_column.astype(str).str.zfill(5)


def standardize_footnotes(df, column):
    if isinstance(column, str):
        column = [column]
    for col in column:
        df[col] = df[col].astype('string').str.replace('.0', '', regex=False)
    return df
