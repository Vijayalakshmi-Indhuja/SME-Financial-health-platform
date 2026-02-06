# SME Financial Health Platform

An end-to-end AI-based financial health assessment platform for Small and Medium Enterprises (SMEs).

This system analyzes SME financial data and generates:

- Financial summary metrics
- Risk indicators
- Revenue statistics
- Basic forecasting insights
- Structured JSON analysis output

The backend API is built using FastAPI and deployed on Render Cloud.

---

## 🚀 Live Deployment

API Base URL:
https://sme-finance-api.onrender.com

Swagger Documentation:
https://sme-finance-api.onrender.com/docs

---

## 🛠 Tech Stack

Backend:
- Python
- FastAPI
- Uvicorn
- Pandas
- NumPy

Deployment:
- Render
- GitHub

Optional:
- PostgreSQL
- SQLAlchemy

---

## 📁 Project Structure

<img width="257" height="611" alt="image" src="https://github.com/user-attachments/assets/74042159-d730-4fba-b10b-b17a463d7e84" />


---

## 📊 API Endpoint

### POST /analyze

Request Body:

{
  "file_path": "data/sample_financials.csv"
}

Response:

{
  "rows": 12,
  "columns": 4,
  "numeric_summary": {
    "amount": {
      "mean": 47916.66,
      "sum": 575000,
      "min": 15000,
      "max": 130000
    }
  }
}

---

## ⚙️ Local Setup

1️⃣ Clone Repository

       git clone https://github.com/Vijayalakshmi-Indhuja/SME-Financial-health-platform.git
       cd SME-Financial-health-platform
---

2️⃣ Create Environment

      conda create -n sme_env python=3.10
      conda activate sme_env


4️⃣ Run Application

      uvicorn backend.app:app --reload


Access:
http://127.0.0.1:8000/docs

---

## ☁️ Deployment (Render)

Start command used in Render:

      uvicorn backend.app:app --host 0.0.0.0 --port 10000


---

## 🎯 Use Case

This platform helps SMEs:
- Understand financial health
- Monitor revenue patterns
- Detect risk indicators
- Generate structured financial insights

---

## 👩‍💻 Author

Vijayalakshmi K   
Hackathon Submission Project
