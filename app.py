import pandas as pd
import plotly.express as px
import streamlit as st 

car_data = pd.read_csv('vehicles.csv') # lendo os dados

# Criar cabeçalho principal
st.title('Dashboard Deyvla')  # Título grande
st.header('Análise de Veículos Usados')

st.write('Bem-vindo ao dashboard de análise de veículos usados! Aqui você pode explorar os dados de anúncios de vendas de carros usados e visualizar diferentes gráficos para entender melhor o mercado.')  

st.markdown('## Seção de Gráficos')  # Cabeçalho médio
st.write('Nesta seção, você pode criar diferentes tipos de gráficos para analisar os dados de anúncios de vendas de carros usados. Sinta-se à vontade para explorar os dados!')
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
