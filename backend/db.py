import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    engine = create_engine(DATABASE_URL)
else:
    engine = None



#from sqlalchemy import create_engine

#DB_USER = "postgres"
#DB_PASSWORD = "mypostgres123"
#DB_HOST = "localhost"
#DB_PORT = "5432"
#DB_NAME = "sme_db"

#engine = create_engine(
#   f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#)