import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
token = '9ee95b47facd2f62a3e522071bc68aab'
header = {'Content-Type': 'application/json', 'trainer_token': token}
TRAINER_ID = '33368'

def test_stat200():
    responce = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': TRAINER_ID})
    assert responce.status_code == 200

def test_trainer_name():
    responce = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert responce.status_code == 200
    assert responce.json()['data'][0]['trainer_name'] == 'Замай'
