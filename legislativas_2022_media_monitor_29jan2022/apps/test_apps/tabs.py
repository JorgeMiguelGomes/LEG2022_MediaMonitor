# -*- coding: utf-8 -*-

# Import libraries 
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px 

df = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/data_products/legislativas_2022_final_dataset_percentages.csv')

df_individuals  = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/data_products/legislativas_2022_all_candidates_filtered.csv')

df_individuals = df_individuals.drop(columns=["Unnamed: 0"])
df_indivuduals = df_individuals.drop(columns=["Post Created Date"])
df_individuals_melt=pd.melt(df_individuals,id_vars=['candidato','Page Name'])

available_candidates = df_individuals_melt['candidato'].unique()
available_pages = df_individuals_melt['Page Name'].unique()
available_metrcis = df_individuals_melt['variable'].unique()



# -------------- Styling -------------------------------------------

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

candidate_color_map = {
    "Rui Rio": "#FF6400",
    "Francisco Rodrigues dos Santos": "#0B6AB1",
    "António Costa": "#F1A0A2",
    "Rui Tavares": "#00CE8C",
    "Catarina Martins": "#C90635",
    "Jerónimo de Sousa": "#025298",
    "André Ventura": "#202056",
    "João Cotrim Figueiredo": "#00AEEF",
    "Inês Sousa-Real": "#00798E"
}

pie_color_map = {
    "Angry":"#666666",
    "Love":"#5F468F"
}

# -------------------- APP starts here ---------------------------

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div(children=[
        html.H1(children='Legislativas Media Monitor')


        ],className='twelve columns'),

    html.Div(children=[
        dcc.Tabs([
            dcc.Tab(label='Totals', children=[
                    html.Div([
                        dcc.Graph(id='graph_totals')
                        ],
                        className='ten columns'),

                        html.Div([
                            
                            html.Br(),
                            html.Div(id='output_data'),
                            html.Br(),

                            html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

                            dcc.Dropdown(
                            id='dropdown_total',
                            options=[{'label': 'Total Interactions', 'value': 'Total Interactions'} ,
                                     {'label': 'Total Likes','value': 'Likes'},
                                     {'label': 'Total Comments','value': 'Comments'},
                                     {'label': 'Total Shares','value': 'Shares'},
                                     {'label': 'Total Love','value': 'Love'},
                                     {'label': 'Total Angry','value': 'Angry'},
                                ],
                                optionHeight=35,                        #height/space between dropdown options
                                value='Total Interactions',             #dropdown value selected automatically when page loads
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
                                ),                                      #'memory': browser tab is refreshed
                                                                        #'session': browser tab is closed
                                                                        #'local': browser cookies are deleted
                        ],className='two columns'),
                        ]),
            dcc.Tab(label='Stacked', children=[
                    html.Div([
                        dcc.Graph(id='graph_totals_stacked')
                        ],
                        className='ten columns'),

                        html.Div([
                            
                            html.Br(),
                            html.Div(id='output_data_stacked'),
                            html.Br(),

                            html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

                            dcc.Dropdown(
                            id='dropdown_total_stacked',
                            options=[{'label': 'Total Interactions', 'value': 'Total Interactions_Percentages'} ,
                                     {'label': 'Total Likes','value': 'Likes_Percentages'},
                                     {'label': 'Total Comments','value': 'Comments_Percentages'},
                                     {'label': 'Total Shares','value': 'Shares_Percentages'},
                                     {'label': 'Total Love','value': 'Love_Percentages'},
                                     {'label': 'Total Angry','value': 'Angry_Percentages'},
                                ],
                                optionHeight=35,                        #height/space between dropdown options
                                value='Total Interactions_Percentages',             #dropdown value selected automatically when page loads
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
                                ),                                      #'memory': browser tab is refreshed
                                                                        #'session': browser tab is closed
                                                                        #'local': browser cookies are deleted
                        ],className='two columns'),
                
            ]),
            dcc.Tab(label='Individual', children=[
                    html.Div([
                        dcc.Graph(id='graph_individuals') 
                        ],
                        className=' four columns'),

                        html.Div([
                            
                            html.Br(),
                            html.Div(id='output_data_individuals'),
                            html.Br(),

                            html.Label(['Candidate:'],style={'font-weight': 'bold', "text-align": "left"}),

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
                                ),                                      #'memory': browser tab is refreshed
                                                                        #'session': browser tab is closed
                                                                        #'local': browser cookies are deleted
                                                                  #'session': browser tab is closed
                                 
                                 
                        ],className='two columns'),

                    html.Div([
                        dcc.Graph(id='graph_shares_comments') 
                        ],
                        className=' four columns'),

                    html.Div([
                            
                            html.Br(),
                            html.Div(id='output_data_ocs'),
                            html.Br(),

                            html.Label(['Media Outlet'],style={'font-weight': 'bold', "text-align": "left"}),

                            dcc.Dropdown(
                            id='dropdown_media_outlet',
                            options=[{'label': i, 'value': i} for i in df['Page Name'].unique()
                                ],
                                optionHeight=35,                        #height/space between dropdown options
                                value='Agência Lusa'      ,             #dropdown value selected automatically when page loads
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
                                ),                                      #'memory': browser tab is refreshed
                                                                        #'session': browser tab is closed
                                                                        #'local': browser cookies are deleted
                                                                        #'session': browser tab is closed
                                 
                                 
                        ],className='two columns'),


            ]),
        ]),
    ])
])


