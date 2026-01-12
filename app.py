import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Analisis Socioeconómico - ENAHO 2023')

@st.cache_data

def load_data():
    return pd.read_csv('enaho_2023.csv', encoding='latin-1', nrows=500)

df_enaho = load_data()

st.write('Muestra de datos (Primeras 500 filas para optimización de carga).')

if st.button('Construir Histograma de Edades'):
    st.write('Distribución de edades en la muestra')
    fig = px.histogram(df_enaho, x="edad")
    st.plotly_chart(fig, use_container_width=True)

if st.button('Construir Gráfico ded Dispersión'):
    st.write('Relación entre Horas Trabajadas e Ingreso')
    fig = px.scatter(df_enaho, x="horas", y="ingreso")
    st.plotly_chart(fig, use_container_width=True)
    