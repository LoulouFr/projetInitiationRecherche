from flask import Flask, render_template, jsonify
import readCSV

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to your API"


@app.route('/villes', methods=['GET'])
def citiesAvailable():
    return jsonify(readCSV.loadAllCitiesAvailable())


@app.route('/ville/<string:ville>', methods=['GET'])
def city(ville):
    return jsonify(readCSV.getCity(ville).toList())


@app.route('/quartier/<string:quartier>', methods=['GET'])
def quartier(quartier):
    return jsonify(readCSV.quartier(quartier).toList())


if __name__ == '__main__':
    app.run(debug=True)