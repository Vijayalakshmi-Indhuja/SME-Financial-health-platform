import hashlib
import pandas as pd
from backend.db import engine

def _hash(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()

def create_user(username, password):
    hashed = _hash(password)

    df = pd.DataFrame(
        [[username, hashed]],
        columns=["username", "password"]
    )

    df.to_sql("users", engine, if_exists="append", index=False)

def login_user(username, password):
    hashed = _hash(password)

    query = f"""
    select * from users
    where username = '{username}'
      and password = '{hashed}'
    """

    df = pd.read_sql(query, engine)

    return len(df) == 1