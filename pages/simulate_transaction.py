from services import S3Manager

import dash
from dash import html, dcc, callback, Input, Output, dash_table
from random import randint


dash.register_page(__name__, path='/simulate-transaction')

s3_manager = S3Manager()
df = s3_manager.load_dataframe()
features = ['Time', 'Amount', 'V2', 'V4', 'V11', 'V10', 'V12', 'V14']

layout = html.Div(className='simulate-transaction-page',
    children=[
    html.H1(children='Simulação de Transação', style={"text-align": "center"}),

    html.P(children='Simulação utilizando o algoritmo Random Forest para classificar a transação em fraude, inconclusiva ou legítima.'),

    html.H2(children='Transações em tempo real:'),
    dash_table.DataTable(id='live-table'),

    dcc.Interval(id='refresh', interval=10000, n_intervals=0),
])

@callback(Output('live-table', 'data'),
          Input('refresh', 'n_intervals'))
def update_table(n):
    actual = randint(1, 100)
    subset = df.loc[actual:actual+5, features]

    return subset.to_dict('records')
