import dash
from dash import html, dcc, callback, Input, Output, dash_table

dash.register_page(__name__, path='/')

layout = html.Div(className='single-page',
    children=[
    html.H1(children='Contexto')
])