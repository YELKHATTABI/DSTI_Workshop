import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash("Dashboard", external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
file_path = "C:/Users/dsti0/DSTI_Workshop/datasets/processed_retail_dataset.csv"

def load_data(file_path_link):
    """
    """
    processed_df = pd.read_csv(file_path_link,index_col="InvoiceDate")
    processed_df.index = pd.to_datetime(processed_df.index)
    return processed_df


data = load_data(file_path)

agg_retail = data.resample("M").agg({"Total_value":"sum","InvoiceNo":"count"})
fig = px.line(agg_retail, y="Total_value",hover_data=["InvoiceNo"])


app.layout = html.Div(
    children=[
        html.H1(
            id="title",
            children='Retail data analysis'),
        
        dcc.Graph(
            id='graph',
            figure=fig,
        ),
        dcc.DatePickerSingle(
            id='start_date',
            min_date_allowed=data.index.min(),
            max_date_allowed=data.index.max(),
            date=data.index.min()
        ),
        dcc.DatePickerSingle(
            id='end_date',
            min_date_allowed=data.index.min(),
            max_date_allowed=data.index.max(),
            date=data.index.max()
        ),
        dcc.RadioItems(
            id="precision",
            options=[
                {'label': 'Month', 'value': "M"},
                {'label': 'Day', 'value': "D"},
            ],
            value="M"
        )  
])

@app.callback(
    Output('graph','figure'),
    [Input('precision','value'),
    Input('start_date','date'),
    Input('end_date','date')]
)
def update_graph(precision,start_date,end_date):    
    agg_retail = data.resample(precision).agg({"Total_value":"sum","InvoiceNo":"count"})
    fig = px.line(agg_retail.loc[start_date:end_date], y="Total_value",hover_data=["InvoiceNo"])

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
