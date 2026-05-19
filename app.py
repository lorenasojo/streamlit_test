import pandas as pd
import plotly.express as px
import streamlit as st

# título
st.header('Análisis de vehículos usados')

# leer datos
car_data = pd.read_csv('vehicles_us.csv')

# histograma
st.write('Histograma de precios de vehículos')

fig_hist = px.histogram(car_data, x='price')

st.plotly_chart(fig_hist)

# dispersión
st.write('Relación entre kilometraje y precio')

fig_scatter = px.scatter(
    car_data,
    x='odometer',
    y='price'
)

st.plotly_chart(fig_scatter)
