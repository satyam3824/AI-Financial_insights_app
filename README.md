# AI-Financial_insights_app# 💼 AI-Powered Financial Summary Generator

This Streamlit app lets users upload Excel or CSV files with financial data (Revenue, Expenses, Net Profit), and instantly generates:

- 📈 Visual charts (Revenue vs Profit)
- 📊 Key financial ratios (Net Profit Margin, Expense Ratio)
- 🤖 AI-generated performance summary (via Gemini Pro or Flash)
- 📄 Downloadable PDF report with business-style insights

---

## 🚀 Features

- Upload **Excel/CSV** financial data
- Calculates:
  - Net Profit Margin (%)
  - Expense Ratio (%)
- Generates **performance summary and improvement suggestions** using Gemini AI
- Exports AI insights as a **PDF**
- Visualizes data with **Plotly bar charts**
- Fully interactive via **Streamlit UI**

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [Google Gemini API (Generative AI)](https://ai.google.dev/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/)
- [FPDF2](https://py-pdf.github.io/fpdf2/) (for PDF export)

---

## 📂 Sample Data Format

You can upload a file like this (`.xlsx` or `.csv`):

| Year | Revenue | Expenses | Net Profit |
|------|---------|----------|------------|
| 2022 | 900000  | 600000   | 300000     |
| 2023 | 1200000 | 800000   | 400000     |

> ✅ Excel sheet must have columns named exactly: `Year`, `Revenue`, `Expenses`, `Net Profit`.

---

## 🔐 API Key Setup

1. Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a `.streamlit/secrets.toml` file:

```toml
[generation]
api_key = "YOUR_GEMINI_API_KEY"
