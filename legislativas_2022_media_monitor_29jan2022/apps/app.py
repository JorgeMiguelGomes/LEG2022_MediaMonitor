# -*- coding: utf-8 -*-

# Full Dashboard --- WORK IN PROGRESS

import time
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import Input, Output, dcc, html


# Data treatment

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

pie_color_map = {"Angry": "#EB9486", "Love": "#CAE7B9"}


# START APP -----------------------------------------------------

app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)

app.layout = dbc.Container(
    [
        # First Row
        dbc.Row(
            [
                dbc.Col(
                    html.Hr(
                        style={
                            "borderWidth": "2vh",
                            "width": "100%",
                            "borderColor": "#CAE7B9",
                            "opacity": "unset",
                        }
                    ),
                    width={"size": 2},
                ),
                dbc.Col(
                    html.Hr(
                        style={
                            "borderWidth": "2vh",
                            "width": "100%",
                            "borderColor": "#F3DE8A",
                            "opacity": "unset",
                        }
                    ),
                    width={"size": 2},
                ),
                dbc.Col(
                    html.Hr(
                        style={
                            "borderWidth": "2vh",
                            "width": "100%",
                            "borderColor": "#EB9486",
                            "opacity": "unset",
                        }
                    ),
                    width={"size": 2},
                ),
                dbc.Col(
                    html.Hr(
                        style={
                            "borderWidth": "2vh",
                            "width": "100%",
                            "borderColor": "#7E7F9A",
                            "opacity": "unset",
                        }
                    ),
                    width={"size": 2},
                ),
                dbc.Col(
                    html.Hr(
                        style={
                            "borderWidth": "2vh",
                            "width": "100%",
                            "borderColor": "#97A7B3",
                            "opacity": "unset",
                        }
                    ),
                    width={"size": 2},
                ),
            ],
            className="g-0",
        ),  # end of first row
        # Second Row
        dbc.Row(
            [  # you have to create a children's array to have more than one column in a row
                dbc.Col(
                    html.H3("Legislativas 2022 Media Monitor"),
                    width={"size": 6, "offset": 0},
                ),  # First Column
                dbc.Col(
                    html.H4("Data from CrowdTangle", style={"color": "#7E7F9A"}),
                    width={"size": 5, "offset": 0},
                ),  # Second Column
            ],  # Close Children of first Row
        ),  # end of second row
        # Third Row
        dbc.Row(
            [
                dbc.Col(
                    html.H5("Observing Media Trends"), width={"size": 3, "offset": 0}
                ),  # second row
                dbc.Col(
                    html.H5("Made with Plotly Dash", style={"color": "#97A7B3"}),
                    width={"size": 5, "offset": 3},
                ),
            ],
        ),  # end of third row
        # Fourth Row
        dbc.Row(
            dbc.Col(
                html.Hr(
                    style={
                        "borderWidth": "0.5vh",
                        "width": "100%",
                        "borderColor": "#F3DE8A",
                        "opacity": "unset",
                    }
                ),
                width={"size": 10, "offset": 0},
            ),
        ),
        # Fith Row - TABS
        dbc.Tabs(
            [
                dbc.Tab(
                    label="About",
                    tab_id="method",
                    label_style={"color": "#CAE7B9"},
                    tab_style={"background-color": "#97A7B3"},
                    active_label_style={"background-color": "#080808"},
                ),
                dbc.Tab(
                    label="Metrics by Totals",
                    tab_id="totals",
                    label_style={"color": "#F3DE8A"},
                    tab_style={"background-color": "#7E7F9A"},
                    active_label_style={"background-color": "#080808"},
                ),
                dbc.Tab(
                    label="Stacked Analysis",
                    tab_id="stacked",
                    label_style={"color": "#EB9486"},
                    tab_style={"background-color": "#F3DE8A"},
                    active_label_style={"background-color": "#080808"},
                ),
                dbc.Tab(
                    label="Love vs Angry",
                    tab_id="love_angry",
                    label_style={"color": "#7E7F9A"},
                    tab_style={"background-color": "#EB9486"},
                    active_label_style={"background-color": "#080808"},
                ),
                dbc.Tab(
                    label="Conclusions",
                    tab_id="conclusions",
                    label_style={"color": "#97A7B3"},
                    tab_style={"background-color": "#F3DE8A"},
                    active_label_style={"background-color": "#080808"},
                ),
            ],
            id="tabs",
            active_tab="method",  # this is the tab that will be active when the user comes to the website
        ),  # end of tabs
        html.Div(id="tab-content", className="p-5"),
    ]
)


# Callbacks

# Totals CallBack and Graph


