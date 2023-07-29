import dash
from components import footer
from dash import html, dcc
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
        # html.P(children='Módulo 2 (Onça Pintada) do projeto de extensão Pantanal Dev - Desafio: Detecção de fraudes.'),
        html.P(children='De acordo com o Serasa (2022) 47% dos brasileiros tem 4+ cartões de crédito e 29% tem cinco ou mais cartoões. De acordo com uma pesquisa realizada pela Kaspersky em 2022, 2 em 10 brasileiros relataram terem sofrido com fraude online de cartão de crédito. Pensando nas consequencias para os usuários de cartão e do aumento da atividade online e o sucesso dos e-commerces, tentativas de fraudes precisam ser identificadas o mais rápido possível pelas instituições financeiras.'),

        html.P(children='Assim, esse trabalho teve como objetivo testar um modelo de aprendizado de máquina para identificar transações fraudulentas.'),

        html.A(children='https://www.serasa.com.br/imprensa/pesquisa-da-serasa-aponta-que-consumidores-tem-quatro-ou-mais-cartoes/', href='https://www.serasa.com.br/imprensa/pesquisa-da-serasa-aponta-que-consumidores-tem-quatro-ou-mais-cartoes/'),
        html.P(children=''),
        html.A(children='https://www.securityreport.com.br/2-em-cada-10-brasileiros-ja-sofreram-fraudes-on-line-de-cartao-de-credito/#.Y9pardLMJH4', href='https://www.securityreport.com.br/2-em-cada-10-brasileiros-ja-sofreram-fraudes-on-line-de-cartao-de-credito/#.Y9pardLMJH4'),
    ]),

    html.H2(children='Base de Dados'),
    html.Div(className='text-box', children=[
        html.P(children='Para o projeto foi utilizado um dataset disponipilizado no kaggle. Esse dataset foi montado com dados de operadoras de cartão europeias de transações feitas em setembro de 2013. É um dataset extremamente desbalanceado, com apenas 0.172% de entradas de fraude. Ele também é completamente anonimizado, com seus atrinutos nomeados como V1 até V28, somado aos atributos Time e Amount. Para balançear os dados para utilizar no treinamento do modelo utilizamos a tecnica SMOTE. Para mais detalhes clique na aba Balanceamento dos dados.'),
        # gráfico pizza
        dcc.Graph(
            id='pie_graph_initial',
            figure=pie_graph_initial
        ),
    ]),

    html.H2(children='Algoritmo Utilizado'),
    html.Div(className='text-box', children=[
        html.P(children='O modelo Random Forest é um algoritmo de aprendizado de máquina White Box (Modelo Explicativo) que combina várias árvores de decisão para fazer previsões mais precisas. Cada árvore é treinada em uma amostra aleatória dos dados e usa apenas algumas variáveis. Depois, as previsões das árvores são combinadas por votação (classificação) ou média (regressão) para obter o resultado final. O Random Forest é conhecido por ser robusto e evitar overfitting.'),

        html.Img(src='assets/tree-example.png', alt='Exemplo da árvore gerada pelo algoritmo.', style={"width": "790px", "margin-bottom": "1rem"}),

        html.Img(src='assets/metrics.png', alt='Exemplo da métrica de precisão.'),
    ]),
    footer,
])
