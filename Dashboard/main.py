# main.py
import streamlit as st
import pandas as pd
from app.utils import load_data, plot_boxplot, generate_summary_table

# Streamlit app configuration
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")
st.title("Solar Radiation Insights Dashboard 🌞")
st.markdown("Visualizing solar radiation data for Benin, Sierra Leone, and Togo.")

# Define the data paths
data_files = {
    "Benin": "data/benin_clean.csv",
    "Sierra Leone": "data/sierra_clean.csv",
    "Togo": "data/togo_clean.csv",
}

# Load the data
datasets = load_data(data_files)

# Ensure the datasets were loaded properly
if datasets is None:
    st.error("Failed to load data. Please ensure data files exist in the 'data/' directory.")
else:
    # Sidebar for user filters
    st.sidebar.header("Filter Options")
    selected_countries = st.sidebar.multiselect(
        "Select Countries", options=list(data_files.keys()), default=list(data_files.keys())
    )
    selected_metric = st.sidebar.radio("Select Metric", ["GHI", "DNI", "DHI"], index=0)

    # Filter the data based on selections
    filtered_df = pd.concat([datasets[country] for country in selected_countries], ignore_index=True)

    # Boxplot for the selected metric
    st.subheader(f"Distribution of {selected_metric} by Country")
    st.pyplot(plot_boxplot(filtered_df, selected_metric))

    # Summary statistics table
    st.subheader("Summary Statistics Table")
    st.dataframe(generate_summary_table(filtered_df))

    # Ranking by average GHI
    st.subheader("Ranking of Countries by Average GHI")
    average_ghi = filtered_df.groupby("Country")["GHI"].mean().sort_values(ascending=False)
    st.bar_chart(average_ghi)