@app.callback(
    Output(component_id="graph_totals", component_property="figure"),
    [Input(component_id="dropdown_total", component_property="value")],
)
def build_graph_total(column_chosen):
    dff = df.reset_index().sort_values(["Total Interactions"], ascending=False)
    fig = px.bar(
        dff,
        x="Page Name",
        y=column_chosen,
        color="candidato",
        color_discrete_map=candidate_color_map,
        template="plotly_white",
        labels={
        "Page Name":"Media Outlets", column_chosen:"AMOUNT OF REACTIONS", "candidato":"CANDIDATES"},
        custom_data=[dff["candidato"]],
    )

    fig.update_traces(hoverinfo="none", hovertemplate=None)

    fig.update_traces(
        hovertemplate="<br>".join(
            [
                "<b>LEG2022</b>",
                "Period: 30DEZ2021 - 29JAN20222",
                "<b>CANDIDATE: %{customdata[0]}</b>",
                "Media Outlet: %{x}",
                "Total Amount: <b>%{y}</b>",
            ],
        ),
    )
    fig.update_layout(hoverlabel_bgcolor="black")

    return fig


# Stacked Call Back and Graph


@app.callback(
    Output(component_id="graph_totals_stacked", component_property="figure"),
    [Input(component_id="dropdown_total_stacked", component_property="value")],
)
def build_graph_total_stacked(column_chosen):
    dff = df
    fig_stacked = px.bar(
        dff,
        x="Page Name",
        y=column_chosen,
        color="candidato",
        color_discrete_map=candidate_color_map,
        template="plotly_white",
    )
    return fig_stacked


# Pie Chart for Candidate and Media Outlets


@app.callback(
    Output(component_id="graph_shares_comments", component_property="figure"),
    Output(component_id="graph_individuals", component_property="figure"),
    Input(component_id="dropdown_media_outlet", component_property="value"),
    Input(component_id="dropdown_candidates", component_property="value"),
)
def build_graphs(column_chosen, candidato_filter):

    # Data Treatment
    dff = df
    totals_sentiment = dff.groupby(["candidato"])[["Love", "Angry"]].sum().reset_index()
    totals_sentiment_melt = pd.melt(totals_sentiment, id_vars="candidato")
    totals_sentiment_melt = totals_sentiment_melt[
        totals_sentiment_melt["candidato"] == candidato_filter
    ]

    # Data Treatment
    dff_m = df[df["candidato"] == candidato_filter]
    totals_sentiment_media = (
        dff_m.groupby(["Page Name"])[["Love", "Angry"]].sum().reset_index()
    )
    totals_sentiment_media_melt = pd.melt(totals_sentiment_media, id_vars="Page Name")
    totals_sentiment_media_melt = totals_sentiment_media_melt[
        totals_sentiment_media_melt["Page Name"] == column_chosen
    ]

    # Pie Charts

    fig_candidates = px.pie(
        totals_sentiment_media_melt,
        names="variable",
        values="value",
        hole=0.5,
        color="variable",
        color_discrete_map=pie_color_map,
    )
    fig_media = px.pie(
        totals_sentiment_melt,
        names="variable",
        values="value",
        hole=0.6,
        color="variable",
        color_discrete_map=pie_color_map,
    )

    return fig_candidates, fig_media


# TABS CALLBACKS -------------------------------------


