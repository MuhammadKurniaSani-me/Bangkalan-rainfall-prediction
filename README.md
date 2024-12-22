# Rainfall Intensity Prediction for Bangkalan, Indonesia

This project focuses on predicting rainfall intensity in Bangkalan, Indonesia, using historical weather data from the National Weather Station (BMKG).

**Try Yourself**
![here](https://bangkalan-rainfall-prediction.streamlit.app/?embed_options=show_toolbar,light_theme,show_colored_line,show_padding,disable_scrolling,show_footer,dark_theme)

**Data**

* **Source:** BMKG Bangkalan
* **Features:** [List of features used - e.g., Temperature, Humidity, Wind Speed, Pressure, etc.]

**Data Preprocessing**

* **Missing Value Imputation:** [Specify the method used - e.g., Mean imputation, Median imputation, KNN imputation]
* **Normalization:** Min-Max normalization (scaling values to a range between 0 and 1)
* **Feature Selection:** Pearson correlation to identify the most significant features for rainfall intensity prediction.

**Model**

* **Multiple Linear Regression:** A linear regression model is used to establish a relationship between the selected features and rainfall intensity.

**Prediction**

* **Data Splitting:** 80% of the data is used for training the model, and 20% is used for testing its performance.

**Evaluation**

* **Root Mean Squared Error (RMSE):** The RMSE metric is used to evaluate the model's accuracy in predicting rainfall intensity.

**Steps**

1. **Data Collection:** Acquire historical weather data from the BMKG Bangkalan.
2. **Data Preprocessing:** Clean and prepare the data for model training.
3. **Model Training:** Train the multiple linear regression model using the training data.
4. **Prediction:** Make predictions on the test data.
5. **Evaluation:** Evaluate the model's performance using the RMSE metric.

**Future Work**

* Explore other machine learning algorithms (e.g., Random Forest, Support Vector Regression, Neural Networks).
* Implement more advanced data preprocessing techniques (e.g., feature engineering, dimensionality reduction).
* Consider external factors that may influence rainfall (e.g., El Niño, La Niña).
* Develop a user-friendly interface for data input and prediction visualization.

**Preview**


![prediction-page](https://github.com/MuhammadKurniaSani-me/Bangkalan-rainfall-prediction/blob/1450b8cc7b363cb0d6a9b38f7ecf77d6f6f194f0/prediction-page.png)

---

![data-page](https://github.com/MuhammadKurniaSani-me/Bangkalan-rainfall-prediction/blob/1450b8cc7b363cb0d6a9b38f7ecf77d6f6f194f0/data-page.png)

---

![normalization-page](https://github.com/MuhammadKurniaSani-me/Bangkalan-rainfall-prediction/blob/1450b8cc7b363cb0d6a9b38f7ecf77d6f6f194f0/norm-data-page.png)

---

![feature-selection-page](https://github.com/MuhammadKurniaSani-me/Bangkalan-rainfall-prediction/blob/1450b8cc7b363cb0d6a9b38f7ecf77d6f6f194f0/features-selection-page.png)

---

![evaluation-page](https://github.com/MuhammadKurniaSani-me/Bangkalan-rainfall-prediction/blob/1450b8cc7b363cb0d6a9b38f7ecf77d6f6f194f0/evaluation-score-page.png)


**Disclaimer**

This project aims to provide a basic framework for rainfall intensity prediction. The accuracy of the predictions may vary depending on the quality and quantity of the data, as well as the complexity of the underlying weather patterns.
