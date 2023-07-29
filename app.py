from components import custom_nav, footer
from dash import Dash, html
import dash_bootstrap_components as dbc
import dash


external_stylesheets = [
    {
        "href": (
			"http://fonts.googleapis.com/css?"
			"family=Ubuntu:regular,bold&subset=Latin"
        ),
        "rel": "stylesheet",
    },
]

app = Dash(__name__, use_pages=True, external_stylesheets=[external_stylesheets])

server = app.server

app.layout = html.Div([
    custom_nav,
	dash.page_container,
    footer,
])

if __name__ == '__main__':
	app.run(debug=True)
