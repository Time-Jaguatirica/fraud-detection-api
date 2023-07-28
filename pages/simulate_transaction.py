from services import S3Manager

import dash
from dash import html, dcc, callback, Input, Output, dash_table
from random import randint
import plotly.express as px
import pandas as pd


dash.register_page(__name__, path='/simulate-transaction')

s3_manager = S3Manager()
df = s3_manager.load_dataframe()
rf_model = s3_manager.load_model()

feature_importances = pd.Series(rf_model.feature_importances_, index=df.drop(columns=['Class']).columns).sort_values(ascending=False)
feature_graph = px.bar(feature_importances)

features = ['Time', 'Amount', 'V2', 'V4', 'V11', 'V10', 'V12', 'V14']

layout = html.Div(className='single-page',
    children=[
    html.H1(children='Aplicação Prática'),

    html.Div(className='text-box', children=[
        html.P(children='Simulação de insights sendo gerados em tempo real pelo algoritmo Random Forest para classificar as transações em seu négocio, podendo captar padrões e identificar fraudes imediatamente.'),
    ]),

    html.H3(children='Features de maior relevância para o algoritmo'),
    dcc.Graph(id='feature-graph', figure=feature_graph),

    html.H3(children='Transações em tempo real'),
    dash_table.DataTable(id='live-table'),
    dcc.Interval(id='refresh', interval=10000, n_intervals=0),

    html.Hr(),

    html.H3(children='Filtrar por:'),
    dcc.RadioItems(options=['Legítima', 'Fraude'], value='Legítima', id='controls-and-radio-item'),
    dash_table.DataTable(id='filter-table'),

    dcc.Store(id='subset')
])


@callback(Output('subset', 'data'),
          Input('refresh', 'n_intervals'))
def generate_subset_dict(n):
    subset = generate_random_subset(df).drop(columns=['Class'])
    predictions = rf_model.predict(subset)
    filter_subset = subset.loc[:, features]

    return { "records": filter_subset.to_dict('records'), "predictions": predictions}

@callback(Output('live-table', 'data'),
          Input('subset', 'data'))
def update_table(subset_dict):
    return subset_dict["records"]

@callback(Output('filter-table', 'data'),
          Input('controls-and-radio-item', 'value'))
def filter_table(value):
    if value == 'Fraude':
        subset = df.loc[df['Class'] == 1]
        subset = generate_random_subset(subset)

    else:
        subset = generate_random_subset(df)
    
    return subset.loc[:, features].to_dict('records')


def generate_random_subset(df):
    df_random_values = list(df.index.values)

    random_list = []

    for i in range(10):
        actual_random = df_random_values[randint(0, len(df_random_values))]
        df_random_values.remove(actual_random)
        random_list.append(actual_random)

    subset = df.loc[random_list]

    return subset
