import os
from db.connection import run_sql_files

BASE_DIR = os.path.dirname(__file__)
MIGRATIONS_DIR = os.path.join(BASE_DIR, "migrations")

def run_migrations():
    run_sql_files(MIGRATIONS_DIR, "✅ All migrations applied successfully")

if __name__ == "__main__":
    run_migrations()