import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


DATA_URL = (
    "C:\\Users\\gamboa\\PycharmProjects\\jgamboaData\\dataset\\Motor_Vehicle_Collisions_-_Crashes.csv"
)

st.markdown("<h1 style='text-align: center; color: black;'>Geographic Data</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: black;'>Dataset of Vehicle Collisions</h1>", unsafe_allow_html=True)
st.markdown('<style>h2{color: blue; text-align:center;}</style>', unsafe_allow_html=True)


@st.cache(persist=True)
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[["CRASH DATE", "CRASH TIME"]])
    data.dropna(subset=["LATITUDE", "LONGITUDE"], inplace=True)
    data.drop(data[data['LATITUDE'] == 0].index, inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash date_crash time': 'date/time'}, inplace=True)
    data.rename(columns={'number of persons injured': 'injured_persons'}, inplace=True)
    data.rename(columns={'number of pedestrians injured': 'injured_pedestrians'}, inplace=True)
    data.rename(columns={'number of cyclist injured': 'injured_cyclists'}, inplace=True)
    data.rename(columns={'number of motorist injured': 'injured_motorists'}, inplace=True)
    return data

data = load_data(600000)

st.sidebar.header("jgamboa")
st.header("Number of Injured Person x Collision")

st.sidebar.header("Filter Parameters")
st.sidebar.header("where are most people injure?")
#injured_people = st.sidebar.slider("# Person injured in Collisions", 0, 9)
injured_people = st.sidebar.number_input("Number Person injured in Collisions", step=1, min_value=0, max_value=9, value=1)
st.map(data.query('injured_persons > @injured_people')[["latitude", "longitude"]].dropna(how="any"))
