# -*- coding: utf-8 -*-

# FILTERING BY OCS and Candidate Graph


# import libraries
import plotly.express as px
import pandas as pd
import os

raw_data_base_path = "../legislativas_2022_media_monitor_29jan2022_raw_data/"
filter_data_base_path = "../legislativas_2022_media_monitor_29jan2022_filter_data/"
graphs_base_path = "../legislativas_2022_media_monitor_29jan2022_graphs/"

candidate_color_map = {
    "ruirio": "#FF6400",
    "franciscosantos ": "#0B6AB1",
    "antoniocosta": "#E31F26",
    "ruitavares": "#00CE8C",
    "catarinamartins": "#C90635",
    "jeronimosousa": "#025298",
    "andreventura": "#202056",
    "joaofigueiredo": "#00AEEF",
    "inesreal": "#00798E"
}

assets = [
    {
        'name': 'André Ventura',
        'source_csv': 'crowdtangle_2022_01_29_andreventura_last_30_days_dataset_raw.csv',
        'filter_csv': 'crowdtangle_2022_01_29_andreventura_last_30_days_dataset_filter.csv',
        'output_png': 'legislativas_2022_images_andreventura_total.png',
        'color': '#202056'
    },
    {
        'name': 'António Costa',
        'source_csv': 'crowdtangle_2022_01_29_antoniocosta_last_30_days_dataset_raw.csv',
        'filter_csv': 'crowdtangle_2022_01_29_antoniocosta_last_30_days_dataset_filter.csv',
        'output_png': 'legislativas_2022_images_antoniocosta_total.png',
        'color': '#E31F26'
    },
    {
        'name': 'Catarina Martins',
        'source_csv': 'crowdtangle_2022_01_29_catarinamartins_last_30_days_dataset_raw.csv',
        'filter_csv': 'crowdtangle_2022_01_29_catarinamartins_last_30_days_dataset_filter.csv',
        'output_png': 'legislativas_2022_images_catarinamartins_total.png',
        'color': '#C90635'
    },
    {
        'name': 'Francisco Santos',
        'source_csv': 'crowdtangle_2022_01_29_franciscosantos_last_30_days_dataset_raw.csv',
        'filter_csv': 'crowdtangle_2022_01_29_franciscosantos_last_30_days_dataset_filter.csv',
        'output_png': 'legislativas_2022_images_franciscosantos_total.png',
        'color': '#0B6AB1'
    },
    {
        'name': 'Inês Sousa Real',
        'source_csv': 'crowdtangle_2022_01_29_inesreal_last_30_days_dataset_raw.csv',
        'filter_csv': 'crowdtangle_2022_01_29_inesreal_last_30_days_dataset_filter.csv',
        'output_png': 'legislativas_2022_images_inesreal_total.png',
        'color': '#00798E'
    },
    {
        'name': 'Jerónimo Sousa',
        'source_csv': 'crowdtangle_2022_01_29_jeronimosousa_last_30_days_dataset_raw.csv',
        'filter_csv': 'crowdtangle_2022_01_29_jeronimosousa_last_30_days_dataset_filter.csv',
        'output_png': 'legislativas_2022_images_jeronimosousa_total.png',
        'color': '#025298'
    },
    {
        'name': 'João Figueiredo',
        'source_csv': 'crowdtangle_2022_01_29_joaofigueiredo_last_30_days_dataset_raw.csv',
        'filter_csv': 'crowdtangle_2022_01_29_joaofigueiredo_last_30_days_dataset_filter.csv',
        'output_png': 'legislativas_2022_images_joaofigueiredo_total.png',
        'color': '#00AEEF'
    },
    {
        'name': 'Rui Rio',
        'source_csv': 'crowdtangle_2022_01_29_ruirio_last_30_days_dataset_raw.csv',
        'filter_csv': 'crowdtangle_2022_01_29_ruirio_last_30_days_dataset_filter.csv',
        'output_png': 'legislativas_2022_images_ruirio_total.png',
        'color': '#FF6400'
    },
    {
        'name': 'Rui Tavares',
        'source_csv': 'crowdtangle_2022_01_29_ruitavares_last_30_days_dataset_raw.csv',
        'filter_csv': 'crowdtangle_2022_01_29_ruitavares_last_30_days_dataset_filter.csv',
        'output_png': 'legislativas_2022_images_ruitavares_total.png',
        'color': '#00CE8C'
    },
]

for asset in assets:

    # csv to pandas dataframe
    df = pd.read_csv(f"{raw_data_base_path}{asset['source_csv']}")

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

    df_filter.to_csv(f"{filter_data_base_path}{asset['filter_csv']}")

    # Create series based on value counts for each Facebook Page

    series_counter = df_filter['Page Name'].value_counts()

    # Turn series into a dataframe

    df_c = series_counter.to_frame().reset_index()

    # Rename Columns

    df_c = df_c.rename(columns={'index': 'Page Name', 'Page Name': 'Counts'})

    # Plot Candidates main graph

    fig_main = px.bar(df_c, x='Page Name', y='Counts', template='plotly_white',
                      title=f"{asset['name']} - Total Mentions by Media Outlet<br><sup>Period:30/12/2021 to 29/01/2022</sup>",
                      color_discrete_sequence=[f"{asset['color']}"],
                      text='Counts'
                      )

    fig_main.update_traces(textfont_size=12, textangle=0,
                           textposition="outside", cliponaxis=False)

    fig_main.write_image(
        f"{graphs_base_path}{asset['output_png']}",  width=1920, height=1080, scale=4)
    # fig_main.show()
