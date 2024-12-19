import streamlit as st 

st.title("halaman Tabungan")

# Formulir Input
with st.form("Menabung"):
    Nama = st.text_input("Nama")
    Jumlah = st.number_input("Jumlah (Rp.)", min_value=0)
    Tanggal = st.date_input("Tanggal")
    Waktu = st.time_input("Waktu")
    sumbit_button =st.form_submit_button(label="Menabung")
    
    if sumbit_button and Jumlah >= 50000 :
        st.session_state['total_semua'].append({
            'Tipe' : 'Menabung', 
            'Jumlah' : Jumlah
        })
        st.success("Menabung Berhasil")
    else:
        st.error("Menabung Gagal")