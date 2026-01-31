import pandas as pd

def load_financial_data(path):
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
    return df
