def generate_recommendations(score, risks):
    recs=[]

    if score>70:
        recs.append("Eligible for business loan")
    elif score>50:
        recs.append("Suitable for working capital loan")
    else:
        recs.append("Improve finances before borrowing")

    if "Low profit margin" in risks:
        recs.append("Reduce operating costs")

    if "High loan burden" in risks:
        recs.append("Consider refinancing loan")

    return recs
