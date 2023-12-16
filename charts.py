# charts.py

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def generate_sample_data():
    # Replace this with fetching data from your database or any other data source
    num_days = 365
    data = {
        'Date': pd.date_range(start='2022-01-01', periods=num_days),
        'Sessions': np.random.randint(30, 120, size=num_days)
    }
    return pd.DataFrame(data)

def display_bar_chart(data):
    st.subheader("Nombre de séances pour chaque plage horaire")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Date', data=data, ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

def display_line_chart(data):
    st.subheader("Nombre de séances programmées en fonction du jour de la semaine")
    data['Day_of_Week'] = data['Date'].dt.day_name()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='Day_of_Week', data=data, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    st.pyplot(fig)

def app():
    st.title("Graphiques sur les séances programmées")

    # Fetch data from your database or any other data source
    df = generate_sample_data()

    # Display bar chart
    display_bar_chart(df)

    # Display line chart
    display_line_chart(df)
