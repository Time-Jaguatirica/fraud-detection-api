from services import S3Manager, SmoteSampler

import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px


dash.register_page(__name__, path='/')

s3_manager = S3Manager()
df = s3_manager.load_dataframe()

smote_sampler = SmoteSampler(df)

class_df = df['Class'].value_counts()
pie_graph_initial = px.pie(class_df, values=class_df, names=['Normal', 'Fraude'], title='Porcentagem de transações normais vs fraudes.')

X_smote, y_smote = smote_sampler.get_xy()
smote_df = y_smote.value_counts()
pie_graph_smote = px.pie(smote_df, values=smote_df, names=['Normal', 'Fraude'], title='Após a aplicação da técnica SMOTE')

layout = html.Div(children=[
    html.H1(children='Técnicas de balanceamento dos dados'),

    html.Div(children='''
             Na aréa de detecção de fraudes, é muito comum as classes virem desbalanceadas, onde as anomalias são as exceções por isso se torna vital a utilização de técnicas de balanceamento para obter precisão nas análises.
    '''),

    dcc.Graph(
        id='pie_graph_initial',
        figure=pie_graph_initial
    ),

    dcc.Graph(
        id='pie_graph_smote',
        figure=pie_graph_smote
    )
])
