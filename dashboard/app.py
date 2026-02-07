import pandas as pd
import streamlit as st
import plotly.express as px
import os

st.title("📊 Sales Data Analytics Dashboard")

# Absolute path handling (bulletproof)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_FILE = os.path.join(BASE_DIR, "data", "sales_data_cleaned.csv")

st.write("📁 Loading data from:")
st.code(DATA_FILE)

# Load data
df = pd.read_csv(DATA_FILE)

# Bar chart
st.subheader("Revenue by Product")
fig_bar = px.bar(df, x="Product", y="Revenue", color="Product")
st.plotly_chart(fig_bar)

# Pie chart
st.subheader("Revenue by Category")
fig_pie = px.pie(df, names="Category", values="Revenue")
st.plotly_chart(fig_pie)

# Line chart
st.subheader("Sales Trend Over Time")
fig_line = px.line(df, x="Date", y="Revenue")
st.plotly_chart(fig_line)
