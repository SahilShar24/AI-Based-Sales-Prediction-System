import streamlit as st
import pandas as pd
from cleaning import clean_data
from eda import generate_eda
from visualization import generate_charts
from insights import generate_insights

# Title
st.title("🛒 Data Analysis Automation Bot")

# Description
st.write("Upload your dataset and let the bot analyze it automatically.")

# File Upload
file = st.file_uploader("Upload CSV file", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    # Clean data
    df, report = clean_data(df)

    st.subheader("🧹 Data Cleaning Report")
    for key, value in report.items():
        st.write(f"{key}: {value}")

    st.subheader("📊 Raw Data Preview")
    st.dataframe(df.head())
    
    st.subheader("✅ Cleaned Data Preview")
    st.dataframe(df.head())

    st.subheader("📌 Dataset Info")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])
    st.write("Column Names:", list(df.columns))

    #eda
    eda_report = generate_eda(df)

    st.subheader("📊 Data Summary")
    st.dataframe(eda_report['summary'])

    st.subheader("📌 Top Categories")
    for col, values in eda_report['top_categories'].items():
        st.write(f"Top values in {col}:")
        st.write(values)

    # Charts
    st.subheader("📈 Visualizations")

    charts = generate_charts(df)

    for chart in charts:
        st.plotly_chart(chart)
    
    st.subheader("🤖 AI Insights")

    insights = generate_insights(df)

    for insight in insights:
        st.write(insight)