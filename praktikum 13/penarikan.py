import streamlit as st 

st.title("Halaman Penarikan")

# Formulir Input
with st.form("Penarikan"):
    Nama = st.text_input("Nama")
    Jumlah = st.number_input("Jumlah (Rp.)", min_value=0, step=1000)
    Tanggal = st.date_input("Tanggal")
    Waktu = st.time_input("Waktu")
    sumbit_button =st.form_submit_button(label="Penarikan")
    
    if sumbit_button and Jumlah >= 50000 :
        st.session_state['total_semua'].append({
            'Tipe' : 'Penarikan', 
            'Jumlah' : Jumlah
        })
        st.success("Penarikan Uang Berhasil")
    else:
        st.error("Penarikan Gagal")