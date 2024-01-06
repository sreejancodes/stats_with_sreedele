import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    countries_file = pd.read_csv("static/countries.txt", sep="\t")
    return render_template('index.html', countries = countries_file.to_dict(orient='records'))

@app.route("/success", methods = ["POST"])
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)