import numpy as np
from sklearn.linear_model import LinearRegression

def monthly_forecast(df):
    rev = df[df["type"]=="revenue"]
    monthly = rev.groupby(rev["date"].dt.month)["amount"].sum()

    X = np.array(range(len(monthly))).reshape(-1,1)
    y = monthly.values

    model = LinearRegression()
    model.fit(X,y)

    future = np.array([[len(monthly)+i] for i in range(6)])
    preds = model.predict(future)

    return preds.round(0)
