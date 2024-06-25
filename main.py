import streamlit as st
import joblib


# ## Normalization
mm_scaler = joblib.load('mm_scaler.joblib')

st.title('Rainfall Prediction use Regression Model')

reg = joblib.load('regression_model.joblib')


## functions
def preprocess(X):
    return mm_scaler.transform(X)

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

def calc_rainfall(model, scaler, args = [0, 0, 0, 0]):
    args = scaler.transform([args])
    s1, s2, s3, s4 = model.coef_
    vi1, vi2, vi3, vi4 = args[0]
    return ( (s1*vi1) + (s2*vi2) + (s3*vi3) + (s4*vi4) ) + model.intercept_

def predict_rainfall(min_humidity, avg_humidity, max_humidity, n_rainy_day):
    
    prediction = calc_rainfall(model=reg, scaler=mm_scaler, args=[min_humidity, avg_humidity, max_humidity, n_rainy_day])
    class_pred = classify_rainfal(prediction)
    return {'class':class_pred, 'val':round(prediction, 2)}


## data flow
with st.form('rainfall_prediction_form'):
    st.subheader('Masukkan data (independent variable)', divider='rainbow')
    n_rainy_day = st.slider(label="Jumlah hari hujan", min_value=1, max_value=7, value=None, step=1)
    min_humidity = st.slider(label='Kelembaban minimum', min_value=35, max_value=57, value=None, step=1)
    avg_humidity = st.slider(label='Kelembaban rata-rata', min_value=69, max_value=82, value=None, step=1)
    max_humidity = st.slider(label='Kelembaban maksimum', min_value=92, max_value=99, value=None, step=1)
    
    prediction = predict_rainfall(min_humidity, avg_humidity, max_humidity, n_rainy_day)
    
    submit = st.form_submit_button('Predict Rainfall')

if submit:
    st.subheader('Hasil prediksi (dependent variable)', divider='rainbow')
    st.write('Prediksi hujan adalah: ', prediction['class'], 'dengan intensitas: ', prediction['val'])