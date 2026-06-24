import snowflake.connector as sc
from snowflake.connector.pandas_tools import write_pandas
from dotenv import load_dotenv
import os


def create_snowflake_connection():
    """Creates a connection to snowflake."""
    load_dotenv()

    conn_params = {
        'account': os.environ.get('SNOWFLAKE_ACCOUNT'),
        'user': os.environ.get('SNOWFLAKE_USER'),
        'role': os.environ.get('SNOWFLAKE_ROLE'),
        'authenticator': 'SNOWFLAKE_JWT',
        'private_key_file': os.environ.get('SNOWFLAKE_PRIVATE_KEY_PATH'),
        'warehouse': os.environ.get('SNOWFLAKE_WAREHOUSE'),
        'database': os.environ.get('SNOWFLAKE_DATABASE'),
        'schema': os.environ.get('SNOWFLAKE_SCHEMA'),
    }

    missing = [key for key, value in conn_params.items() if value is None]

    if missing:
        raise ValueError(
            f'Values missing from connection parameters: {", ".join(missing)}'
        )

    conn = sc.connect(**conn_params)

    return conn


def df_to_snowflake(conn, df, table_name):
    """Writes a DataFrame to a Snowflake table, creating or overwriting the table if it exists."""
    df = df.reset_index(drop=True)
    success, _nchunks, _nrows, _ = write_pandas(
        conn, df, table_name, auto_create_table=True, overwrite=True
    )

    if not success:
        raise RuntimeError(f'write_pandas failed for table {table_name}')
