from dash import html
from dash import html, dcc, callback, Input, Output, dash_table
import dash_bootstrap_components as dbc

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#4A4A4A",
}

custom_nav = dbc.Nav(
    children=[
        html.H2(children="Detecção de Fraudes", style={"color": "#FFFFFF"}),
        dbc.NavItem(dbc.NavLink("⚙️ Contexto", active="exact", href="/")),
        dbc.NavItem(dbc.NavLink("📈 Aplicação Prática", active="exact", href="/simulate-transaction")),
        dbc.NavItem(dbc.NavLink("📊 Balanceamento dos dados", active="exact", href="/balance")),
    ],
    pills=True,
    style=SIDEBAR_STYLE
)
