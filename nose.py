import streamlit as st 
import pandas as pd
import numpy as np
import gdown

st.title('Fallecidos por COVID19')

#Criterio virolÃ³gico = Criterio virológico
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



option = st.selectbox(
    ' Lista de fallecidos según el criterio ',
    ('Criterio virológico', 'Criterio serológico', 'Criterio radiológico', 'Criterio nexo epidemiológico', 
     'Criterio investigación epidemiológica', 'Criterio clínico', 'Criterio SINADEF'))
if option == 'Criterio virológico':
    op1 = df["CLASIFICACION_DEF"].value_counts()
    b = (
        Bar()
        .add_xaxis(["FEMENINO", "MASCULINO"])
        .add_yaxis(
            "Casos positivos por sexo", [int(tipo2),int(tipo3)]
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=" "
            ),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    st_pyecharts(b)
    
    
