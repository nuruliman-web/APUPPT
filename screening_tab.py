import streamlit as st
import pandas as pd

def fetch_all_data():
    """Simulasi ambil data. Ganti dengan logika database asli abang nanti."""
    # Data dummy untuk memastikan fitur pencarian jalan
    data = {
        "Nama": ["Budi Santoso", "Siti Aminah", "Andi Wijaya"],
        "NIK": ["123456", "654321", "987654"],
        "Status": ["Clear", "Watchlist", "Clear"]
    }
    df = pd.DataFrame(data)
    stats = {"Total": len(df)}
    return df, stats, len(df)

def run_pencarian(user_email, db_p, is_admin):
    st.header("🔍 Screening Nasabah")
    st.write(f"Selamat datang, **{user_email}**")

    # Layout kolom untuk input pencarian
    col1, col2 = st.columns([3, 1])
    
    with col1:
        search_query = st.text_input("Masukkan Nama atau NIK Nasabah:", placeholder="Contoh: Budi Santoso")
    
    with col2:
        st.write("##") # Spacer
        search_button = st.button("Cari Nasabah", use_container_width=True)

    if search_button:
        if search_query:
            # Logika pencarian sederhana
            results = db_p[
                db_p['Nama'].str.contains(search_query, case=False, na=False) | 
                db_p['NIK'].str.contains(search_query, na=False)
            ]
            
            if not results.empty:
                st.success(f"Ditemukan {len(results)} hasil.")
                st.dataframe(results, use_container_width=True)
                
                # Fitur tambahan jika dia Admin
                if is_admin:
                    st.info("💡 Mode Admin: Anda memiliki akses untuk mengunduh laporan ini.")
                    csv = results.to_csv(index=False).encode('utf-8')
                    st.download_button("Unduh Hasil (CSV)", data=csv, file_name="hasil_screening.csv", mime="text/csv")
            else:
                st.warning("Nasabah tidak ditemukan di database.")
        else:
            st.error("Silakan masukkan kata kunci pencarian.")

    st.divider()
    st.subheader("📊 Statistik Database Terkini")
    st.info(f"Jumlah data tersimpan saat ini: {len(db_p)} entitas.")
