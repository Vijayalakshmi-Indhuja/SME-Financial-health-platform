try:
    from backend.db import engine
    DB_ENABLED = True
except:
    DB_ENABLED = False


def save_financial_data(df):

    if not DB_ENABLED:
        return

    df.to_sql(
        "financial_data",
        engine,
        if_exists="append",
        index=False
    )


#from backend.db import engine

#def save_financial_data(df):
#    df.to_sql(
#       "financial_data",
#        engine,
#        if_exists="append",
#        index=False
#    )