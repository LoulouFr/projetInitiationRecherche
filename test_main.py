import pytest
import requests

def test_getVilles():
    response = requests.get("http://127.0.0.1:5000/villes")
    assert response.status_code ==200
    assert response.json() == ['Berlin', 'Londres', 'New York', 'Rome', 'Madrid', 'Sydney', 'Dubai', 'Moscou', 'Paris', 'Tokyo']


def test_getVille():
    response = requests.get("http://127.0.0.1:5000/ville/Berlin")
    assert response.status_code == 200
    assert response.json()[0] == {'Ville': 'Berlin', 'Quartier': 'Est', 'Prix au m²': 19393}


def test_quartierParVille():
    response = requests.get("http://127.0.0.1:5000/quartierParVille/Berlin/Moderne")
    assert response.status_code == 200
    assert response.json()[0] == {'Ville': 'Berlin', 'Quartier': 'Moderne', 'Prix au m²': 5493}


def test_prixMoyen():
    response = requests.get("http://127.0.0.1:5000/prixMoyenVille/Berlin")
    assert response.status_code == 200
    assert response.json() == {'prix_moyen': '14681.234693877552'}