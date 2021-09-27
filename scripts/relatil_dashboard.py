from pkg_resources import load_entry_point
import streamlit as st
import pandas as pd
import plotly.express as px

file_path = "C:/Users/dsti0/DSTI_Workshop/datasets/processed_retail_dataset.csv"

@st.cache
def load_data(file_path_link):
    """
    """
    processed_df = pd.read_csv(file_path_link,index_col="InvoiceDate")
    processed_df.index = pd.to_datetime(processed_df.index)
    return processed_df


data = load_data(file_path)

st.title("Retail dataset analysis")

st.header("Analysis of total value")

st.write("Hello world!")

start_date = st.date_input(
    label='start date',
    value=data.index.min(),
    min_value=data.index.min(),
    max_value=data.index.max()
    )
end_date = st.date_input(
    label='end date',
    value=data.index.max(),
    min_value=data.index.min(),
    max_value=data.index.max()
    )

precision =st.radio(
    label="Precision",
    options=["M","D"]
)

agg_retail = data.resample(precision).agg({"Total_value":"sum","InvoiceNo":"count"})
fig = px.line(agg_retail.loc[start_date:end_date], y="Total_value",hover_data=["InvoiceNo"])

st.plotly_chart(fig)
