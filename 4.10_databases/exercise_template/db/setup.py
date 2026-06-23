import os
import psycopg
from connection import get_connection

BASE_DIR = os.path.dirname(__file__)
MIGRATIONS_DIR = os.path.join(BASE_DIR, "migrations")

def run_migrations():
    migrations = [f for f in os.listdir(MIGRATIONS_DIR) if f.endswith(".sql")]
    migrations.sort()

    conn = get_connection()
    try:
        for migration in migrations:
            file_path = os.path.join(MIGRATIONS_DIR, migration)

            with open(file_path, "r") as f:
                query_string = f.read()

            print(f"Running: {migration}")
            conn.execute(query_string)
        
        conn.commit()
        print("✅ All migrations applied successfully")

    except psycopg.Error as e:
        conn.rollback()
        print("❌ Database error occurred")
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    run_migrations()

