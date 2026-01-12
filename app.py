import pandas as pd
import plotly.express as px
import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Analista de Datos - ENAHO 2023", layout="wide")

# Título
st.title('📊 Dashboard Dinámico de Indicadores Socioeconómicos')
st.markdown("### Fuente: Encuesta Nacional de Hogares (ENAHO 2023) - Perú")

# lectura de datos
@st.cache_data
def load_data():
    df = pd.read_csv('enaho_2023.csv', encoding='latin-1', sep=None, engine='python', nrows=1000)
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()

    # --- BARRA LATERAL PARA FILTROS DINÁMICOS ---
    st.sidebar.header("Panel de Control")
    st.sidebar.write("Use los filtros para actualizar los gráficos automáticamente.")
    
    # Filtro dinámico por Sexo (1=Hombre, 2=Mujer)
    lista_sexo = df['sexo'].unique()
    filtro_sexo = st.sidebar.multiselect("Filtrar por Género (1:H, 2:M):", 
                                        options=lista_sexo, 
                                        default=lista_sexo)
    
    # Aplicar filtro
    df_filtrado = df[df['sexo'].isin(filtro_sexo)]

    # --- DISEÑO EN COLUMNAS PARA LOS GRÁFICOS ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribución de Edades")
        if st.checkbox('Ver Histograma de Edades'):
            # Gráfico dinámico
            fig_hist = px.histogram(df_filtrado, x="edad", color="sexo",
                                   title="Frecuencia por Edad y Género",
                                   labels={'edad': 'Edad', 'sexo': 'Género'},
                                   color_discrete_sequence=px.colors.qualitative.Set2)
            st.plotly_chart(fig_hist, use_container_width=True)

    with col2:
        st.subheader("Relación Ingresos vs Trabajo")
        if st.checkbox('Ver Gráfico de Dispersión'):
            # Gráfico dinámico con línea de tendencia
            fig_scatter = px.scatter(df_filtrado, x="horas", y="ingreso", 
                                     color="sexo",
                                     title="Horas de Trabajo vs Ingreso Mensual",
                                     labels={'horas': 'Horas trabajadas', 'ingreso': 'Sueldo (S/.)'},
                                     trendline="ols") # Para añadir la línea de tendencia económica
            st.plotly_chart(fig_scatter, use_container_width=True)

except Exception as e:
    st.error(f"Error al cargar el Dashboard: {e}")

    