import pandas as pd
import numpy as np
import pickle


df = pd.read_csv("Cleaned.csv")
X = pd.read_csv("X.csv")

# Load the saved model from file
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

# categorical columns:
cat_columns = ['Manufacturer', 'Model', 'Category', 'Leather interior', 'Fuel type',
       'Gear box type', 'Drive wheels', 'Doors', 'Wheel']


map_list = [{} for _ in range(len(cat_columns))] 

for i in range(len(cat_columns)):
    for j in range (len(df[cat_columns[i]])):
        map_list[i][df[cat_columns[i]][j]] = X[cat_columns[i]][j]



def PREPROCESS (Levy, Manufacturer, Model, Category, Leather_interior, Fuel_type, Engine_volume, Mileage,
                     Cylinders, Gear_box_type, Drive_wheels, Doors, Wheel, Airbags, Age):

    Manufacturer = map_list[0][Manufacturer]

    Model = map_list[1][Model]


    Category = map_list[2][Category]


    Leather_interior = map_list[3][Leather_interior]

    Fuel_type = map_list[4][Fuel_type]


    Gear_box_type = map_list[5][Gear_box_type]

    Drive_wheels = map_list[6][Drive_wheels]

    Doors = map_list[7][Doors]

    Wheel = map_list[8][Wheel]

    return [Levy, Manufacturer, Model, Category, Leather_interior, Fuel_type, Engine_volume, Mileage,
                     Cylinders, Gear_box_type, Drive_wheels, Doors, Wheel, Airbags, Age]


def PREDICT(List):
    x = np.zeros(len(X.columns))
    counter = 0
    for i in List:
        x[counter] = i
        counter+=1
        
    return model.predict([x])[0]