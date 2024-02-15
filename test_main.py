import pytest
import requests

def test_getVilles():
    response = requests.get("http://127.0.0.1:5000/villes")
    assert response.status_code ==200
    assert response.json() == ['Berlin', 'Londres', 'New York', 'Rome', 'Madrid', 'Sydney', 'Dubai', 'Moscou', 'Paris', 'Tokyo']