import pytest
import requests

def test_status_code_200():
    url = "https://api.pokemonbattle-stage.me/v2/trainers"
    response = requests.get(url)
    assert response.status_code == 200


def test_id774():   
    url = "https://api.pokemonbattle-stage.me/v2/trainers?trainer_id=774&page=0"
    response = requests.get(url)
    response = response.json()
    assert response["trainer_name"] == "Юлия"

