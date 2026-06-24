# School System
## An Example Python Application connected to a database

## 🧠 What you are learning

- Connecting Python to a PostgreSQL database
- Writing and running SQL queries
- Structuring a small multi-file project

# Quickstart

### 0. Navigate to project folder
```
cd [project folder]
```

### 1. Install external packages of code (dependencies)
```
pip install -r requirements.txt
```

### 2. Set up environment variables
Create a .env file using the example provided:
```
cp .env.example .env 

```
If you haven't yet, create a new local database for this project.
```sql
-- inside the query editor in pgadmin
CREATE DATABASE project_dev;
```
⚠️ Update the values inside .env with your database credentials. Check with your teacher if you need help.

### 3. Set up the database tables

```
python -m db.migrate
```

### 4. Seed your database tables with data
```
python -m db.seed
```

### 5. Run the app and follow the instructions in app.py
```
python app.py
```



## Migrations vs seeds

### Migrations
Migrations change the **structure** of the database.

Examples:
- create a table
- add a column
- add a foreign key
- add a unique constraint

Store these in:

```text
db/migrations/
```

### Seeds
Seeds insert **sample / default data**.

Examples:
- default users
- role lookup data
- sample courses
- sample enrolments
- sample assignments

Store these in:

```text
db/seeds/
```

## Migration worflow
Use the migration helper script to create a new SQL file inside db/migrations. For example:
```
python db/create_migration.py "create enrolments"
```
Then add the sql you want to execute to the generated file. Afterwards, run the migrations
```
python -m db.migrate
```

## psycopg documentation

Use the official usage [docs](https://www.psycopg.org/psycopg3/docs/basic/usage.html) to understand how it works