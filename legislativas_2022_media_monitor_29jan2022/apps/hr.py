# -*- coding: utf-8 -*-

# --------- Import libraries -----------
import dash 
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px 
import dash_bootstrap_components as dbc

# 
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
	html.Hr(style={'borderWidth': "5vh", "width": "100%", "borderColor": "#AB87FF","opacity": "unset"}),
	],
)

if __name__ == "__main__":
	app.run_server(debug=True)