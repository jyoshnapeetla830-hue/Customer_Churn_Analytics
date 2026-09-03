import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

df = pd.read_csv("data/cleaned_churn_data.csv")

st.title("📊 Customer Churn Analytics Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", len(df))
col2.metric("Churned Customers", (df["Churn"] == "Yes").sum())
col3.metric("Churn Rate", f"{(df['Churn'] == 'Yes').mean() * 100:.2f}%")

st.subheader("Churn by Contract")
contract_data = pd.crosstab(df["Contract"], df["Churn"])
st.bar_chart(contract_data)

st.subheader("Churn by Internet Service")
internet_data = pd.crosstab(df["InternetService"], df["Churn"])
st.bar_chart(internet_data)

st.subheader("Churn by Payment Method")
payment_data = pd.crosstab(df["PaymentMethod"], df["Churn"])
st.bar_chart(payment_data)

st.subheader("Churn by Senior Citizen Status")
senior_data = pd.crosstab(df["SeniorCitizen"], df["Churn"])
st.bar_chart(senior_data)

st.subheader("Churn by Tenure Group")
tenure_data = pd.crosstab(df["tenure_group"], df["Churn"])
st.bar_chart(tenure_data)