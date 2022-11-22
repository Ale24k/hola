import streamlit as st 
import pandas as pd
import numpy as np
import gdown
import os


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



#SELECCIÓN DE CRITERIOS
criterio = data['CLASIFICACION_DEF'].unique()
option_criterio = st.selectbox('Lista de fallecidos según el criterio ' , criterio)

#if option_criterio == '
#GRAFICO DE BARRAS DE LOS CRITERIOS
df_criterios = df[df['CLASIFICACION_DEF'] == option_criterio]
df_crit = df_criterios.CLASIFICACION_DEF.value_counts()
st.write('Distribución por criterios')
st.bar_chart(df_crit)


#if option_criterio == 'Criterio SINADEF':
    #B = df[['CLASIFICACION_DEF']].groupby('CLASIFICACION_DEF').count()
