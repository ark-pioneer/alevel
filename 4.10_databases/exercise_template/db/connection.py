import psycopg 

import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("PG_PASS")
    )

def run_sql_files(directory, success_message):
    sql_files = [f for f in os.listdir(directory) if f.endswith(".sql")]
    sql_files.sort()

    conn = get_connection()
    try:
        for sql_file in sql_files:
            file_path = os.path.join(directory, sql_file)

            with open(file_path, "r", encoding="utf-8") as f:
                query_string = f.read()

            print(f"Running {directory}: {sql_file}")
            conn.execute(query_string)

        conn.commit()
        print(success_message)

    except psycopg.Error as e:
        conn.rollback()
        print("❌ Database error occurred")
        print(e)
    finally:
        conn.close()