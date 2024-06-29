from sklearn.feature_selection import r_regression
import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

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


st.set_page_config(page_title="Evaluation")
st.sidebar.header("Evaluation")
st.markdown("# Evaluation")

data = load_data(DATA_URL)

mm_scaler = MinMaxScaler()

X = data.drop(columns=["jumlah-curah-hujan (mm)"])
y = data['jumlah-curah-hujan (mm)']

X_normalized_mm = mm_scaler.fit_transform(X)
col_corr_mm = r_regression(X_normalized_mm, y)
corr_mm = {col: corr for col, corr in zip(X.columns, col_corr_mm)}
best_features_5_mm = {}
for col, corr in corr_mm.items():
    if corr > 0.5:
        best_features_5_mm[col] = corr

selected_df_mm_5 = pd.DataFrame(X_normalized_mm, columns=X.columns).loc[:, [
    feature for feature in best_features_5_mm.keys()]]

X_train_selected_5_mm, X_test_selected_5_mm, y_train_selected_5_mm, y_test_selected_5_mm = train_test_split(
    selected_df_mm_5, y, random_state=42)

model_selected_5_mm = LinearRegression()

model_selected_5_mm.fit(X_train_selected_5_mm, y_train_selected_5_mm)

y_pred_selected_5_mm = model_selected_5_mm.predict(X_test_selected_5_mm)

X_normalized_mm = mm_scaler.fit_transform(X)

mse_selected_5_mm = mean_squared_error(
    y_test_selected_5_mm, y_pred_selected_5_mm, squared=False)

st.header('Evaluasi MSE', divider='rainbow')
st.write("MSE & Standard Normalized:", mse_selected_5_mm)
