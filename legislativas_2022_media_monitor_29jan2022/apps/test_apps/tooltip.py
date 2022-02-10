# -*- coding: utf-8 -*-

# --------- Import libraries -----------
import dash
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# -------------- Data Operations ------------------

df = pd.read_csv(
    "https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/data_products/legislativas_2022_final_dataset_percentages.csv"
)

df_individuals = pd.read_csv(
    "https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/data_products/legislativas_2022_all_candidates_filtered.csv"
)

df_individuals = df_individuals.drop(columns=["Unnamed: 0"])
df_indivuduals = df_individuals.drop(columns=["Post Created Date"])
df_individuals_melt = pd.melt(df_individuals, id_vars=["candidato", "Page Name"])

# -------------- Styling -------------------------------------------


candidate_color_map = {
    "Rui Rio": "#FF6400",
    "Francisco Rodrigues dos Santos": "#0B6AB1",
    "António Costa": "#F1A0A2",
    "Rui Tavares": "#00CE8C",
    "Catarina Martins": "#C90635",
    "Jerónimo de Sousa": "#025298",
    "André Ventura": "#202056",
    "João Cotrim Figueiredo": "#00AEEF",
    "Inês Sousa-Real": "#00798E",
}

pie_color_map = {"Angry": "#666666", "Love": "#5F468F"}


# Define chart


fig = px.bar(
    df,
    x="candidato",
    y="Love",
    color="candidato",
    template="plotly_white",
    color_discrete_map=candidate_color_map,
)

fig.update_traces(hoverinfo="none", hovertemplate=None)


# --------------- Define App -------------


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


dff = df

totals = (
    dff.groupby(["candidato"])[["Love", "Angry"]]
    .sum()
    .reset_index()
    .sort_values(["Love", "Angry"], ascending=False)
)
totals_melt = pd.melt(totals, id_vars="candidato")

fig = px.bar(
    totals_melt,
    x="variable",
    y="value",
    color="candidato",
    template="plotly_white",
    barmode="group",
    labels=dict(x="REACTION TYPES", y="AMOUNT OF REACTIONS", color="CANDIDATOS"),
    color_discrete_map=candidate_color_map,
    custom_data=[totals_melt["candidato"]],
)

fig.update_traces(hoverinfo="none", hovertemplate=None)

fig.update_layout(xaxis=dict(title="CANDIDATOS"), yaxis=dict(title="LOVE"))

fig.update_traces(
    hovertemplate="<br>".join(
        [
            "<b>CANDIDATE: %{customdata[0]}</b>",
            "Reaction Type: %{x}",
            "Reaction Amount: <b>%{y}</b>",
        ],
    ),
)

fig.update_layout(hoverlabel_bgcolor="black")

app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.Div(
            children="""
        Dash: A web application framework for your data.
    """
        ),
        dcc.Graph(id="example-graph", figure=fig),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
