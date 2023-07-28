from services import S3Manager, SmoteSampler

import dash
from dash import html, dcc, callback, Input, Output
import plotly.express as px


dash.register_page(__name__, path='/balance')

s3_manager = S3Manager()
df = s3_manager.load_dataframe()

smote_sampler = SmoteSampler(df)
X_smote, y_smote = smote_sampler.get_xy()

balanced_df = X_smote.copy()
balanced_df['Class'] = y_smote.copy()
heatmap = px.imshow(balanced_df.corr(), color_continuous_scale='Tropic')

box_plot_positive = px.box(balanced_df, x="Class", y="V4")
box_plot_negative = px.box(balanced_df, x="Class", y="V14")

layout = html.Div(className='single-page',
    children=[
    html.H1(children='Balanceamento dos dados'),

    html.Div(className='text-box',
        children=[
        html.P('Um dos principais desafios da análise de fraudes é o desbalanceamento dos dados, as fraudes geralmente representam uma parcela ínfima do total de transações, dado isso é necessário tratar os dados. Abaixo estão comparativos de antes e depois da aplicação de uma técnica de oversampling conhecida como SMOTE.'),
        html.P('Synthetic Minority Oversampling Technique é uma estratégia de oversampling baseada em vizinhos mais próximos para selecionar os objetos as serem amostrados. A vizinha de um objeto geralmente é dado por uma mediade de dissimilaridade, também denominada de distância.')
    ]),

    html.H3(children='Mapa de calor SMOTE'),
    dcc.Graph(
        id='heatmap',
        figure=heatmap
    ),

    html.Div(className='side-div',
        children=[
            html.H3(children='Correlação Positiva'),
            dcc.Graph(
                id='box-plot-positive',
                figure=box_plot_positive
            ),
            html.Div(className='text-box',
                children=[
                html.P('Observando o mapa de calor é possível perceber os atributos, V2, V4 e V11 possuem uma correlação positiva com a chance de ser uma fraude, ou seja quanto maior o seu valor maior a probabilidade da transação ser fraudulenta. Importante observar que todos esses atributos possuem uma grande quantidade de outliers, o que pode ser visualizados nos gráficos de boxplot acima.'),
            ]),
    ]),

    html.Div(className='side-div',
        children=[
            html.H3(children='Correlação Negativa'),
            dcc.Graph(
                id='box-plot-negative',
                figure=box_plot_negative
            ),
            html.Div(className='text-box',
                children=[
                html.P('Da mesma maneira é possível dizer que os atributos V10, V12 e V14 possuem uma correlação negativa com a classe fraude, ou seja quanto menor o seu valor maior a probabilidade da transação ser fraudulenta. Nesses casos também é possível visualizar um número significativo de outliers.'),
            ]),
    ])
])
