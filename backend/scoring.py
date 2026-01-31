def credit_score(m):
    score = 100

    if m["margin"] < 10:
        score -= 25
    if m["loan"] > 0.3 * m["revenue"]:
        score -= 30
    if m["expense"] > m["revenue"]:
        score -= 30

    return max(score,0)
