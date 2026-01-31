import hashlib
import pandas as pd

try:
    from backend.db import engine
    DB_ENABLED = engine is not None
except:
    DB_ENABLED = False


def _hash(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()


def create_user(username, password):

    if not DB_ENABLED:
        return False

    hashed = _hash(password)

    df = pd.DataFrame(
        [[username, hashed]],
        columns=["username", "password"]
    )

    df.to_sql("users", engine, if_exists="append", index=False)
    return True


def login_user(username, password):

    # cloud safe fallback
    if not DB_ENABLED:
        # demo login for deployed app
        return username == "admin" and password == "admin123"

    hashed = _hash(password)

    query = f"""
    select * from users
    where username = '{username}'
      and password = '{hashed}'
    """

    try:
        df = pd.read_sql(query, engine)
        return len(df) == 1
    except:
        return False