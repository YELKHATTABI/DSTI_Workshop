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
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig1 = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig2 = px.bar(df, x="Fruit", y="Amount", color="City", barmode="stack")


app.layout = html.Div(
    children=[
        html.H1(
            id="title",
            children='Hello Dash!!!'),
        html.Div(
            id="paragraph",
            children='''
            Dash: A web application framework for Python.
            '''
        ),
        dcc.Graph(
            id='graph',
            figure=fig1,
        ),
        dcc.RadioItems(
            id="choice",
            options=[
                {'label': 'Stacked Fig', 'value': 1},
                {'label': 'Group Fig', 'value': 2},
            ],
            value=1
        )  
])

@app.callback(
    Output('graph','figure'),
    Input('choice','value')

)
def update_graph(choice_value):
    if choice_value == 1:
        updated_fig = fig1
    elif choice_value ==2:
        updated_fig = fig2

    return updated_fig





if __name__ == '__main__':
    app.run_server(debug=True)