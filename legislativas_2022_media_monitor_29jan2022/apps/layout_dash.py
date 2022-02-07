# -*- coding: utf-8 -*-

# --------- Import libraries -----------
import dash 
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px 
import dash_bootstrap_components as dbc


# -------------- Data Operations ------------------

df = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/data_products/legislativas_2022_final_dataset_percentages.csv')

df_individuals  = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/data_products/legislativas_2022_all_candidates_filtered.csv')

df_individuals = df_individuals.drop(columns=["Unnamed: 0"])
df_indivuduals = df_individuals.drop(columns=["Post Created Date"])
df_individuals_melt=pd.melt(df_individuals,id_vars=['candidato','Page Name'])



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
    "Inês Sousa-Real": "#00798E"
}

pie_color_map = {
    "Angry":"#666666",
    "Love":"#5F468F"
}



# Define Tabs Content 

# tab1 = Totals non stacked

tab1_content = dbc.Row(
	#dbc.Card(
    #dbc.CardBody(

    	
		
			
			[ # Array for multiple elements inside row 

				dbc.Row(dbc.Col(html.Hr(style={'borderWidth': "1vh", "width": "100%", "borderColor": "#CAE7B9","opacity": "unset"}),width={'size':12, 'offset':0}),),
				html.H1("Overview"),
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
	                               
	                        ), # End of DropDown Total
	        	dcc.Graph(id='graph_totals_stacked'),


            ], #End of Array for multiple elements                                 
                                                                       
    	),# End of Row 
    
	#), # End of CardBody 

#) #End of tab_content Card



# tab2 = Totals stacked

tab2_content = html.Div(
	#dbc.Card(
    #dbc.CardBody(

    	
		
			
			[ # Array for multiple elements inside row 

			dbc.Col(html.Hr(style={'borderWidth': "5vh", "width": "100%", "borderColor": "#AB87FF","opacity": "unset"}),width={'size':10, 'offset':1}),
			html.H1("% Totals Stacked "),
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
                                ),    # End of DropDown Total

            ], #End of Array for multiple elements                                 
                                                                       
    	),# End of Row 
    
	#), # End of CardBody 

#) #End of tab_content Card


tabs = html.Div(
	
    [
        dbc.Tabs(
            [
                dbc.Col(dbc.Tab(tab1_content,label="OVERVIEW")),
                dbc.Col(dbc.Tab(tab2_content,label="PERCENTAGES", label_style={"color": "#B4E1FF"})),
            ]
        ),
    ],

)



# --------------- Define App -------------

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# --------------- Start App Layout ------------------

app.layout = html.Div([

		dbc.Row(
			[
			dbc.Col(html.Hr(style={'borderWidth': "2vh", "width": "100%", "borderColor": "#CAE7B9","opacity": "unset"}),width={'size':2, 'offset':1}),
			dbc.Col(html.Hr(style={'borderWidth': "2vh", "width": "100%", "borderColor": "#F3DE8A","opacity": "unset"}),width={'size':2}),
			dbc.Col(html.Hr(style={'borderWidth': "2vh", "width": "100%", "borderColor": "#EB9486","opacity": "unset"}),width={'size':2}),
			dbc.Col(html.Hr(style={'borderWidth': "2vh", "width": "100%", "borderColor": "#7E7F9A","opacity": "unset"}),width={'size':2}),
			dbc.Col(html.Hr(style={'borderWidth': "2vh", "width": "100%", "borderColor": "#97A7B3","opacity": "unset"}),width={'size':2}),

			

			],className="g-0",
		),
		dbc.Row( # Second row 
			[ # you have to create a children's array to have more than one column in a row 
				dbc.Col(html.H1("Legislativas 2022 Media Monitor"), width={'size': 6, 'offset':1}), #First Column
				dbc.Col(html.H4("Data from CrowdTangle",style={"color":"#7E7F9A"}), width={'size': 5, 'offset':0}), #Second Column
			], # Close Children of first Row
		), # end of first row  

		dbc.Row(
			[
			dbc.Col(html.H5("Observing Media Trends"), width={'size':3, 'offset':1}), # second row
			dbc.Col(html.H5("Made with Plotly Dash",style={"color":"#97A7B3"}), width={'size':5,'offset':3}),
			],
		),

		# third  row makes horizontal line
		dbc.Row(dbc.Col(html.Hr(style={'borderWidth': "0.5vh", "width": "100%", "borderColor": "#F3DE8A","opacity": "unset"}),width={'size':10, 'offset':1}),), 

		# fourth  row : lets add the tabs
		

		
			




				

	], # Div Array Closes 
) # HTML div closes 

# -------------- Define callbacks ------
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

# ------------- Start App --------------

if __name__ == "__main__":
	app.run_server(debug=True)