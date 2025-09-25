import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados do CSV
df = pd.read_csv('vehicles.csv')

# Cabeçalho principal
st.header("Análise de Veículos nos EUA")

# Botão para gerar histograma
if st.button("Gerar Histograma de Preços"):
    fig = px.histogram(df, x="price")  # ajuste o nome da coluna conforme seu CSV
    st.plotly_chart(fig)

# Cabeçalho para outra seção
st.header("Gráfico de Dispersão")

# Botão para gerar gráfico de dispersão
if st.button("Gerar Gráfico de Dispersão"):
    fig2 = px.scatter(df, x="model_year", y="price", color="model")
    st.plotly_chart(fig2)