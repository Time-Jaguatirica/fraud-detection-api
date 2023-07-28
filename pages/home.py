import dash
from dash import html, dcc, callback, Input, Output, dash_table
from services import S3Manager, SmoteSampler
import plotly.express as px

dash.register_page(__name__, path='/')

s3_manager = S3Manager()
df = s3_manager.load_dataframe()

smote_sampler = SmoteSampler(df)

class_df = df['Class'].value_counts()
pie_graph_initial = px.pie(class_df, values=class_df, names=['Normal', 'Fraude'], title='Porcentagem de transações normais vs fraudes.')

layout = html.Div(className='single-page', children=[
    html.H1(children='Contexto do Projeto'),
    html.Div(className='text-box', children=[
        html.P(children='Módulo 2 (Onça Pintada) do projeto de extensão Pantanal Dev (programa de capacitação imersiva em tecnologias inovadoras).'),
        html.P(children='Desafio: Detecção de fraudes.'),
        html.P(children='A detecção de fraudes também relacionada a detecção de anomalias tem como objetivo identificar atividades ou padrões não usuais (incomuns). Por exemplo, para o setor financeiro: falsificação de assinaturas em cheques, clonagem de cartões de crédito, lavagem de dinheiro, declarar falência propositalmente (bankruptcy), etc.'),
    ]),
    # grafico pizza
    dcc.Graph(
        id='pie_graph_initial',
        figure=pie_graph_initial
    ),

    html.H2(children='Base de Dados'),
    html.Div(className='text-box', children=[
        html.P(children='Um conjunto de dados obtidos da Kaggle (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud), contêm transações feitas por cartões de crédito europeus em setembro de 2013. Onde 492 das 284.807 transações são fraudulentas, ou seja, um conjunto altamente desbalanceado.'),
        html.P(children='Essa base de dados contém 30 atributos (V1, V2, ..., V28, tempo e quantidade), 2 classes (0 para transações legítimas e 1 para transações fraudulentas) e 284.807 transações.'),
    ]),

    html.H2(children='Algoritmo Utilizado'),
    html.Div(className='text-box', children=[
        html.P(children='O Random Forest, algoritmo de aprendizado de máquina utilizado para realizar predições, foi utilizado para o treinamendo do modelo.'),
        html.P(children='Em suma, o algoritmo cria de forma aleatória várias Árvores de Decisão (Decision Trees) e combina o resultado de todas elas para chegar no resultado final por meio de um tipo de votação.'),
    ]),
    # exemplo de uso do algoritmo
])