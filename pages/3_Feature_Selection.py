import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import r_regression

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

st.set_page_config(page_title="Feature Selection")
st.sidebar.header("Feature Selection")
st.markdown("# Feature Selection")

data = load_data(DATA_URL)

mm_scaler = MinMaxScaler()

X = data.drop(columns=["jumlah-curah-hujan (mm)"])
y = data['jumlah-curah-hujan (mm)']

X_normalized_mm = mm_scaler.fit_transform(X)

col_corr_mm = r_regression(X_normalized_mm, y)

corr_mm = {col:corr for col, corr in zip(X.columns, col_corr_mm)}

best_features_5_mm = {}
for col, corr in corr_mm.items():
    if corr > 0.5:
        best_features_5_mm[col] = corr
        
st.header('Feature terbaik', divider='rainbow')
st.markdown(
    """
    Nilai korelasi fitur yang lebih dari 0.5
"""
)
print('Nilai PCC dari kolom > 0.5')
for col, val in zip(best_features_5_mm.keys(), best_features_5_mm.values()):
    st.markdown(f' - {col} = {round(val, 2)}')