from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
import os

app = FastAPI()


# Request model
class AnalyzeRequest(BaseModel):
    file_path: str


# Root route (VERY IMPORTANT for Render health check)
@app.get("/")
def home():
    return {"message": "SME Financial Health API is running 🚀"}


# Helper function to convert numpy types
def convert_numpy_types(obj):
    if isinstance(obj, dict):
        return {k: convert_numpy_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_types(i) for i in obj]
    elif isinstance(obj, np.integer):
        return int(obj)
    elif isinstance(obj, np.floating):
        return float(obj)
    else:
        return obj


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    try:
        # Validate file existence
        if not os.path.exists(request.file_path):
            raise HTTPException(status_code=404, detail="File not found")

        df = pd.read_csv(request.file_path)

        total_rows = int(df.shape[0])
        total_columns = int(df.shape[1])

        numeric_summary = {}

        for col in df.select_dtypes(include=[np.number]).columns:
            numeric_summary[col] = {
                "mean": float(df[col].mean()),
                "sum": float(df[col].sum()),
                "min": float(df[col].min()),
                "max": float(df[col].max()),
            }

        response = {
            "rows": total_rows,
            "columns": total_columns,
            "numeric_summary": numeric_summary
        }

        return convert_numpy_types(response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
