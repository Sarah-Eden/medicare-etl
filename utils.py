import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from dotenv import load_dotenv
import os
import pandas as pd


def create_snowflake_connection():
    """Creates a connection to snowflake."""
    load_dotenv()

    conn = snowflake.connector.connect(
        account = os.environ.get('SF_ACCOUNT'),
        user = os.environ.get('SF_USER'),
        password = os.environ.get('SF_PASSWORD'),
        role = os.environ.get('SF_ROLE'),
        database = os.environ.get('SF_DATABASE'),
        schema = os.environ.get('SF_SCHEMA'),
        warehouse = os.environ.get('SF_WAREHOUSE')
    )

    return conn


def df_to_snowflake(conn, df, table_name):
    """Writes a DataFrame to a Snowflake table, creating or overwriting the table if it exists."""
    write_pandas(conn, df, table_name, auto_create_table=True, overwrite=True)


def load_data(path):
    """Loads data from a CSV file to a DataFrame, suppresses mixed datatype warning message."""
    df = pd.read_csv(path, low_memory=False)
    return df