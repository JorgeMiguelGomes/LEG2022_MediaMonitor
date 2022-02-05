# -*- coding: utf-8 -*-

# Aggregating Dataframes and Plotting Results


# import libraries
import plotly.express as px
import pandas as pd
import os

# define color for each candidate 
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


# Fetching filtered dataframes from GitHub Repo
df_ac = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/legislativas_2022_media_monitor_29jan2022_filter_data/crowdtangle_2022_01_29_antoniocosta_last_30_days_dataset_filter.csv')
df_rr = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/legislativas_2022_media_monitor_29jan2022_filter_data/crowdtangle_2022_01_29_ruirio_last_30_days_dataset_filter.csv')
df_cm = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/legislativas_2022_media_monitor_29jan2022_filter_data/crowdtangle_2022_01_29_catarinamartins_last_30_days_dataset_filter.csv')
df_js = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/legislativas_2022_media_monitor_29jan2022_filter_data/crowdtangle_2022_01_29_jeronimosousa_last_30_days_dataset_filter.csv')
df_ir = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/legislativas_2022_media_monitor_29jan2022_filter_data/crowdtangle_2022_01_29_inesreal_last_30_days_dataset_filter.csv')
df_fs = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/legislativas_2022_media_monitor_29jan2022_filter_data/crowdtangle_2022_01_29_franciscosantos_last_30_days_dataset_filter.csv')
df_av = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/legislativas_2022_media_monitor_29jan2022_filter_data/crowdtangle_2022_01_29_andreventura_last_30_days_dataset_filter.csv')
df_jf = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/legislativas_2022_media_monitor_29jan2022_filter_data/crowdtangle_2022_01_29_joaofigueiredo_last_30_days_dataset_filter.csv')
df_rt = pd.read_csv('https://raw.githubusercontent.com/JorgeMiguelGomes/LEG2022_MediaMonitor/main/legislativas_2022_media_monitor_29jan2022/legislativas_2022_media_monitor_29jan2022_filter_data/crowdtangle_2022_01_29_ruitavares_last_30_days_dataset_filter.csv')

# Create a new column in each dataframe with candidate's name
df_ac['candidato'] = "António Costa"
df_rr['candidato'] = "Rui Rio"
df_cm['candidato'] = "Catarina Martins"
df_js['candidato'] = "Jerónimo de Sousa"
df_ir['candidato'] = "Inês Sousa-Real"
df_fs['candidato'] = "Francisco Rodrigues dos Santos"
df_av['candidato'] = "André Ventura"
df_jf['candidato'] = "João Cotrim Figueiredo"
df_rt['candidato'] = "Rui Tavares"

#Make unique dataframe 
frames = [df_ac,df_rr,df_cm,df_js,df_ir,df_fs,df_av,df_jf,df_rt]
df_all = pd.concat(frames)


# create dataframe only with needed columns 
work_df = df_all[['candidato','Page Name','Post Created Date','Total Interactions','Likes','Comments','Shares','Love','Angry']]

# delete commas from Total Interactions
work_df= work_df.replace(',','', regex=True)

# Optionally you can save the dataframe to csv 
# Use work_df.to_csv('path/filename.csv')


