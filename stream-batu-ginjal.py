import pickle
import numpy as np
import streamlit as st

#load save model
model = pickle.load(open('penyakit_batu_ginjal.sav', 'rb'))

#judul web
st.title('Prediksi Batu Ginjal Berdasarkan Analisa Urin')


col1, col2,  = st.columns(2)

st.text ('Renaldi Al Anshari , 191351075')
with col1 :
    gravity = st.number_input('Berat Jenis Urin')
with col2 :
    ph = st.number_input('PH urin')
with col1 :
    osmo = st.number_input('Osmolalitas Urin')
with col2 :
    cond = st.number_input('Konduktivitas Urin')
with col1 :
    urea = st.number_input('Konsentrasi Ureum Dalam Urin')
with col2 :
    calc = st.number_input('Konsentrasi Kalsium Dalam Urin')

# code for prediction
kidney_stone_diagnosis =''

# membuat tombol prediksi 
if st.button('Prediksi Batu Ginjal Berdasarkan Analisis Urin'):
    kidney_stone_prediction = model.predict([[gravity, ph, osmo, cond, urea, calc]])

    if (kidney_stone_prediction[0]==1):
        kidney_stone_diagnosis = 'Pasien Terdeteksi Adanya Batu Ginjal'
    else :
        kidney_stone_diagnosis = 'Pasien Tidak Terdeteksi Adanya Batu Ginjal'
st.success(kidney_stone_diagnosis)