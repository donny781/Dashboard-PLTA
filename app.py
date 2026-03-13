import streamlit as st
import pandas as pd
from graphviz import Digraph

st.set_page_config(page_title="Dashboard Kepegawaian PLTA", layout="wide")

st.title("📊 Dashboard Kepegawaian Unit PLTA")

menu = st.sidebar.selectbox(
    "Menu",
    ["Dashboard", "Data Pegawai", "Struktur Organisasi", "Profil Pegawai"]
)

# Load Data
try:
    df = pd.read_excel("data_pegawai.xlsx")
except:
    st.warning("File data_pegawai.xlsx belum tersedia")
    df = pd.DataFrame(columns=["Nama","Jabatan","Unit","Status"])


# DASHBOARD
if menu == "Dashboard":

    st.subheader("Statistik Pegawai")

    col1,col2,col3 = st.columns(3)

    col1.metric("Jumlah Pegawai", len(df))
    col2.metric("Pegawai Tetap", len(df[df["Status"]=="Tetap"]))
    col3.metric("Pegawai Kontrak", len(df[df["Status"]=="Kontrak"]))


# DATA PEGAWAI
elif menu == "Data Pegawai":

    st.subheader("Data Nominatif Pegawai")

    st.dataframe(df, use_container_width=True)

    uploaded_file = st.file_uploader("Upload Data Excel")

    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.success("Data berhasil diupload")
        st.dataframe(df)


# STRUKTUR ORGANISASI
elif menu == "Struktur Organisasi":

    st.subheader("Diagram Struktur Organisasi")

    dot = Digraph()

    dot.node('A', 'Manager Unit')
    dot.node('B', 'Supervisor Operasi')
    dot.node('C', 'Supervisor Pemeliharaan')
    dot.node('D', 'Supervisor Administrasi')
    dot.node('E', 'Operator')
    dot.node('F', 'Teknisi')
    dot.node('G', 'Staff Keuangan')
    dot.node('H', 'Staff SDM')

    dot.edge('A','B')
    dot.edge('A','C')
    dot.edge('A','D')
    dot.edge('B','E')
    dot.edge('C','F')
    dot.edge('D','G')
    dot.edge('D','H')

    st.graphviz_chart(dot)


# PROFIL PEGAWAI
elif menu == "Profil Pegawai":

    st.subheader("Profil Pegawai")

    nama = st.selectbox("Pilih Nama Pegawai", df["Nama"])

    profil = df[df["Nama"] == nama]

    st.write("### Informasi Pegawai")
    st.table(profil)
