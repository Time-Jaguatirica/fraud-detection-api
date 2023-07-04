from flask import Flask, render_template
from .services import DataFrame

app = Flask(__name__)
dataframe = DataFrame()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/features")
def get_features():
    return dataframe.get_features()

if __name__ == "__main__":
    app.run(debug=True)
