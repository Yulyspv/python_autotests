import pytest
import requests


def test_status_code_200():
    url = 'https://api.pokemonbattle-stage.me/v2/trainers'
    response = requests.get(url)
    assert response.status_code == 200


def test_id916():  
  
  response = requests.get ('https://pokemonbattle-stage.me/v2/trainers', params= {'trainer_id': '916'})
  response = response.json()
  
  assert response['data']['trainer_name'] == 'Юлия'
 