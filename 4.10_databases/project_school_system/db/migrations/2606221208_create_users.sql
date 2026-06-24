CREATE TABLE IF NOT EXISTS users(
  id SERIAL PRIMARY KEY,
  first_name varchar(60),
  last_name varchar(60),
  email varchar(80)
)