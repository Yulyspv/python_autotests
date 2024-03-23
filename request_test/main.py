import requests

data_pokemon1 = {"name" : "Козявка", "photo" : "https://dolnikov.ru/pokemons/albums/001.png"}

response = requests.post("https://api.pokemonbattle-stage.me/v2/pokemons", json = data_pokemon1, headers={"trainer_token" : "1d75353e14d00a829d1a015c39a40b2b"})

print(response.text)


import requests

data_pokemon2 = {
    "pokemon_id": "2430",
    "name": "казявамазява",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response = requests.put("https://api.pokemonbattle-stage.me/v2/pokemons", json = data_pokemon2, headers={"trainer_token" : "1d75353e14d00a829d1a015c39a40b2b"})

print(response.text)


import requests

data_pokemon3 = {
    "pokemon_id": "2430"
}

response = requests.post("https://api.pokemonbattle-stage.me/v2/trainers/add_pokeball", json = data_pokemon3, headers={"trainer_token" : "1d75353e14d00a829d1a015c39a40b2b"})

print(response.text)