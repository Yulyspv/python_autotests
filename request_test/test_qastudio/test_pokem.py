import pytest
import requests


def test_status_code_200():
    url = 'https://api.pokemonbattle-stage.me/v2/trainers'
    response = requests.get(url)
    assert response.status_code == 200


def test_id774():   
    
    response = requests.get('https://api.pokemonbattle-stage.me/v2/trainers',  params={'trainer_id':'774'})
    response = response.json()
    assert response['trainer_name'] == 'Юлия'

