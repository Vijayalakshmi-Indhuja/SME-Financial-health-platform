def calculate_metrics(df):
    revenue = df[df["type"]=="revenue"]["amount"].sum()
    expense = df[df["type"]=="expense"]["amount"].sum()
    loan = df[df["type"]=="loan_payment"]["amount"].sum()

    profit = revenue - expense
    margin = round((profit / revenue)*100,2)

    return {
        "revenue": revenue,
        "expense": expense,
        "profit": profit,
        "margin": margin,
        "loan": loan
    }
