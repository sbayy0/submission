import streamlit as st
import pandas as pd

# Load Data
df = pd.read_csv("dashboard/main_data.csv")

# Dashboard Title
st.title("Bike Sharing Dashboard")

# Show Data
st.write("## Data Preview")
st.dataframe(df)
