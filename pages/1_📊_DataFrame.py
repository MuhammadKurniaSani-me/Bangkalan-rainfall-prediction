import streamlit as st
import pandas as pd

# load data
DATA_URL = 'https://raw.githubusercontent.com/MuhammadKurniaSani-me/datasets/main/real-dataset/only%20data-prediksi-curah-hujan-bangkalan%203.csv'

def classify_rainfal(intensity):
    if (intensity <= 2):
        return "Hujan ringan"

    if (intensity > 2 and intensity <= 15):
        return "Hujan sedang"

    if (intensity > 15 and intensity <= 30):
        return "Hujan lebat"

    if (intensity > 30 and intensity <= 60):
        return "Hujan deras"

    return "Hujan sangat deras"

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
        data[r_intense] = data[r_intense].apply(classify_rainfal)
    return data

st.set_page_config(page_title="DataFrame", page_icon="📊")
st.sidebar.header("DataFrame")
st.markdown("# DataFrame")

data = load_data(DATA_URL)

st.dataframe(data)