import requests

URL = 'https://api.pokemonbattle.ru/v2'
token = '9ee95b47facd2f62a3e522071bc68aab'
header = {'Content-Type': 'application/json', 'trainer_token': token}

body_create = {
    "name": "Фимозавр",
    "photo_id": 12
}

body_change = {
    "pokemon_id": "330299",
    "name": "заноза",
    "photo_id": 35
}

body_catch = {
    "pokemon_id": "330299"
}


responce_create = requests.post(url=f'{URL}/pokemons', headers = header,json = body_create)
print(responce_create.text)

pokemon_id = responce_create.json()['id']
print(pokemon_id)


responce_change = requests.put(url=f'{URL}/pokemons', headers = header,json = body_change)
print(responce_change.text)


responce_catch = requests.post(url=f'{URL}/trainers/add_pokeball', headers = header,json = body_catch)
print(responce_catch.text)