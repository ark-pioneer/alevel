import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(dbname="neondb", host="ep-lucky-brook-a2vpkefg-pooler.eu-central-1.aws.neon.tech", user="neondb_owner", password="npg_Win31vtJhfIw")
print("got connection")
# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM users")
print("excuted query")
# Retrieve query results
records = cur.fetchall()
print(records)