from db.connection import get_connection
import psycopg 

def find_all_users():
    try:
        with get_connection() as conn:
            return conn.execute("SELECT * FROM public.users").fetchall()
    except psycopg.Error as e:
        print(e)