@app.callback(
    Output(component_id='graph_totals', component_property='figure'),
    [Input(component_id='dropdown_total', component_property='value')]
)


def build_graph_total(column_chosen):
    dff =  df 
    fig = px.bar(dff,x='Page Name',y=column_chosen,color='candidato',color_discrete_map=candidate_color_map, 
                template='plotly_white',
                title='MEDIA MONITOR - Legislativas 2022<br><sup>Period:30/12/2021 a 29/01/2022</sup')
    return fig 

@app.callback(
    Output(component_id='graph_totals_stacked', component_property='figure'),
    [Input(component_id='dropdown_total_stacked', component_property='value')]
)


def build_graph_total_stacked(column_chosen):
    dff =  df 
    fig_stacked = px.bar(dff,x='Page Name',y=column_chosen,color='candidato',color_discrete_map=candidate_color_map, 
                template='plotly_white',
                title='MEDIA MONITOR - Legislativas 2022<br><sup>Period:30/12/2021 a 29/01/2022</sup')
    return fig_stacked

@app.callback(
    Output(component_id='graph_individuals', component_property='figure'),
    [Input(component_id='dropdown_candidates', component_property='value')],
)


def build_graph_individuals(column_chosen):
    dff = df
    totals_sentiment = dff.groupby(['candidato'])[['Love','Angry']].sum().reset_index()
    totals_sentiment_melt = pd.melt(totals_sentiment,id_vars="candidato")
    totals_sentiment_melt = totals_sentiment_melt[totals_sentiment_melt['candidato'] == column_chosen]


    fig_individuals = px.pie(totals_sentiment_melt,names="variable",values="value",hole=0.5, color="variable",color_discrete_map=pie_color_map)

    fig_shares_comments = px.pie(totals_sentiment_melt,names="variable",values="value",hole=0.5, color="variable",color_discrete_map=pie_color_map)

    return fig_individuals

@app.callback(
    Output(component_id='graph_shares_comments', component_property='figure'),
    
    [Input(component_id='dropdown_media_outlet', component_property='value')],
)

def build_graph_shares_comments(column_chosen):
    dff = df
    total_shares_comments = dff.groupby(['Page Name'])[['Love','Angry']].sum().reset_index()
    total_shares_comments_melt = pd.melt(total_shares_comments,id_vars="Page Name")
    total_shares_comments_melt = total_shares_comments_melt[total_shares_comments_melt['Page Name'] == column_chosen] 

    fig_shares_comments = px.bar(total_shares_comments_melt,x="variable",y="value", color="variable",color_discrete_map=pie_color_map, template='plotly_white')   

    return fig_shares_comments

if __name__ == '__main__':
    app.run_server(debug=True)


#--------------- End Dashboard -----------------