import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load data
df = pd.read_csv("sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M').astype(str)

# Sidebar filters
st.sidebar.header("Filters")
region = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
product = st.sidebar.multiselect("Select Product", options=df['Product'].unique(), default=df['Product'].unique())

# Filtered Data
df_filtered = df[(df['Region'].isin(region)) & (df['Product'].isin(product))]

# Dashboard Title
st.title("Sales & Revenue Dashboard")

# KPIs
total_revenue = df_filtered['Total Revenue'].sum()
total_units = df_filtered['Units Sold'].sum()

st.metric("Total Revenue", f"${total_revenue:,.2f}")
st.metric("Total Units Sold", f"{total_units:,}")

# Plots
st.subheader("Revenue by Region")
fig1, ax1 = plt.subplots()
sns.barplot(data=df_filtered.groupby("Region")["Total Revenue"].sum().reset_index(),
            x="Region", y="Total Revenue", ax=ax1)
st.pyplot(fig1)

st.subheader("Monthly Revenue Trend")
monthly = df_filtered.groupby("Month")["Total Revenue"].sum().reset_index()
fig2, ax2 = plt.subplots()
sns.lineplot(data=monthly, x="Month", y="Total Revenue", marker="o", ax=ax2)
plt.xticks(rotation=45)
st.pyplot(fig2)

st.subheader("Top Products by Revenue")
top_products = df_filtered.groupby("Product")["Total Revenue"].sum().sort_values(ascending=False).head(5)
fig3, ax3 = plt.subplots()
sns.barplot(x=top_products.values, y=top_products.index, ax=ax3)
st.pyplot(fig3)