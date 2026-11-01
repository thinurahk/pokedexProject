# Name:  Thinura Hewa Koonputugodage  
# Student Number:  10727799

# This is a starter file for "admin.py" in the Project of CSP1150 in Semester 2, 2026.
# It gives you just enough code to help ensure that your program is well structured.
# Use this file as the basis of your work.  You are not required to reference it.

# The "pass" commands do nothing:  They are placeholders to make the starter file run smoothly.
# Replace them with your own code as you complete the assignment.


# Import necessary module(s).
import json
import urllib.request
import os


# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input != '':
            return user_input

# This function finds some desired English text from a list of dictionaries.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def extract_english(entries, key):
    for entry in entries:
        if entry['language']['name'] == 'en':
            return entry[key]
    


# This function repeatedly prompts for input until a valid Pokémon number is entered.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def choose_pokemon(prompt, data):
    pass


# This function opens the text file in write mode and writes data to it in JSON format.
# See Point 4 of the "Functions in admin.py" section of the assignment brief.
def save_data(data):
    file = open('pokemon.txt', 'w')
    json.dump(data, file,indent=4)
    file.close()

# Here is where you attempt to open the text file and read the data into a "data" variable

try:
    file = open('pokemon.txt', 'r')
    data = json.load(file)
    file.close()
except:
    data = []

# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.


# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Pokédex Administration Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower()


    if choice == 'a':
        # Add a new Pokémon.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.
        pokemon_name = input_something('Enter a Pokémon Name : ')
        pokemon_name = pokemon_name.lower()
        pokemon_name = pokemon_name.replace('.', ' ')
        pokemon_name = pokemon_name.replace("'", ' ')
        pokemon_name = pokemon_name.replace(' ', '-')
        pokemon_name = pokemon_name.replace(':', '')

        url = f'https://pokeapi.co/api/v2/pokemon-species/'+ pokemon_name
        request = urllib.request.Request(url,headers={'User-Agent':10727799 })

        try: 
            response = urllib.request.urlopen(request)
            species_data = json.load(response)
            response.close()

        except urllib.error.HTTPError:
            print('Pokémon not found.')       

        else:
            pokemon_number = species_data['pokedex_numbers'][0]['entry_number']
            pokemon_exists = False
            for pokemon in data:
                if pokemon['number'] == pokemon_number:
                    pokemon_exists = True

            if pokemon_exists:
                print('This Pokémon is already in your Pokédex.') 

            else:
                pomemon_name = extract_english(species_data['names'], 'name')
                pokemon_category = extract_english(species_data['genera'], 'genus')

                evolves_from = None

                if species_data['evolves_from_species'] != None:
                    previous_name = species_data['evolves_from_species']['names']

                    previous_url = species_data['evolves_from_species']['url']
                    previous_request = urllib.request.Request(previous_url,headers={'User-Agent':10727799 })
                    previous_response = urllib.request.urlopen(previous_request)    
                    previous_name = json.load(previous_response)
                    previous_response.close()

                print(f'Pokémon {pomemon_name} added to your Pokédex.')
                print('category:', pokemon_category)


    elif choice == 'l':
        # List current Pokémon.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        pass


    elif choice == 's':
        # Search current Pokémon.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        pass


    elif choice == 'v':
        # View details of a Pokémon.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        pass


    elif choice == 'd':
        # Delete a Pokémon.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        pass


    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        pass


    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        pass
