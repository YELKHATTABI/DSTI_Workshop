import streamlit as st
import pandas as pd
import numpy as np

st.title('California Housing')

@st.cache
def load_data():
    df = pd.read_csv("/Users/yelkhattabi/DSTI_Workshop/datasets/housing.csv")
    df = df.drop(index=df[df.total_bedrooms.isna()].index)
    return df

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('Map')
st.map(data)