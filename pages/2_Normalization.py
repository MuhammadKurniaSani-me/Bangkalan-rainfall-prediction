import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# load data
DATA_URL = 'https://raw.githubusercontent.com/MuhammadKurniaSani-me/datasets/main/real-dataset/only%20data-prediksi-curah-hujan-bangkalan%203.csv'

@st.cache_data
def load_data(url=DATA_URL):
    data = pd.read_csv(url, sep=';')
    for month in data['bulan']:
        data['bulan'].replace(month, month.split('/')[0], inplace=True)
    data.set_index('bulan', inplace=True)
    data.replace(0, pd.NA, inplace=True)
    data = data.replace(',', '.', regex=True)
    for r_intense in data.loc[:, ['jumlah-curah-hujan (mm)']]:
        data[r_intense] = data[r_intense].astype(float)
    return data

st.set_page_config(page_title="Normalization")
st.sidebar.header("Normalization")
st.markdown("# Normalization")

data = load_data(DATA_URL)

mm_scaler = MinMaxScaler()

X = data.drop(columns=["jumlah-curah-hujan (mm)"])
y = data['jumlah-curah-hujan (mm)']

X_normalized_mm = mm_scaler.fit_transform(X)

data_norm = pd.DataFrame(X_normalized_mm, columns=X.columns, index=data.index)

st.dataframe(data_norm)