# SME Financial Health Platform

An end-to-end AI based financial health assessment platform for Small and Medium Enterprises (SMEs).

This application allows business users to upload their financial data and receive:
- Financial summary and KPIs
- Risk indicators
- Simple credit score
- Revenue forecasting
- Business recommendations
- Multilingual (English / Hindi) recommendations
- Secure login system

---

## Features

- Login based access
- CSV financial data upload
- Key financial metrics calculation
- Risk detection engine
- Credit scoring logic
- 6-month revenue forecasting (Linear Regression)
- Recommendation engine
- Multilingual output layer (English / Hindi)
- PostgreSQL support (local environment)
- Streamlit based dashboard

---

## Tech Stack

- Python
- Streamlit
- Pandas, NumPy
- Scikit-learn
- PostgreSQL (optional / local)
- SQLAlchemy

---

## Project Structure

<img width="200" height="500" alt="image" src="https://github.com/user-attachments/assets/c631b628-40e7-4497-bb34-f2d3917dd7d7" />

---

## How to Run Locally
       conda activate sme_env
       streamlit run frontend/streamlit_app.py
---

## Login

A sample user can be created using the backend authentication utility.

---

## Note on Database

PostgreSQL is supported for local development.
For cloud deployment the database layer is optional and disabled automatically.

---

## Purpose

This project was developed as a portfolio and hackathon project to demonstrate:
- financial analytics
- applied machine learning
- data pipelines
- AI driven recommendations
- dashboard development

