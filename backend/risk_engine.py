def detect_risks(m):
    risks=[]

    if m["margin"] < 10:
        risks.append("Low profit margin")

    if m["loan"] > 0.3 * m["revenue"]:
        risks.append("High loan burden")

    if m["expense"] > m["revenue"]:
        risks.append("Expenses exceed revenue")

    return risks
