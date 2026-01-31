from sqlalchemy import create_engine
import os

DATABASE_URL = os.getenv("DATABASE_URL")

# For local testing ONLY
#if DATABASE_URL is None:
   # DATABASE_URL = "postgresql://neondb_owner:npg_UVB3wdDN8AWj@ep-flat-king-ah41moa0-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL not set")

engine = create_engine(DATABASE_URL)


#from sqlalchemy import create_engine

#DB_USER = "postgres"
#DB_PASSWORD = "mypostgres123"
#DB_HOST = "localhost"
#DB_PORT = "5432"
#DB_NAME = "sme_db"

#engine = create_engine(
#   f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#)