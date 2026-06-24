from transforms.utils import create_snowflake_connection
import logging


def run_scripts(conn):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    logger.addHandler(handler)

    scripts = ['sql/constraints.sql', 'sql/views.sql']
    current_script = ""

    try:

        for script in scripts:
            current_script = script
            with open(script, 'r') as sql_file:
                for result_cursor in conn.execute_stream(
                    sql_file, remove_comments=True
                ):
                    for result in result_cursor:
                        logger.info(f'Result: {result}')
            logger.info(f'{current_script} executed successfully.')

    except Exception as e:
        logger.error(f'Script: {current_script},  Error: {e}')
        raise


if __name__ == '__main__':
    conn = None

    try:
        conn = create_snowflake_connection()
        run_scripts(conn)
    finally:
        if conn:
            conn.close()
