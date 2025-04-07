import streamlit as st
import pandas as pd
import pydeck as pdk
import altair as alt
import functions as functions

st.cache_data.clear() # Si tienes problemas con la cache, descomenta esta linea


# Configuración inicial del proyecto
st.set_page_config(
    page_title="Project Cargatron",
    page_icon=":zap:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Carga y procesamiento de datos
df = pd.read_csv("data/red_recarga_acceso_publico_2024.csv", sep= ";")

st.header(f"My Streamlit APP - Project Cargatron")


uploaded_file = st.sidebar.file_uploader(
    "Choose a file (must be ';' separated)", type=["csv"]
    )

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, sep=";")
        st.balloons()
    except:
        st.write("File format not recognized.")

# Sistema de navegación
option = st.sidebar.selectbox(
    "Page:",
    ("Home", "Map", "Charts"),
)

# Lógica para navegar entre las páginas
if option == "Home":
    functions.home(df)
elif option=="Map":
    functions.map(df)
elif option=="Charts":
    functions.charts(df)