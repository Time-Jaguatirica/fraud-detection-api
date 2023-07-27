from services import S3Manager

import dash
from dash import html, dcc, callback, Input, Output, dash_table
from random import randint


dash.register_page(__name__, path='/')

s3_manager = S3Manager()
df = s3_manager.load_dataframe()
rf_model = s3_manager.load_model()

features = ['Time', 'Amount', 'V2', 'V4', 'V11', 'V10', 'V12', 'V14']

layout = html.Div(className='simulate-transaction-page',
    children=[
    html.H1(children='Simulação de Transação', style={"text-align": "center"}),

    html.Div(className='text-box', children=[
        html.P(children='Simulação utilizando o algoritmo Random Forest para classificar a transação em fraude ou legítima.'),
        html.P(children='Em resumo, o Random Forest irá criar múltiplas árvores de decisão de maneira aleatória, formando o que podemos enxergar como uma floresta, onde cada árvore será utilizada na escolha do resultado final, em uma espécie de votação.'),
    ]),

    html.H2(children='Transações em tempo real:'),
    dash_table.DataTable(id='live-table'),
    dcc.Interval(id='refresh', interval=10000, n_intervals=0),

    html.Hr(),

    html.H2(children='Filtrar por:'),
    dcc.RadioItems(options=['Legítima', 'Fraude'], value='Legítima', id='controls-and-radio-item'),
    dash_table.DataTable(id='filter-table'),

    dcc.Store(id='subset')
])


@callback(Output('subset', 'data'),
          Input('refresh', 'n_intervals'))
def generate_subset_dict(n):
    actual = randint(1, 100)
    subset = df.loc[actual:actual+10].drop(columns=['Class'])
    predictions = rf_model.predict(subset)
    filter_subset = subset.loc[actual:actual+10, features]

    return { "records": filter_subset.to_dict('records'), "predictions": predictions}

@callback(Output('live-table', 'data'),
          Input('subset', 'data'))
def update_table(subset_dict):
    return subset_dict["records"]

@callback(Output('filter-table', 'data'),
          Input('subset', 'data'),
          Input('controls-and-radio-item', 'value'))
def filter_table(data, type):
    records = data['records']
    predictions = data['predictions']

    fraud = []
    legitimate = []

    for i in range(len(records)):
        if predictions[i] == 0:
            legitimate.append(records[i])
        else:
            fraud.append(records[i])


    if type == 'Legítima':
        return legitimate

    return fraud
