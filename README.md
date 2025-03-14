# Bike Sharing Dashboard

Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis pola penyewaan sepeda berdasarkan dataset historis.  

- **EDA diperbarui** dengan insight yang lebih rinci dan sistematis.
- **Dashboard interaktif** dengan fitur filter berdasarkan hari.
- **Visualisasi yang lebih jelas** tentang hubungan suhu dengan jumlah penyewaan.

## Struktur Proyek
```
submission_jupyter/
│   ├───dashboard/
│   │   ├───dashboard.py  # File utama Streamlit
│   │   ├───main_data.csv  # Dataset yang digunakan
│   ├───data/
│   │   ├───day.csv  # Dataset asli
│   │   ├───hour.csv
│   ├───notebook.ipynb  # Notebook untuk analisis awal
│   ├───README.md  # Dokumentasi proyek
│   ├───requirements.txt  # Daftar dependencies
│   └───url.txt
```

## Instalasi & Menjalankan Dashboard
### 1️ **Clone Repository**
```bash
git clone https://github.com/username/repository-name.git
cd repository-name
```
### 2️ **Install Dependencies**
Pastikan sudah menginstal Python. Kemudian jalankan:
```bash
pip install -r requirements.txt
```
### 3️ **Jalankan Aplikasi Streamlit**
```bash
streamlit run dashboard/dashboard.py
```
Akses dashboard melalui **http://localhost:8501**.

## Deployment ke Streamlit Cloud
Untuk meng-host di **Streamlit Cloud**:
1. Upload repository ke **GitHub**.
2. Buka [Streamlit Cloud](https://share.streamlit.io/).
3. Pilih repository & file `dashboard/dashboard.py`.
4. Klik **Deploy**.


