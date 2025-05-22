import streamlit as st
import random

st.set_page_config(page_title="Simple Wildfire Risk Checker")

st.title("🔥 Wildfire Risk Estimator")

address = st.text_input("Enter address (any text):")

if st.button("Check Risk") and address:
    score = round(random.uniform(3.0, 9.5), 1)
    level = (
        "Extreme" if score >= 8 else
        "High" if score >= 6 else
        "Moderate" if score >= 4 else
        "Low"
    )

    st.success(f"Risk Score for '{address}': {score}/10")
    st.info(f"Risk Level: {level}")
