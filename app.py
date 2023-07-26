from dash import Dash, html
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

app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
	dash.page_container
])

if __name__ == '__main__':
	app.run(debug=True)
