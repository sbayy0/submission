import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
file_path = "dashboard/main_data.csv"  # Pastikan path sesuai dengan lokasi file di repo
df = pd.read_csv(file_path)

# Dashboard Title
st.title("Bike Sharing Dashboard")

# Pilihan Interaktif: Pilih Hari
all_days_option = "Semua Hari"
days_options = [all_days_option] + sorted(df['weekday'].unique().tolist())

selected_day = st.selectbox("Pilih Hari:", days_options)

# Filter Data
if selected_day == all_days_option:
    filtered_data = df  # Tampilkan semua data
else:
    filtered_data = df[df['weekday'] == selected_day]

# Tampilkan Data Preview
st.write("## Data Preview")
st.dataframe(filtered_data)

# Visualisasi 1: Pola Penyewaan Sepeda Berdasarkan Hari
st.write("## Pola Penyewaan Sepeda Berdasarkan Hari")
fig1 = px.bar(df, x='weekday', y='cnt', title='Jumlah Penyewaan Sepeda per Hari', color='cnt')
st.plotly_chart(fig1)

# Visualisasi 2: Pengaruh Suhu terhadap Penyewaan
st.write("## Pengaruh Suhu terhadap Penyewaan Sepeda")
fig2 = px.scatter(filtered_data, x='temp', y='cnt', title='Hubungan Suhu dan Jumlah Penyewaan', color='cnt')
st.plotly_chart(fig2)

# Visualisasi 3: Total Penyewaan Berdasarkan Musim (Interaktif)
st.write("## Total Penyewaan Berdasarkan Musim")
season_option = st.radio("Pilih Musim:", df['season'].unique(), horizontal=True)
season_filtered = df[df['season'] == season_option]

fig3 = px.bar(season_filtered, x='season', y='cnt', title='Total Penyewaan Sepeda Berdasarkan Musim', color='cnt')
st.plotly_chart(fig3)
