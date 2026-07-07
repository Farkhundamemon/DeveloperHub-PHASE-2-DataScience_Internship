import streamlit as st
import pandas as pd

st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")

df = pd.read_csv('Global_Superstore2.csv', encoding='latin1')

st.title("Global Superstore Business Dashboard")

st.sidebar.header("Filters")
region = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
category = st.sidebar.multiselect("Select Category", options=df['Category'].unique(), default=df['Category'].unique())
subcategory = st.sidebar.multiselect("Select Sub-Category", options=df['Sub-Category'].unique(), default=df['Sub-Category'].unique())

filtered_df = df[
    (df['Region'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Sub-Category'].isin(subcategory))
]

col1, col2 = st.columns(2)
col1.metric("Total Sales", f"${filtered_df['Sales'].sum():,.2f}")
col2.metric("Total Profit", f"${filtered_df['Profit'].sum():,.2f}")

st.subheader("Top 5 Customers by Sales")
top_customers = filtered_df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)
st.bar_chart(top_customers)