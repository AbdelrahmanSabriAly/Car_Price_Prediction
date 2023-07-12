import streamlit as st
import plotly.express as px
import pandas as pd
import pickle
from utils.Predict_pipeline import PREPROCESS,PREDICT

# Load the saved model from file
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

df = pd.read_csv("./Cleaned.csv")
X = pd.read_csv("./X.csv")

def get_results(input):

    result = PREDICT(input)
    st.success(f"Your car's price is {result.round(2):,.0F} USD")


def APP():
    st.title("Car Price Prediction :car:")
    Levy = st.slider('Enter Levy', 0, 30000)	

    Manufacturer = st.selectbox('Pick a Manufacturer', df['Manufacturer'].unique())

    Model = st.selectbox('Pick a Model', df['Model'].unique())

    Category = st.selectbox('Pick a Category', df['Category'].unique())

    Leather_interior = st.radio('Does the car have a leather interior?', ['Yes', 'No'])

    Fuel_type = st.selectbox('Pick a Fuel type', df['Fuel type'].unique())

    Engine_volume = st.slider('Enter Engine volume', min_value=0.0, max_value=9.0, step=0.1)
    Mileage = st.slider('Enter Mileage in KM', 0, 30000)	
    Cylinders = st.slider('Enter number of cylinders', 1, 14)	

    Gear_box_type = st.radio('Enter Gear box type', df['Gear box type'].unique())
    Drive_wheels = st.radio('Specify the Drive wheels', df['Drive wheels'].unique())

    Doors = st.radio('Specify the number of Doors', df['Doors'].unique())

    Wheel = st.radio('Specify the Wheel', df['Wheel'].unique())

    Airbags = st.slider('Enter number of Airbags', 0, 20)	
    Age = st.slider('Enter the Age of the car in years', 1, 35)	


    preprocessed_input = PREPROCESS (Levy, Manufacturer, Model, Category, Leather_interior, Fuel_type, Engine_volume, Mileage,
                     Cylinders, Gear_box_type, Drive_wheels, Doors, Wheel, Airbags, Age)
    
    
    #st.button("Predict!", on_click=get_results(preprocessed_input))
    button_clicked = st.button("Predict!")

    if button_clicked:
        get_results(preprocessed_input)




