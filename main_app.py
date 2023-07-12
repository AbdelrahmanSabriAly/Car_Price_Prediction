import streamlit as st
from streamlit_option_menu import option_menu  # Importing a custom option menu widget
import plotly.express as px
import pandas as pd
import pickle
from utils.app import APP
from utils.EDA import show_EDA
from utils.contact import show_contact
from utils.about import ABOUT

# Load the saved model from file
with open('random_forest_model.pkl', 'rb') as file:
    model = pickle.load(file)

df = pd.read_csv("./Cleaned.csv")
X = pd.read_csv("utils\X.csv")
st.set_page_config(page_title = "Car Price Prediction", page_icon=":car:",layout='wide')


# CSS style to hide Streamlit's main menu and footer
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer{visibility: hidden;}
</style>
"""

# Applying the CSS style to hide Streamlit's main menu and footer
st.markdown(hide_st_style, unsafe_allow_html=True)


with st.sidebar:
    # Creating a sidebar menu with different options
    choose = option_menu("Main Menu", [ "About","App", "EDA", "Contact"],
                         icons=['house','app-indicator', "bar-chart",'person lines fill'],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#0E1117"},
        "icon": {"color": "#c32148", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

# ------------------- Exploratory Data Analysis -------------------------
if choose == 'About':
    ABOUT()
# ------------------- Exploratory Data Analysis -------------------------
elif choose == "EDA":
    show_EDA(df)

# ----------------------------- App ----------------------------------
elif choose == "App":
    APP()


# -------------------------- Contact ----------------------------------
else:
    show_contact()
