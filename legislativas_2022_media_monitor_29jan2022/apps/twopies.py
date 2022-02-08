

# -*- coding: utf-8 -*-

# # Two Pie Charts 

import time
import dash
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash import Input, Output, dcc, html

# Data treatment 

df = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/data_products/legislativas_2022_final_dataset_percentages.csv')

df_individuals  = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/data_products/legislativas_2022_all_candidates_filtered.csv')

df_individuals = df_individuals.drop(columns=["Unnamed: 0"])
df_indivuduals = df_individuals.drop(columns=["Post Created Date"])
df_individuals_melt=pd.melt(df_individuals,id_vars=['candidato','Page Name'])


# Styling 

pie_color_map = {
    "Angry":"#EB9486",
    "Love":"#CAE7B9"
}

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP],suppress_callback_exceptions=True,
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
                )


app.layout = dbc.Container(
    [
        # First Row 
        dbc.Row(
            [
            dbc.Col(html.Hr(style={'borderWidth': "2vh", "width": "100%", "borderColor": "#CAE7B9","opacity": "unset"}),width={'size':2}),
            dbc.Col(html.Hr(style={'borderWidth': "2vh", "width": "100%", "borderColor": "#F3DE8A","opacity": "unset"}),width={'size':2}),
            dbc.Col(html.Hr(style={'borderWidth': "2vh", "width": "100%", "borderColor": "#EB9486","opacity": "unset"}),width={'size':2}),
            dbc.Col(html.Hr(style={'borderWidth': "2vh", "width": "100%", "borderColor": "#7E7F9A","opacity": "unset"}),width={'size':2}),
            dbc.Col(html.Hr(style={'borderWidth': "2vh", "width": "100%", "borderColor": "#97A7B3","opacity": "unset"}),width={'size':2}),
            ],className="g-0",
        ), # end of first row 


 		dbc.Tabs(
            [
                dbc.Tab(label="About", tab_id="method", label_style={"color": "#CAE7B9"},tab_style={'background-color': '#97A7B3'},active_label_style={"background-color":"#080808"}),      
                dbc.Tab(label="Metrics by Totals", tab_id="totals", label_style={"color": "#F3DE8A"},tab_style={'background-color': '#7E7F9A'}, active_label_style={"background-color":"#080808"}),
                dbc.Tab(label="Stacked Analysis", tab_id="stacked", label_style={"color": "#EB9486"},tab_style={'background-color': '#F3DE8A'}, active_label_style={"background-color":"#080808"}),
                dbc.Tab(label="Love vs Angry", tab_id="love_angry", label_style={"color": "#7E7F9A"},tab_style={'background-color': '#EB9486'}, active_label_style={"background-color":"#080808"}),
                dbc.Tab(label="Conclusions", tab_id="conclusions", label_style={"color": "#97A7B3"},tab_style={'background-color': '#F3DE8A'}, active_label_style={"background-color":"#080808"}),
            ],
            id="tabs",
            active_tab="love_angry", # this is the tab that will be active when the user comes to the website 
        ), # end of tabs 
        html.Div(id="tab-content", className="p-5"),
    ]
)


# Callbacks 

# Pie Chart for Candidates 

# @app.callback(
#     Output(component_id='graph_individuals', component_property='figure'),
#     [Input(component_id='dropdown_candidates', component_property='value')],
# )

# def build_graph_individuals(column_chosen):
#     dff = df
#     totals_sentiment = dff.groupby(['candidato'])[['Love','Angry']].sum().reset_index()
#     totals_sentiment_melt = pd.melt(totals_sentiment,id_vars="candidato")
#     totals_sentiment_melt = totals_sentiment_melt[totals_sentiment_melt['candidato'] == column_chosen]
#     fig_individuals = px.pie(totals_sentiment_melt,names="variable",values="value",hole=0.5, color="variable",color_discrete_map=pie_color_map)
#     candidato_filter = column_chosen
#     return fig_individuals

# Pie Chart for Media Outlets     

