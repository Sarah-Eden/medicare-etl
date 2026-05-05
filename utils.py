import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from dotenv import load_dotenv
import os
import pandas as pd


def create_snowflake_connection():
    load_dotenv()
    conn = None

    try:
        conn = snowflake.connector.connect(
            account = os.environ.get('SF_ACCOUNT'),
            user = os.environ.get('SF_USER'),
            password = os.environ.get('SF_PASSWORD'),
            role = os.environ.get('SF_ROLE'),
            database = os.environ.get('SF_DATABASE'),
            schema = os.environ.get('SF_SCHEMA'),
            warehouse = os.environ.get('SF_WAREHOUSE')
        )
    except Exception as e:
        print(f'Error connecting to snowflake: {e}')

    return conn


def df_to_snowflake(conn, df, table_name):
    try:
        write_pandas(conn, df, table_name, auto_create_table=True, overwrite=True)

    except Exception as e:
        print(f'Error writing data to snowflake: {e}')


def load_data(path):
    df = pd.read_csv(path, low_memory=False)
    return df