@app.callback(Output("tab-content", "children"), [Input("tabs", "active_tab")])
def switch_tab(at):
    # TAB 01
    if at == "method":
        tab1_content = dbc.Row(
            [
                dbc.Col(
                    dcc.Markdown(
                        """

### INTRODUCTION

This dashboard shows a quantitative analysis of the mentions that each main candidate, to the Portuguese Legisilative elections had on Facebook, by a set of chosen media outlets.

**Only the title of the Facebook post was filtered**



### DATASETS 

**Raw Datasets can be found [here](https://github.com/JorgeMiguelGomes/LEG2022_MediaMonitor/tree/main/legislativas_2022_media_monitor_29jan2022/legislativas_2022_media_monitor_29jan2022_raw_data)**

**Full raw dataset can be found [here](https://github.com/JorgeMiguelGomes/LEG2022_MediaMonitor/tree/main/legislativas_2022_media_monitor_29jan2022/data_products)**

These datasets can be used under a [**Creatve Commons License 4.0 BY-SA-NC**](https://creativecommons.org/licenses/by-nc-sa/4.0/)

When using **Crowdtangle** datasets please observe the mandatory references you should make in your work, [**that can be found here**](https://help.crowdtangle.com/en/articles/4558716-understanding-and-citing-crowdtangle-data)

### OBJECTIVE 

Monitor, quantitatively, how many times media outlets in Portugal mention each candidate, in their titles posted to social media, during the pre-electoral and electoral campaign for the 2022 elections

### METHODOLOGY

1.  Search Crowdtangle for every candidate’s respective keywords
2.  Export to .csv
3.  Import and treat .csv using Python Scripts 
4.  Generate Graphics
5.  Analyze Data







                    """
                    ),
                ),
            ],
        )

        return tab1_content

    # TAB 02
    elif at == "totals":

        tab2_content = (
            dbc.Row(
                [
                    dbc.Col(
                        # DROPDOWN TAB 2
                        dcc.Dropdown(
                            id="dropdown_total",
                            options=[
                                {
                                    "label": "Total Interactions",
                                    "value": "Total Interactions",
                                },
                                {"label": "Total Likes", "value": "Likes"},
                                {"label": "Total Comments", "value": "Comments"},
                                {"label": "Total Shares", "value": "Shares"},
                                {"label": "Total Love", "value": "Love"},
                                {"label": "Total Angry", "value": "Angry"},
                            ],
                            optionHeight=35,
                            value="Total Interactions",
                            disabled=False,
                            multi=False,
                            searchable=True,
                            search_value="",
                            placeholder="Please select...",
                            clearable=True,
                            style={"width": "50"},
                        ),
                    ),
                    # GRAPH TAB 2
                    dbc.Row(
                        dbc.Col(dcc.Graph(id="graph_totals")),
                    ),
                ],
            ),
        )

        return tab2_content

    # TAB 03
    elif at == "stacked":
        tab3_content = (
            dbc.Row(
                [
                    dbc.Col(
                        # DROPDOWN TAB 03
                        dcc.Dropdown(
                            id="dropdown_total_stacked",
                            options=[
                                {
                                    "label": "Total Interactions",
                                    "value": "Total Interactions_Percentages",
                                },
                                {"label": "Total Likes", "value": "Likes_Percentages"},
                                {
                                    "label": "Total Comments",
                                    "value": "Comments_Percentages",
                                },
                                {
                                    "label": "Total Shares",
                                    "value": "Shares_Percentages",
                                },
                                {"label": "Total Love", "value": "Love_Percentages"},
                                {"label": "Total Angry", "value": "Angry_Percentages"},
                            ],
                            optionHeight=35,
                            value="Total Interactions_Percentages",
                            disabled=False,
                            multi=False,
                            searchable=True,
                            search_value="",
                            placeholder="Please select...",
                            clearable=True,
                            style={"width": "100%"},
                        ),
                    ),
                    # GRAPH TAB 3
                    dbc.Row(
                        dbc.Col(dcc.Graph(id="graph_totals_stacked")),
                    ),
                ],
            ),
        )

        return tab3_content

    # TAB 04
    elif at == "love_angry":
        tab4_content = (
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Dropdown(
                                id="dropdown_candidates",
                                options=[
                                    {"label": i, "value": i}
                                    for i in df_individuals_melt.candidato.unique()
                                ],
                                optionHeight=35,  # height/space between dropdown options
                                value="António Costa",  # dropdown value selected automatically when page loads
                                disabled=False,  # disable dropdown value selection
                                multi=False,  # allow multiple dropdown values to be selected
                                searchable=True,  # allow user-searching of dropdown values
                                search_value="",  # remembers the value searched in dropdown
                                placeholder="Please select...",  # gray, default text shown when no option is selected
                                clearable=True,  # allow user to removes the selected value
                                style={
                                    "width": "100%"
                                },  # use dictionary to define CSS styles of your dropdown
                                # className='select_box',               #activate separate CSS document in assets folder
                                # persistence=True,                     #remembers dropdown value. Used with persistence_type
                                # persistence_type='memory'             #remembers dropdown value selected until...
                            ),
                            dbc.Col(
                                dcc.Graph(id="graph_individuals"),
                            ),
                        ],
                        width={"size": 6, "offset": 0},
                    ),
                    dbc.Col(
                        [
                            dcc.Dropdown(
                                id="dropdown_media_outlet",
                                options=[
                                    {"label": i, "value": i}
                                    for i in df["Page Name"].unique()
                                ],
                                optionHeight=35,  # height/space between dropdown options
                                value="Agência Lusa",  # dropdown value selected automatically when page loads
                                disabled=False,  # disable dropdown value selection
                                multi=False,  # allow multiple dropdown values to be selected
                                searchable=True,  # allow user-searching of dropdown values
                                search_value="",  # remembers the value searched in dropdown
                                placeholder="Please select...",  # gray, default text shown when no option is selected
                                clearable=True,  # allow user to removes the selected value
                                style={
                                    "width": "100%"
                                },  # use dictionary to define CSS styles of your dropdown
                                # className='select_box',               #activate separate CSS document in assets folder
                                # persistence=True,                     #remembers dropdown value. Used with persistence_type
                                # persistence_type='memory'             #remembers dropdown value selected until...
                            ),
                            dbc.Col(
                                dcc.Graph(id="graph_shares_comments"),
                            ),
                        ],
                        width={"size": 6, "offset": 0},
                    ),
                ],
            ),
        )

        return tab4_content

    # TAB 05
    elif at == "conclusions":
        tab5_content = html.P("Blah Blab Blaah ")
        return tab5_content

    # Error Message
    return html.P("This shouldn't ever be displayed...")


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)


# APP END
