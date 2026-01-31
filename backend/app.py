from backend.storage import save_financial_data
from backend.data_loader import load_financial_data
from backend.metrics import calculate_metrics
from backend.risk_engine import detect_risks
from backend.scoring import credit_score
from backend.recommender import generate_recommendations
from backend.forecasting import monthly_forecast


def run_pipeline(file_path):
    df = load_financial_data(file_path)
    
    save_financial_data(df)

    metrics = calculate_metrics(df)
    risks = detect_risks(metrics)
    score = credit_score(metrics)
    recs = generate_recommendations(score, risks)
    forecast = monthly_forecast(df)

    return metrics, risks, score, recs, forecast
