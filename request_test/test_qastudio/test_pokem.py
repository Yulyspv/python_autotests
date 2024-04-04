import pytest
import requests

host='https://api.pokemonbattle-stage.me/v2'
token='92dec79899b03a3ad84bb2f80bffd945'



def test_status_code():
     response=requests.get(f'{host}/trainers', params={'trainer_id':916})
     assert response.status_code == 200

def test_trainer_name():
     response=requests.get(f'{host}/trainers', params={'trainer_id':916})
     assert response.json()["trainer_name"]=="Юлия"