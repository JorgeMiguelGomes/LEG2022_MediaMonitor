# -*- coding: utf-8 -*-

# import libraries 

from dash import Dash, dcc, html, Input, Output
import pandas as pd 
import plotly.express as px 

# read csv to dataframe 

df = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/data_products/legislativas_2022_final_dataset_percentages.csv')

print(df.info())

# Create color for each candidate 

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



app = Dash(__name__)

#------------------------------------------------------------------------------------------------

app.layout = html.Div([

    html.Div([
        dcc.Graph(id='graph')
    ],className='nine columns'),

    html.Div([
        
        html.Br(),
        html.Div(id='output_data'),
        html.Br(),

        html.Label(['Choose column:'],style={'font-weight': 'bold', "text-align": "center"}),

        dcc.Dropdown(
        id='dropdown',
        options=[{'label': 'Total Interactions', 'value': 'Total Interactions_Percentages'} ,
                 {'label': 'Total Likes','value': 'Likes_Percentages'},
                 {'label': 'Total Comments','value': 'Comments_Percentages'},
                 {'label': 'Total Shares','value': 'Shares_Percentages'},
                 {'label': 'Total Love','value': 'Love_Percentages'},
                 {'label': 'Total Angry','value': 'Angry_Percentages'},
            ],
            optionHeight=35,                        #height/space between dropdown options
            value='Total Interactions_Percentages', #dropdown value selected automatically when page loads
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
    ],className='three columns'),

])

#------------------------------------------------------------------------------------------------


@app.callback(
    Output(component_id='graph', component_property='figure'),
    [Input(component_id='dropdown', component_property='value')]
)


def build_graph(column_chosen):
    dff =  df 
    fig = px.bar(dff,x='Page Name',y=column_chosen,color='candidato',color_discrete_map=candidate_color_map, 
                template='plotly_white',
                title='MEDIA MONITOR - Legislativas 2022<br><sup>Period:30/12/2021 a 29/01/2022</sup')
    return fig 

if __name__ == '__main__':
    app.run_server(debug=True)



