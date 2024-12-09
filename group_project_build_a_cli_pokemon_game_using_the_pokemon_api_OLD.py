import requests
import json
import random

# Get the list of pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text) ['results']
# pokemon_list = json.loads(response.text)

### PRINT A LIST OF DICTIONARIES WHERE THE KEY = NAME, VALUE = API URL FOR THE NAME
#print(pokemon_list)

### PRINT A LIST OF NAMES
#list_of_names = []
# for pokemon in pokemon_list:
#     list_of_names.append(pokemon['name'])

list_of_names = []
for pokemon in pokemon_list:
    list_of_names.append(pokemon['name'])
#print(list_of_names)

length_of_pokemon_list = len(list_of_names)
random_pokemon_number = random.randint(0, length_of_pokemon_list - 1)
random_pokemon = list_of_names[random_pokemon_number]
cpu_pokemon_choice = random_pokemon
print(f"You will fight against: {cpu_pokemon_choice.capitalize()}")

# capitalise the first letter of each pokemon name
for i in range(len(list_of_names)):
    list_of_names[i] = list_of_names[i].capitalize()
#print(list_of_names)

print(f"You will now have to select your pokemon to fight from this list:\n{list_of_names}")
#
# Ask the user to choose a pokemon
print('Enter your pokemon:')
# Get the user's choice
choice = input().lower()

print(f"The fight will be between: {cpu_pokemon_choice.capitalize()} and {choice.capitalize()}\n")


### NEW CODE
# def fun(name_of_pokemon):
#     url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(name_of_pokemon)
#     response = requests.get(url)
#     pokemon_data = json.loads(response.text)
#
#     abilities = pokemon_data['abilities'][0]
#     ability = abilities['ability']
#
#     height = int(pokemon_data['height'])
#     weight = int(pokemon_data['weight'])
#     height_formatted = height / 10
#     weight_formatted = weight / 10
#
#     return ability, height_formatted, weight_formatted
#
# #print(fun(cpu_pokemon_choice))
# print(f"The characteristics of {cpu_pokemon_choice.capitalize()} are: {fun(cpu_pokemon_choice)}")

### STANDARD
## Get the pokemon's data from the API
# def display_characteristics(name_of_pokemon):
#     url = f'https://pokeapi.co/api/v2/pokemon/{name_of_pokemon}/'
#     response = requests.get(url)
#     pokemon_data = response.json()
#
#     ability = pokemon_data['abilities'][0]['ability']['name']
#     height_formatted = pokemon_data['height'] / 10
#     weight_formatted = pokemon_data['weight'] / 10
#
#     winning_factor = height_formatted / weight_formatted
#
#     print(f'Name: {pokemon_data["name"].capitalize()}')
#     print(f'Weight: {weight_formatted} (kgs)')
#     print(f'Height: {height_formatted} (m)')
#     print(f'Ability: {ability}')
#     print(f'Winning Factor: {winning_factor}')
#
#
#     return name_of_pokemon, height_formatted, weight_formatted, winning_factor


def calculate_characteristics(name_of_pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{name_of_pokemon}/'
    response = requests.get(url)
    pokemon_data = response.json()

    ability = pokemon_data['abilities'][0]['ability']['name']
    height_formatted = pokemon_data['height'] / 10
    weight_formatted = pokemon_data['weight'] / 10

    winning_factor = height_formatted / weight_formatted

    return ability, height_formatted, weight_formatted, winning_factor

def display_characteristics(name_of_pokemon):
    name, height, weight, winning_factor = calculate_characteristics(name_of_pokemon)

    print(f'Name: {name.capitalize()}')
    print(f'Weight: {weight} (kgs)')
    print(f'Height: {height} (m)')
    print(f'Winning Factor: {winning_factor}')












