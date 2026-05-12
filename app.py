import streamlit as st
import screening_tab as sc

# KUNCI TAMPILAN FULLSCREEN
st.set_page_config(page_title="Compliance System v1.1", layout="wide")

def main():
    # Simulasi Session State (Seolah-olah sudah login)
    if 'user' not in st.session_state:
        st.session_state['user'] = "imanmuhamad9@gmail.com"
        st.session_state['role'] = "Admin"

    # Header Aplikasi
    c1, c2 = st.columns([10, 2])
    c1.title("🏦 Screening System")
    if c2.button("Keluar"):
        st.write("Logout Berhasil")

    st.divider()

    # Panggil fungsi dari file screening_tab.py
    # 1. Ambil data
    db_p, stats, total = sc.fetch_all_data()
    
    # 2. Jalankan tampilan screening
    sc.run_pencarian(st.session_state['user'], db_p, True)

if __name__ == "__main__":
    main()