@app.callback(
    Output(component_id='graph_shares_comments', component_property='figure'),
    Output(component_id='graph_individuals', component_property='figure'),
    Input(component_id='dropdown_media_outlet', component_property='value'),
    Input(component_id='dropdown_candidates', component_property='value')
)

def build_graph_shares_comments(column_chosen):
    # Data Treatment 


    dff = df[['candidato'] == candidato_filter] # RETURNS ERROR "NameError: name 'candidato_filter' is not defined"
    total_shares_comments = dff.groupby(['Page Name'])[['Love','Angry']].sum().reset_index()
    total_shares_comments_melt = pd.melt(total_shares_comments,id_vars="Page Name")
    total_shares_comments_melt = total_shares_comments_melt[total_shares_comments_melt['Page Name'] == column_chosen] 
    # Pice Charts


    fig_individuals = px.pie(totals_sentiment_melt,names="variable",values="value",hole=0.5, color="variable",color_discrete_map=pie_color_map)
    fig_shares_comments = px.pie(total_shares_comments_melt,names="variable",values="value", color="variable",hole=0.4,color_discrete_map=pie_color_map, template='plotly_white')   
    return fig_shares_comments, fig_individuals



# TABS CALLBACKS -------------------------------------

@app.callback(Output("tab-content", "children"),
    [Input("tabs", "active_tab")])

def switch_tab(at):
    if at == "love_angry":
        tab4_content = dbc.Row(
                        [
                            dbc.Col(
                                [ 
                                dcc.Dropdown(
                                id='dropdown_candidates',
                                options=[{'label': i, 'value': i} for i in df_individuals_melt.candidato.unique()
                                    ],
                                    optionHeight=35,                        #height/space between dropdown options
                                    value='António Costa',             #dropdown value selected automatically when page loads
                                    disabled=False,                         #disable dropdown value selection
                                    multi=False,                            #allow multiple dropdown values to be selected
                                    searchable=True,                        #allow user-searching of dropdown values
                                    search_value='',                        #remembers the value searched in dropdown
                                    placeholder='Please select...',         #gray, default text shown when no option is selected
                                    clearable=True,                         #allow user to removes the selected value
                                    style={'width':"100%"},                 #use dictionary to define CSS styles of your dropdown
                                    # className='select_box',               #activate separate CSS document in assets folder
                                    # persistence=True,                     #remembers dropdown value. Used with persistence_type
                                    # persistence_type='memory'             #remembers dropdown value selected until...
                                    ),  
                                dbc.Col(
                                    dcc.Graph(id='graph_individuals'),
                                    ),
                                ],width={'size':6, 'offset':0}
                            ), 

                            dbc.Col(
                                [ 
                                dcc.Dropdown(
                                id='dropdown_media_outlet',
                                options=[{'label': i, 'value': i} for i in df['Page Name'].unique()
                                ],
                                optionHeight=35,                        #height/space between dropdown options
                                value='Agência Lusa',                   #dropdown value selected automatically when page loads
                                disabled=False,                         #disable dropdown value selection
                                multi=False,                            #allow multiple dropdown values to be selected
                                searchable=True,                        #allow user-searching of dropdown values
                                search_value='',                        #remembers the value searched in dropdown
                                placeholder='Please select...',         #gray, default text shown when no option is selected
                                clearable=True,                         #allow user to removes the selected value
                                style={'width':"100%"},                 #use dictionary to define CSS styles of your dropdown
                                # className='select_box',               #activate separate CSS document in assets folder
                                # persistence=True,                     #remembers dropdown value. Used with persistence_type
                                # persistence_type='memory'             #remembers dropdown value selected until...
                                                      
                                    ),  
                                dbc.Col(
                                    dcc.Graph(id='graph_shares_comments'),
                                    ),
                                ],width={'size':6, 'offset':0}
                            ), 

                        ],
        ),

        return tab4_content
    # Error Message 
    return html.P("FOR SUPPORT PURPOSES ONLY")


if __name__ == "__main__":
    app.run_server(debug=True, port=8888)


