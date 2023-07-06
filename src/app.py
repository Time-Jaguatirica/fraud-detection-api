from flask import Flask, render_template
from .services import KNNClassificator

app = Flask(__name__)
classificator = KNNClassificator()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/heatmap")
def heatmap():
    return render_template("heatmap.html")

@app.route("/features")
def get_features():
    return classificator.get_features()

if __name__ == "__main__":
    app.run(debug=True)
