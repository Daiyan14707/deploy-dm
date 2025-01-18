import streamlit as st
import pickle
import pandas as pd
# Judul Aplikasi
st.title('Prediksi Harga Rumah')
with open('model_house_price.pkl', 'rb') as f:
    model = pickle.load(f)

# Periksa tipe dari model
print(f"Model type: {type(model)}")
# Input form
lb = st.number_input('Luas Bangunan (m²)', min_value=0)
lt = st.number_input('Luas Tanah (m²)', min_value=0)
kt = st.number_input('Jumlah Kamar Tidur', min_value=0)
km = st.number_input('Jumlah Kamar Mandi', min_value=0)
grs = st.number_input("Jumlah Garasi: ", min_value=0)

# Prediksi ketika tombol ditekan
if st.button('Prediksi Harga'):
    if grs < 0:
        print("Jumlah Garasi tidak bisa negatif. Menggunakan nilai default 0.")
        grs = 0  # Menggunakan 0 jika input negatif
    # Membuat array input untuk model
    new_data = pd.DataFrame([[lb, lt, kt, km, grs]])

    # Pastikan bahwa prediksi dilakukan dengan model yang benar
    predicted_price = model.predict(new_data)
    input_data = [[lb, lt, kt, km, grs]]
    
    st.write(f'Prediksi harga rumah: Rp {predicted_price[0]:,.2f}')