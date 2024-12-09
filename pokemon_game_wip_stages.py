import requests
import json
import random
import pprint

def calculate_characteristics(name_of_pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{name_of_pokemon}/'
    response = requests.get(url)
    pokemon_data = response.json()

    ability = pokemon_data['abilities'][0]['ability']['name']
    height_formatted = pokemon_data['height'] / 10
    weight_formatted = pokemon_data['weight'] / 10

    winning_factor = height_formatted / weight_formatted

    return name_of_pokemon, ability, height_formatted, weight_formatted, winning_factor

def add_pokemon_to_battle_dictionary(pokemon_characteristics, battle_dictionary):
    battle_dictionary[pokemon_characteristics[0]] = {
        "ability": pokemon_characteristics[1],
        "height_formatted": pokemon_characteristics[2],
        "weight_formatted": pokemon_characteristics[3],
        "winning_factor": pokemon_characteristics[4]
    }

# Get the list of Pokemon from the API
url = 'https://pokeapi.co/api/v2/pokemon/'
response = requests.get(url)
pokemon_list = json.loads(response.text) ['results']
# pokemon_list is a list where each item is a dictionary containing "name" and "url" as keys

# This code creates an empty list "list of names", and goes through pokemon_list, adding the "names" that were
# the keys
list_of_names = []
for pokemon in pokemon_list:
    list_of_names.append(pokemon['name'])

# This code chooses a random CPU character from the list of names
length_of_pokemon_list = len(list_of_names)
random_pokemon_number = random.randint(0, length_of_pokemon_list - 1)
random_pokemon = list_of_names[random_pokemon_number]
cpu_pokemon_choice = random_pokemon
print(f"You will fight against: {cpu_pokemon_choice.capitalize()}")

# This code prints out a list of pokemon names with capital letters for the user to choose from
for i in range(len(list_of_names)):
    list_of_names[i] = list_of_names[i].capitalize()
print(f"You will now have to select your pokemon to fight from this list:\n{list_of_names}")

# Ask the user to choose a pokemon
print('Enter your pokemon:')
# Get the user's choice
choice = input().lower()

# Logic to check if the user's choice is in the list of names
while choice.capitalize() not in list_of_names:
    print("Please enter a valid pokemon name:")
    choice = input().lower()

# Logic to check if the user's choice is the same as the CPU's choice. If it is, ask the user to choose again
while choice.capitalize() == cpu_pokemon_choice.capitalize():
    print("You can't choose the same pokemon as the CPU. Please choose again:")
    choice = input().lower()

# Display the who the battle is between
print(f"The fight will be between: {cpu_pokemon_choice.capitalize()} and {choice.capitalize()}\n")

# Create an empty dict to hold the battle data
pokemon_battle_dict = {}

# Create a function that will download the characteristics of each pokemon
# def calculate_characteristics(name_of_pokemon):
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
#     return name_of_pokemon, ability, height_formatted, weight_formatted, winning_factor

# Get the characteristics of the CPU pokemon and the user's choice
cpu_pokemon_characteristics = calculate_characteristics(cpu_pokemon_choice)
choice_characteristics = calculate_characteristics(choice)

# def add_pokemon_to_battle_dictionary(pokemon_characteristics, battle_dictionary):
#     battle_dictionary[pokemon_characteristics[0]] = {
#         "ability": pokemon_characteristics[1],
#         "height_formatted": pokemon_characteristics[2],
#         "weight_formatted": pokemon_characteristics[3],
#         "winning_factor": pokemon_characteristics[4]
#     }

add_pokemon_to_battle_dictionary(cpu_pokemon_characteristics, pokemon_battle_dict)
add_pokemon_to_battle_dictionary(choice_characteristics, pokemon_battle_dict)


pprint.pprint(pokemon_battle_dict)
print("\n")

# Print the battle data for each pokemon
for pokemon, data in pokemon_battle_dict.items():
    print(f"Name: {pokemon.capitalize()}")
    print(f"Ability: {data['ability']}")
    print(f"Weight: {data['weight_formatted']}kg")
    print(f"Height: {data['height_formatted']}m")
    print(f"Winning factor: {data['winning_factor']}\n")

#print("\n")

# Determine the winner of the battle
for name, values in pokemon_battle_dict.items():
    print(f"The Pokemon {name.capitalize()} has the winning factor {values['winning_factor']}")

print("\n")

if pokemon_battle_dict[cpu_pokemon_choice]['winning_factor'] > pokemon_battle_dict[choice]['winning_factor']:
    print(f"{cpu_pokemon_choice.capitalize()} - on behalf of the CPU - wins!")
elif pokemon_battle_dict[cpu_pokemon_choice]['winning_factor'] < pokemon_battle_dict[choice]['winning_factor']:
    print(f"{choice.capitalize()} wins! You win!")
else:
    print("It's a draw!")







