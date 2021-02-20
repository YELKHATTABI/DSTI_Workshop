import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash("California Housing dashboard",external_stylesheets=[dbc.themes.BOOTSTRAP])

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}




df = pd.read_csv("/Users/yelkhattabi/DSTI_Workshop/datasets/processed_housing.csv")

fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_data=None, zoom=5, height=600,color="population")
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})



median_house_value_range_slider = dcc.RangeSlider(
        id='median_house_value_range_slider',
        min=0,
        max=int(df.median_house_value.max()),
        marks={
            k:f"{str(k)[:-3]}k" for k in range(25000,500002,50000)
        },
        value=[0, int(df.median_house_value.max())]
    )

# map_color_dropdow = 


side_bar = html.Div(
    [
        html.H2("Parameters", className="display-4"),
        html.Hr(),
        html.H3("Map color selector"),
        dcc.Dropdown(
            id='map_color',
            options=[
                {'label': 'Housing age', 'value': 'housing_median_age'},
                {'label': 'Total rooms', 'value': 'total_rooms'},
                {'label': 'Total bedrooms', 'value': 'total_bedrooms'},
                {'label': 'Population', 'value': 'population'},
                {'label': 'Number of households', 'value': 'households'},
                {'label': 'Median income', 'value': 'median_income'},
                {'label': 'Median house value', 'value': 'median_house_value'},
                {'label': 'Ocean proximity', 'value': 'ocean_proximity'},
            ],
            value='median_house_value'
        ), 
    ],
    style=SIDEBAR_STYLE,
)

app.layout = dbc.Container(
                    [
                    html.H1("California Housing Dashboard"),
                    dbc.Row(
                        [
                            dbc.Col(
                                [side_bar,],
                                md=3,
                            ),
                            dbc.Col([
                                dbc.Row([
                                    dbc.Col(
                                        [
                                            dcc.Graph(
                                                id="map",
                                                figure=fig
                                            ),
                                            median_house_value_range_slider,
                                        ]
                                        ,md=7
                                    ),
                                    dbc.Col([
                                        dbc.Row(html.Div("graph")),
                                        dbc.Row(html.Div("graph")),
                                    ],md=3),
                                ]),
                                dbc.Row(html.Div("graph")),
                            ]),
                        ]
                    ),],
                    fluid=True,
            )


@app.callback(
    Output("map","figure"),
    [
        Input("median_house_value_range_slider","value"),
        Input("map_color","value")]
)
def update_map(min_max_range,color):
    temp_df = df[(df.median_house_value>min_max_range[0]) & (df.median_house_value<min_max_range[1])]
    fig = px.scatter_mapbox(temp_df, lat="latitude", lon="longitude", hover_data=None,
                        zoom=5, height=600,color=color)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig



if __name__=="__main__":
    app.run_server(debug=True)

