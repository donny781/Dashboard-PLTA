import streamlit as st
import pandas as pd
from graphviz import Digraph

st.set_page_config(page_title="Dashboard Struktur Organisasi PLTA", layout="wide")

st.title("📊 Dashboard Struktur Organisasi Unit PLTA")

# DATA PEGAWAI
data = {
    "Jabatan": [
        "Manager Unit",
        "Supervisor Operasi",
        "Supervisor Pemeliharaan",
        "Supervisor Administrasi",
        "Operator PLTA",
        "Teknisi Pemeliharaan",
        "Staff Keuangan",
        "Staff SDM"
    ],
    "Nama": [
        "Budi Santoso",
        "Andi Wijaya",
        "Rudi Hartono",
        "Siti Aminah",
        "Dedi Saputra",
        "Agus Pratama",
        "Rina Marlina",
        "Tono Prasetyo"
    ]
}

df = pd.DataFrame(data)

st.subheader("Data Pegawai")
st.dataframe(df, use_container_width=True)

st.subheader("Diagram Struktur Organisasi")

# Membuat diagram
dot = Digraph()

# Node jabatan
dot.node('A', 'Manager Unit\nBudi Santoso')
dot.node('B', 'Supervisor Operasi\nAndi Wijaya')
dot.node('C', 'Supervisor Pemeliharaan\nRudi Hartono')
dot.node('D', 'Supervisor Administrasi\nSiti Aminah')
dot.node('E', 'Operator PLTA\nDedi Saputra')
dot.node('F', 'Teknisi\nAgus Pratama')
dot.node('G', 'Staff Keuangan\nRina Marlina')
dot.node('H', 'Staff SDM\nTono Prasetyo')

# Struktur hubungan
dot.edge('A', 'B')
dot.edge('A', 'C')
dot.edge('A', 'D')
dot.edge('B', 'E')
dot.edge('C', 'F')
dot.edge('D', 'G')
dot.edge('D', 'H')

st.graphviz_chart(dot)

st.subheader("Profil Pegawai")

pegawai = st.selectbox("Pilih Pegawai", df["Nama"])

profil = df[df["Nama"] == pegawai]

st.write("### Informasi Pegawai")
st.write(profil)
