import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
file_path = "dashboard/main_data.csv"  # Pastikan path sesuai dengan lokasi file di repo
df = pd.read_csv(file_path)

# Dashboard Title
st.title("Bike Sharing Dashboard")

# Pilihan interaktif: Pilih Hari
selected_day = st.selectbox("Pilih Hari:", df['weekday'].unique())

# Filter data berdasarkan hari yang dipilih
filtered_data = df[df['weekday'] == selected_day]

# Tampilkan Data Preview
st.write("## Data Preview")
st.dataframe(filtered_data)

# Visualisasi 1: Pengaruh Suhu terhadap Penyewaan
st.write("## Pengaruh Suhu terhadap Penyewaan Sepeda")
fig1 = px.scatter(filtered_data, x='temp', y='cnt', title='Hubungan Suhu dan Jumlah Penyewaan')
st.plotly_chart(fig1)

# Visualisasi 2: Total Penyewaan Berdasarkan Musim
st.write("## Total Penyewaan Berdasarkan Musim")
fig2 = px.bar(df, x='season', y='cnt', title='Total Penyewaan Sepeda Berdasarkan Musim')
st.plotly_chart(fig2)
