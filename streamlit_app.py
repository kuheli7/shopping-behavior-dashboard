# -*- coding: utf-8 -*-
# Copyright 2024-2025 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Customized from Streamlit Gallery: Seattle Weather Template

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Shopping Behaviour Analysis",
    layout="wide",
)

# ---------------- Load Dataset ----------------
@st.cache_data
def load_data():
    return pd.read_csv("shopping_behavior_updated.csv")

df = load_data()

# ---------------- Sidebar Filters ----------------
st.sidebar.title("Filter Options")

category = st.sidebar.multiselect(
    "Product Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

gender = st.sidebar.multiselect(
    "Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)

payment = st.sidebar.multiselect(
    "Payment Method",
    df["Payment Method"].unique(),
    default=df["Payment Method"].unique()
)

age_range = st.sidebar.slider(
    "Age Range",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (18, 60)
)

# ---------------- Apply Filters ----------------
filtered_df = df[
    (df["Category"].isin(category)) &
    (df["Gender"].isin(gender)) &
    (df["Payment Method"].isin(payment)) &
    (df["Age"].between(age_range[0], age_range[1]))
]

# ---------------- Title ----------------
st.title("Shopping Behaviour Analysis Dashboard")
st.markdown(
    "Interactive dashboard customized from a Streamlit Gallery template to analyze customer shopping behaviour."
)

st.markdown("---")

# ---------------- KPI Section (Template-style summary) ----------------
total_purchase = filtered_df["Purchase Amount (USD)"].sum()
avg_purchase = filtered_df["Purchase Amount (USD)"].mean()

male_count = filtered_df[filtered_df["Gender"] == "Male"].shape[0]
female_count = filtered_df[filtered_df["Gender"] == "Female"].shape[0]

with st.container():
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Purchase Amount", f"${total_purchase:,.2f}")
    col2.metric("Average Purchase Value", f"${avg_purchase:,.2f}")
    col3.metric("Male Purchases", male_count)
    col4.metric("Female Purchases", female_count)

st.markdown("---")

# ---------------- Tabs ----------------
tab1, tab2, tab3 = st.tabs(
    ["Category Analysis", "Age Trends", "Spending Behaviour"]
)

# ---------------- Tab 1: Bar Chart ----------------
with tab1:
    st.subheader("Purchase Distribution by Category")

    category_counts = filtered_df["Category"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))
    category_counts.plot(kind="bar", ax=ax)
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Number of Purchases")
    ax.set_title("Purchases by Category")
    ax.tick_params(axis="x", rotation=30)

    st.pyplot(fig)

    st.markdown(
        "This bar chart highlights customer preferences across different product categories."
    )

# ---------------- Tab 2: Line Chart ----------------
with tab2:
    st.subheader("Average Purchase Amount by Age")

    age_trend = filtered_df.groupby("Age")["Purchase Amount (USD)"].mean()

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(age_trend.index, age_trend.values, marker="o")
    ax.set_xlabel("Age")
    ax.set_ylabel("Average Purchase Amount (USD)")
    ax.set_title("Purchase Trend by Age")

    st.pyplot(fig)

    st.markdown(
        "The line chart shows how average spending changes across different age groups."
    )

# ---------------- Tab 3: Scatter Plot ----------------
with tab3:
    st.subheader("Age vs Purchase Amount by Gender")

    fig, ax = plt.subplots(figsize=(6, 4))

    male = filtered_df[filtered_df["Gender"] == "Male"]
    female = filtered_df[filtered_df["Gender"] == "Female"]

    ax.scatter(male["Age"], male["Purchase Amount (USD)"], label="Male", alpha=0.6)
    ax.scatter(female["Age"], female["Purchase Amount (USD)"], label="Female", alpha=0.6)

    ax.set_xlabel("Age")
    ax.set_ylabel("Purchase Amount (USD)")
    ax.set_title("Spending Behaviour by Age and Gender")
    ax.legend()

    st.pyplot(fig)

    st.markdown(
        "This scatter plot compares spending behaviour between male and female customers."
    )

# ---------------- Data View ----------------
with st.expander("View Filtered Dataset"):
    st.dataframe(filtered_df)
