from pathlib import Path
from datetime import datetime
import re
import sys

MIGRATIONS_DIR = Path("db/migrations")

def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text

def create_migration(description, directory = MIGRATIONS_DIR):
    directory.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%y%m%d%H%M")
    filename = f"{timestamp}_{slugify(description)}.sql"
    path = directory / filename

    template = f"""-- Migration: {description}
-- Created at: {timestamp}

-- Write SQL below


"""

    path.write_text(template, encoding="utf-8")
    return path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_migration.py \"description_here\"")
        raise SystemExit(1)

    description = " ".join(sys.argv[1:])
    path = create_migration(description)
    print(f"Created: {path}")
