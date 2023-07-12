import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("./Cleaned.csv")

num_col = df.drop(['ID','Prod. year'],axis = 1).select_dtypes(exclude="object").columns
cat_col =  df.select_dtypes(include="object").columns
# Define the colors you want to use
colors = ['#c32148', '#00563B', '#00325B','#948ce8']

def show_EDA(df):
    st.header("Exploratory Data Analysis")
    uni,bi = st.tabs(['Univariate Analysis','Bivariate Analysis'])
    uni.subheader("1. Numeric culomns:")
    num_col = df.drop(['ID','Prod. year'],axis = 1).select_dtypes(exclude="object").columns
    #cat_col =  df.select_dtypes(include="object").columns
    for col in num_col:
        if (col == 'Airbags')|(col == 'Cylinders'):
            # Sample data
            x = df[col].value_counts()[:10].index
            y = df[col].value_counts()[:10]

            # Create bar plot
            fig = go.Figure(data=go.Bar(x=x, y=y,marker=dict(color='#c32148')))
            title = col 
            fig.update_layout(title=title,height=400, width=800,)

            # Show the plot
            uni.plotly_chart(fig)
        
        else:
        
            
           # Create a histogram
            fig = go.Figure(data=[go.Histogram(x=df[col],opacity=0.7,marker=dict(color='#c32148'))])

            # Customize the layout
            fig.update_layout(title=col, xaxis_title='Value', yaxis_title='Frequency',barmode='overlay',
                bargap=0.1,height=400, width=800)


            uni.plotly_chart(fig)

    uni.markdown(
    """
    ### Insights from numeric columns:
    - The majority of levies fall within the range of 0 to 24 USD.
    - The 2-litre engine volume exhibits the highest frequency among the sample.
    - The longest mileage recorded lies between 0 and 2500 KM.
    - The most common cylinder number is 4, followed by 12.
    - The most common number of Airbags is 4, followed by 12.
    - The most common car age ranges between 9 and 11 years.
    """
    ,unsafe_allow_html=True)

    uni.subheader("_"*60)
    uni.subheader("2. Categorical columns:")
    # ____________________________________________________________
    for col in cat_col:
    
        if (col == 'Manufacturer')|(col == 'Model'):
            # Sample data
            x = df[col].value_counts()[:10].index
            y = df[col].value_counts()[:10]

            # Create bar plot
            fig = go.Figure(data=go.Bar(x=x, y=y,marker=dict(color='#c32148')))
            title = col
            fig.update_layout(title=title,height=400, width=800)


            # Show the plot
            uni.plotly_chart(fig)
            
        else:
            labels = df[col].value_counts().index
            values = df[col].value_counts()

            fig = go.Figure(data=[go.Pie(labels=labels, values=values,marker=dict(colors=colors))])

            # Set the title of the chart
            fig.update_layout(title=col,height=600, width=800)

            # Display the chart
            uni.plotly_chart(fig)

    uni.markdown(
    """
    ### Insight from categorical columns:
    - Hyundai manifactures the largest number of cars
    - Sonata is the most manufactured car model
    - Sedan is the most common car category
    - Most cars have leather interior
    - Most cars support petrol as a fuel source
    - Most cars have an automatic gear box type
    - Most cars support front drive wheels
    - Most cars have 4 doors
    - Most cars have left-wheel
    - Most common car colors are black, white and silver
    """
    ,unsafe_allow_html=True)
    



#_____________________________________________________________________
    # Create treemap
    car_model_list = ['Manufacturer', 'Model', 'Category']
    fig = px.treemap(df, path=car_model_list, values='Price',color_discrete_sequence=colors,)
    # Show the plot
    bi.subheader("Tree map:")
    bi.plotly_chart(fig)

    for col in cat_col:
   
        if col not in car_model_list:

            values = df.groupby(col).mean()['Price']
            labels =values.index

            fig = go.Figure(data=[go.Pie(labels=labels, values=values,marker=dict(colors=colors))])

            # Set the title of the chart
            fig.update_layout(title=col,height=600, width=800)

            # Display the chart
            bi.plotly_chart(fig)
    
    bi.markdown(
        """
        ### Insights:
    - Cars with leather interior have higher price
    - Cars with diesel, hybrid and plug-in hybrid have higher prices than the others
    - Cars with triptonic gear boxs have higher prices
    - Cars with front and 4x4 drive wheels have higher prices
    - Cars with larger number of doors have higher prices
    - Left wheel cars have higher prices
    - Color does not have great effect on car price
       """
        ,unsafe_allow_html=True)
