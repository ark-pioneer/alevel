import os
from db.connection import run_sql_files

BASE_DIR = os.path.dirname(__file__)
SEEDS_DIR = os.path.join(BASE_DIR, "seeds")

def run_seeds():
    run_sql_files(SEEDS_DIR, "✅ All seed files applied successfully")

if __name__ == "__main__":
    run_seeds()