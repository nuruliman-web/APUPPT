import streamlit as st
from kegiatan_tracker import run_kegiatan_tracker

# Konfigurasi Halaman
st.set_page_config(page_title="Screening & Compliance", layout="wide")

# Sidebar Navigasi
st.sidebar.title("Menu Utama")
menu = st.sidebar.radio("Pilih Fitur:", ["Cross-Check Database", "Log Kegiatan"])

if menu == "Cross-Check Database":
    st.title("🔍 Cross-Check Database Pemerintah")
    st.write("Bandingkan data internal dengan database pemerintah (Upload Excel).")
    
    # Fitur upload dan logika pembanding diletakkan di sini
    import pandas as pd
    from thefuzz import fuzz

    col1, col2 = st.columns(2)
    with col1:
        file_int = st.file_uploader("Upload Data Internal (Excel)", type=['xlsx'])
    with col2:
        file_gov = st.file_uploader("Upload Database Pemerintah (Excel)", type=['xlsx'])

    if file_int and file_gov:
        df_internal = pd.read_excel(file_int)
        dict_gov = pd.read_excel(file_gov, sheet_name=None)
        
        threshold = st.sidebar.slider("Ambang Kemiripan Nama (%)", 50, 100, 80)
        
        st.subheader("Mapping Kolom Data Internal")
        cols = df_internal.columns.tolist()
        col_nama = st.selectbox("Pilih Kolom Nama", cols)
        col_nik = st.selectbox("Pilih Kolom NIK", cols)

        if st.button("🚀 Mulai Cross-Check"):
            for index, row in df_internal.iterrows():
                nama_target = str(row[col_nama]).lower().strip()
                nik_target = str(row[col_nik]).strip()
                
                for sheet_name, df_gov in dict_gov.items():
                    # Logika pencocokan sederhana
                    match = df_gov[df_gov.apply(lambda r: fuzz.token_sort_ratio(nama_target, str(r.iloc[0]).lower()) >= threshold, axis=1)]
                    if not match.empty:
                        st.success(f"Match ditemukan di sheet {sheet_name} untuk: {nama_target}")
                        st.dataframe(match)

elif menu == "Log Kegiatan":
    run_kegiatan_tracker()
