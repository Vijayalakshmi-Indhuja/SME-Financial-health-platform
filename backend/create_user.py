from db import engine
from sqlalchemy import text
import hashlib

username = "admin"
password = "admin123"

hashed = hashlib.sha256(password.encode()).hexdigest()

query = """
INSERT INTO users (username, password)
VALUES (:u, :p)
ON CONFLICT (username) DO NOTHING
"""

with engine.begin() as conn:
    conn.execute(text(query), {"u": username, "p": hashed})

print("User created")
