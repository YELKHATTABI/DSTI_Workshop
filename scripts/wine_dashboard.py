import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.graph_objs as go

file_path = "/Users/yelkhattabi/DSTI_Workshop/datasets/winequality-red.csv"


@st.cache
def load_data():
    df = pd.read_csv(file_path)
    return df



redwine = load_data()

st.header("Raw Dta")


corr = redwine.corr()


st.header("Correlation")
trace = go.Heatmap(z=corr.values,
                  x=corr.index.values,
                  y=corr.columns.values)

st.plotly_chart([trace])