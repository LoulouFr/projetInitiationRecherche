from flask import Flask, render_template, jsonify
import readCSV

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to your API"


@app.route("/citiesAvailable")
def citiesAvailable():
    return jsonify(readCSV.loadAllCitiesAvailable())


if __name__ == "__main__":
    app.run(debug=True)