import streamlit as st

def ABOUT():
    st.subheader("Car price prediction application based on the following dataset:")
    st.markdown("[Car Price Prediction Challenge](https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge)")
    st.markdown(
    """
    ### In this project:
    - The dataset is cleaned (missing values, duplicated values, columns data types and outliers ).
    - An exploratory data analysis is done (both univariate and bivariate analysis).
    - GridSearchCV is used to train multiple regression algorithms, fine tune them and find the best algorithm for the project.
    - Random forest achieved the highest score on the test data (81.2%)
    - Streamlit is used for deployment.

    """
    ,unsafe_allow_html=True)

    st.write("The link of the github repository is the following :")
    st.markdown("[GitHub Repo](https://github.com/AbdelrahmanSabriAly/Car_Price_Prediction.git)")
