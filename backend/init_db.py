from db import engine
from sqlalchemy import text

query = """
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
"""

#engine.connect().execute(text(query))
#print("Tables created")

with engine.begin() as conn:
    conn.execute(text(query))

print("Users table created successfully")
