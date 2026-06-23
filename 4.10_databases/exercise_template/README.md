## Example application connected to a database

## 🧠 What you are learning

- Connecting Python to a PostgreSQL database
- Writing and running SQL queries
- Structuring a small multi-file project

# Quickstart

0. Navigate to project folder
`cd [project folder]`

1. Install external packages of code (dependencies)
` pip install -r requirements.txt`

2. Set up environment variables
Create a .env file using the example provided:
`copy .env.example .env   # Windows`
Then update the values inside .env with your database credentials.

3. Set up the database tables
`python db/setup.py`

4. Run the app and follow the instructions in app.py
`python app.py`
