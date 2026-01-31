import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

import streamlit as st
import backend.auth as auth
from backend.app import run_pipeline
from backend.translator import translate_list

st.set_page_config(page_title="SME Financial Platform")

st.title("SME Financial Health Platform")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.subheader("Login")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if auth.login_user(user, pwd):
            st.session_state.logged_in = True
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")

    st.stop()


# -------- After login --------
language = st.selectbox("Select Language", ["English", "Hindi"])
file = st.file_uploader("Upload financial CSV")

if file:
    with open("temp.csv","wb") as f:
        f.write(file.getbuffer())

    metrics, risks, score, recs, forecast = run_pipeline("temp.csv")

    st.subheader("Summary")
    st.json(metrics)

    st.subheader("Credit Score")
    st.metric("Score",score)

    st.subheader("Risks")
    for r in risks:
        st.warning(r)

    st.subheader("Recommendations")
    translated_recs = translate_list(recs, language)
    for r in translated_recs:
        st.success(r)

    st.subheader("6 Month Revenue Forecast")
    st.line_chart(forecast)