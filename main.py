import requests
import json
token = '12b0a7adf8e69668db368cb063381a9e'
response = requests.post ('https://pokemonbattle.me:5000/pokemons',headers = {'Content-Type' : 'application/json',
'trainer_token' : token},
json = {
    "name": "Opponent",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})
pokemon_id = response.json()['id']
response_change = requests.put('https://pokemonbattle.me:5000/pokemons',headers = {'Content-Type' : 'application/json',
'trainer_token' : token}, json ={
    "pokemon_id": pokemon_id,
    "name": "Opponent 86",
    "photo": "" 
    })
response = requests.post ('https://pokemonbattle.me:5000/pokemons/trainers/add_pokeball',headers = {'Content-Type' : 'application/json',
'trainer_token' : token},
json = {
    "pokemon_id": "2565"
})
print (response_change.text) 