import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Analisis Socioeconómico - ENAHO 2023')

@st.cache_data

def load_data():
    df = pd.read_csv('enaho_2023.csv', encoding='latin-1', sep=None, engine='python', nrows=500)
    df.columns = df.columns.str.strip()
    return df

try:
    df_enaho = load_data()
    
    if st.button('Construir Histograma de Edades'):
        st.write('Distribución de edades en la muestra')

        if 'edad' in df_enaho.columns:
            fig = px.histogram(df_enaho, x="edad")
            st.plotly_chart(fig, use_container_width=True)

        else:
            st.error(f"No se encontró la columna 'edad'. Columnas disponibles: {list(df_enaho.columns)}")

    if st.button('Construir Gráfico de Dispersión'):
        if 'horas' in df_enaho.columns and 'ingreso' in df_enaho.columns:
            st.write('Relación entre Horas e Ingreso')
            fig = px.scatter(df_enaho, x="horas", y="ingreso")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("No se econtraron las columnas neesarias para el gráfico de dispersión.")

except Exception as e:
    st.error(f"Error al cargar el archivo: {e}")
    
    