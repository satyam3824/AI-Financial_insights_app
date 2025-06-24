# helpers.py

import pandas as pd
import google.generativeai as genai
from fpdf import FPDF

def configure_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("models/gemini-1.5-flash")  # updated model name

def calculate_ratios(df):
    df["Net Profit Margin (%)"] = (df["Net Profit"] / df["Revenue"]) * 100
    df["Expense Ratio (%)"] = (df["Expenses"] / df["Revenue"]) * 100
    return df

def generate_insights(df, model):
    try:
        latest = df.iloc[-1]
        previous = df.iloc[-2]

        prompt = f"""
        Analyze this financial performance:

        - Latest Year: {int(latest['Year'])}
        - Revenue: ₹{latest['Revenue']}
        - Expenses: ₹{latest['Expenses']}
        - Net Profit: ₹{latest['Net Profit']}
        - Net Profit Margin: {latest['Net Profit Margin (%)']:.2f}%
        - Expense Ratio: {latest['Expense Ratio (%)']:.2f}%

        Previous Year: {int(previous['Year'])}
        - Revenue: ₹{previous['Revenue']}
        - Net Profit: ₹{previous['Net Profit']}

        Provide a business-style performance summary and improvement suggestions.
        """

        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error generating insights: {e}"

def export_pdf(summary_text, filename="Financial_Summary.pdf"):
    from fpdf import FPDF
    import textwrap
    import re

    def safe_text(text):
        # Remove characters FPDF can't handle
        return re.sub(r'[^\x00-\x7F]+', '', text)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    max_width = 90  # line wrap width

    for line in summary_text.split('\n'):
        clean_line = safe_text(line).strip()
        if not clean_line:
            continue

        # Wrap line to avoid overflow
        wrapped = textwrap.wrap(clean_line, width=max_width)
        for wline in wrapped:
            try:
                pdf.multi_cell(0, 10, wline)
            except Exception:
                try:
                    pdf.cell(0, 10, "⚠️ Skipped a line due to width issue", ln=True)
                except:
                    pass  # fully skip if even this fails

    pdf.output(filename)
    return filename
