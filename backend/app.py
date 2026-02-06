from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np

app = FastAPI()

# Request model
class AnalyzeRequest(BaseModel):
    file_path: str


@app.get("/")
def home():
    return {"message": "SME Financial Health API is running "}


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    try:
        # Load CSV
        df = pd.read_csv(request.file_path)

        # Basic metrics
        total_rows = int(df.shape[0])
        total_columns = int(df.shape[1])

        numeric_summary = {}

        # Convert numpy values to normal Python types
        for col in df.select_dtypes(include=[np.number]).columns:
            numeric_summary[col] = {
                "mean": float(df[col].mean()),
                "sum": float(df[col].sum()),
                "min": float(df[col].min()),
                "max": float(df[col].max()),
            }

        return {
            "rows": total_rows,
            "columns": total_columns,
            "numeric_summary": numeric_summary
        }

    except Exception as e:
        return {"error": str(e)}
