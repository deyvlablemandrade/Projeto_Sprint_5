import pandas as pd
import plotly.express as px
import streamlit as st 

car_data = pd.read_csv(r'C:\Users\User\Documents\Curso_Python_Independente\TripleTen\Projeto_Sprint_5\vehicles.csv') # lendo os dados

# Criar cabeçalho principal
st.header('Dashboard de Análise de Veículos Usados')

hist_button = st.button('Criar histograma') # criar um botão de histograma

if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")
        
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

graf_button = st.button('Criar gráfico') # criar um botão para gráfico

if graf_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um gráfico de disperção para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão
    st.plotly_chart(fig, use_container_width=True) # exibindo
