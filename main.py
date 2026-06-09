import streamlit as st
import pandas as pd
import plotly.express as px
# Dados de exemplo
df = pd.DataFrame({
"Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
"Vendas": [120, 145, 98, 200, 175, 230],
"Clientes": [40, 55, 35, 80, 70, 95],
})



st.title("Dashboar de Teste")
st.header("Olá, meu nome é Ariana")
st.write("Esse é um texto simples")

st.dataframe(df, use_container_width =True)