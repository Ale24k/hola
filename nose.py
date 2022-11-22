import streamlit as st 
import pandas as pd
import numpy as np
import gdown
import os


st.title('Fallecidos por COVID19')

st.title('Fallecidos por COVID19')


# id = 1dSRlbtutz10Lgb4wiYPcWaK3w5QMUH8O
@st.experimental_memo
def download_data():
    #https://drive.google.com/uc?id=YOURFILEID\
    url = "https://drive.google.com/uc?id=1dSRlbtutz10Lgb4wiYPcWaK3w5QMUH8O"
    output = 'data.csv'
    gdown.download(url,output,quiet = False)

download_data()
#vamos a sacar el primer millon de datos:
data = pd.read_csv('data.csv', sep = ';', parse_dates= ['FECHA_CORTE', 'FECHA_FALLECIMIENTO'])
st.dataframe(data.head(20))
#df = df.drop(columns = ["FECHA_CORTE","FECHA_FALLECIMIENTO","EDAD_DECLARADA","SEXO", "CLASIFICACION_DEF", "DEPARTAMENTO", "PROVINCIA", "DISTRITO", "UBIGEO", "UUID"])



criterio = data['CLASIFICACION_DEF'].unique()
option_criterio = st.selectbox('Lista de fallecidos según el criterio ' , criterio)
if opcion_criterio == 'Criterio SINADEF':
    op1 = df["CLASIFICACION_DEF"].value_counts()
    op2 = df["CLASIFICACION_DEF"].value_counts()
