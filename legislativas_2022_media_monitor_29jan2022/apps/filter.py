# -*- coding: utf-8 -*-

# FILTERING BY OCS and Candidate Graph


# import libraries
import plotly.express as px
import pandas as pd
import os

# csv to pandas dataframe
df = pd.read_csv('../legislativas_2022_media_monitor_29jan2022_raw_data/crowdtangle_2022_01_29_inesreal_last_30_days_dataset_raw.csv')

# Create Dataframe based on media outlets criteria

df_filter = df[df['Page Name'].isin(['Jornal de Notícias',
                                     'TVI',
                                     'SIC Notícias',
                                     'Correio da Manhã',
                                     'Diário de Notícias',
                                     'SAPO',
                                     'Público',
                                     'CNN Portugal',
                                     'Notícias ao Minuto',
                                     'Observador',
                                     'Expresso',
                                     'CM TV',
                                     'Semanário Sol',
                                     'RTP',
                                     'Revista Visão',
                                     'RTP Notícias',
                                     'TSF - Rádio Notícias',
                                     'Jornal Económico',
                                     'RTP 1',
                                     'Renascença',
                                     'Jornal de Negócios',
                                     'SÁBADO',
                                     'ionline.pt',
                                     'Agência Lusa',
                                     'ECO',
                                     'Novo Semanário',
                                     'Rádio Observador'
                                     ])]

# Save filtered dataframe to CSV 

df_filter.to_csv('../legislativas_2022_media_monitor_29jan2022_filter_data/crowdtangle_2022_01_29_inesreal_last_30_days_dataset_filter.csv')



# Create series based on value counts for each Facebook Page 

series_counter = df_filter['Page Name'].value_counts()

# Turn series into a dataframe 

df_c= series_counter.to_frame().reset_index()

# Rename Columns 

df_c = df_c.rename(columns={'index':'Page Name','Page Name':'Counts'})


# Plot Candidates main graph 

fig_main = px.bar(df_c, x='Page Name' , y='Counts',template='plotly_white',
                  title='Inês Sousa Real - Total Mentions by Media Outlet<br><sup>Period:30/12/2021 to 29/01/2022</sup>',
                  color_discrete_sequence=["#00798E"], 
                  text='Counts'
                 )

fig_main.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

fig_main.write_image("../legislativas_2022_media_monitor_29jan2022_graphs/legislativas_2022_images_inesreal_total.png",  width=1920, height=1080, scale=4)
# fig_main.show()






