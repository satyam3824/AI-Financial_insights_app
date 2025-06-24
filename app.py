# app.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from helpers import configure_gemini, generate_insights, calculate_ratios, export_pdf

# App UI
st.set_page_config(page_title="AI Financial Summary", layout="wide")
st.title("📊 AI-Powered Financial Summary & Ratio Analyzer")

st.markdown("Upload your company financial data and get AI-generated performance insights.")

# Load Gemini
api_key = st.secrets["generation"]["api_key"]
model = configure_gemini(api_key)

# File Upload
uploaded = st.file_uploader("Upload Excel or CSV file", type=["csv", "xlsx"])

if uploaded:
    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded)

    st.subheader("📂 Uploaded Financial Data")
    st.dataframe(df)

    # Calculate ratios
    df = calculate_ratios(df)

    if st.button("🚀 Generate AI Insights"):
        with st.spinner("Generating insights using Gemini..."):
            summary = generate_insights(df, model)
            st.subheader("🧠 AI-Generated Summary")
            st.markdown(summary)

            # Export to PDF
            pdf_filename = export_pdf(summary)
            with open(pdf_filename, "rb") as f:
                st.download_button("📄 Download PDF Report", f, file_name=pdf_filename)

    # Chart
    st.subheader("📊 Revenue & Profit Chart")
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df["Year"], y=df["Revenue"], name="Revenue", marker_color="green"))
    fig.add_trace(go.Bar(x=df["Year"], y=df["Net Profit"], name="Net Profit", marker_color="blue"))
    fig.update_layout(barmode='group', title="Revenue vs Net Profit")
    st.plotly_chart(fig)

    # Show calculated ratios
    st.subheader("📈 Ratio Analysis")
    st.dataframe(df[["Year", "Net Profit Margin (%)", "Expense Ratio (%)"]])
