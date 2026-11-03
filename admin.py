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
    while True:
        try:
            pokemon_number = int(input(prompt))
            for pokemon in data:
                if pokemon['number'] == pokemon_number:
                    return pokemon

            print('Pokemon number not found. try again.')

        except ValueError:
            print('Please enter a valid number.')


# This function opens the text file in write mode and writes data to it in JSON format.
# See Point 4 of the "Functions in admin.py" section of the assignment brief.
def save_data(data):
    file = open('pokemon.txt', 'w')
    json.dump(data, file,indent=4)
    file.close()

# Here is where you attempt to open the text file and read the data into a "data" variable

# Load the saved Pokémon data from the file.
file = None
try:
    file = open('pokemon.txt', 'r')
    data = json.load(file)
except:
    data = []
finally:    
    if file != None:
        file.close()


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
        
        # Format the Pokemon name for the API request.
        pokemon_name = pokemon_name.lower()
        pokemon_name = pokemon_name.replace('.', '')
        pokemon_name = pokemon_name.replace("'", '')
        pokemon_name = pokemon_name.replace(':', '')
        pokemon_name = pokemon_name.replace(' ', '-')

        url = 'https://pokeapi.co/api/v2/pokemon-species/' + pokemon_name
        request = urllib.request.Request(url,headers={'User-Agent':'10727799' })

        try: 
            response = urllib.request.urlopen(request)
            species_data = json.load(response)
            response.close()

        except urllib.error.HTTPError:
            print('Pokemon not found.')       

        else:
            
            pokemon_number = species_data['pokedex_numbers'][0]['entry_number']  # Get the national Pokédex number.


            pokemon_exists = False         # Check whether the Pokémon already exists.


            for pokemon in data:
                if pokemon['number'] == pokemon_number:
                    pokemon_exists = True

            if pokemon_exists:
                print('This Pokémon is already in your Pokédex.') 

            else:
                pokemon_name = extract_english(species_data['names'], 'name')
                pokemon_category = extract_english(species_data['genera'], 'genus')

                evolves_from = None    # Get the previous evolution, if applicable.


                if species_data['evolves_from_species'] != None:
                    previous_name = species_data['evolves_from_species']['name']

                    previous_url = 'https://pokeapi.co/api/v2/pokemon-species/' + previous_name
                    previous_request = urllib.request.Request(previous_url,headers={'User-Agent':'10727799' })
                 
                    previous_response = urllib.request.urlopen(previous_request)
                    previous_data = json.load(previous_response)
                    previous_response.close()

                    evolves_from = extract_english(previous_data['names'], 'name')

                print(pokemon_name , 'found!')
                print('Pokedex Number:', pokemon_number)
                print('Category:', pokemon_category)

                 # Get the rest of the Pokemon details.
                pokemon_url = 'https://pokeapi.co/api/v2/pokemon/' + str(pokemon_number)
                pokemon_request = urllib.request.Request(pokemon_url,
                                                        headers={'User-Agent':'10727799' })

                pokemon_response = urllib.request.urlopen(pokemon_request)
                pokemon_data = json.load(pokemon_response)
                pokemon_response.close()

                # Convert the height and weight into metres and kilograms.
                pokemon_height = pokemon_data['height'] / 10
                pokemon_weight = pokemon_data['weight'] / 10

                #Get the types of the Pokemon.
                pokemon_types = []

                for type_data in pokemon_data['types']:
                    pokemon_types.append(type_data['type']['name'])

                # Get pokeemon image. 
                image_url = pokemon_data['sprites']['front_default']

                # Create the images folder if it does not exist.
                if not os.path.exists('images'):
                    os.makedirs('images')

                # Download the image and save it to the images folder using pokemon number.
                image_request = urllib.request.Request(image_url, 
                                        headers={'User-Agent': '10727799'}) 
                image_response = urllib.request.urlopen(image_request)
                image_file = open('images/' + str(pokemon_number) + '.png', 'wb')
                image_file.write(image_response.read())
                image_file.close()
                image_response.close()

                #create a dicttionary with the pokemon details
                new_pokemon = {
                    "name": pokemon_name,
                    "number": pokemon_number,
                    "category": pokemon_category,
                    "height": pokemon_height,
                    "weight": pokemon_weight,
                    "types": pokemon_types,
                }

                
                # Add the previous evolution if the Pokémon has one.
                if evolves_from != None:
                    new_pokemon["evolves_from"] = evolves_from

                # Add the new Pokémon to the list.    
                data.append(new_pokemon)

                # Sort the Pokémon list by Pokédex number.
                data.sort(key=lambda pokemon: pokemon['number'])

                # Save the updated Pokémon list.
                save_data(data)

                print(pokemon_name, 'added to your Pokedex!')


    elif choice == 'l':
        # List current Pokémon.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        
        if len(data) == 0:
            print('Your pokedex is empty.')
        else:
            print('Your pokedex Contains :')
            for pokemon in data:
                pokemon_number = str(pokemon['number'])
                while len(pokemon_number) < 4:
                    pokemon_number = '0' + pokemon_number
                print('#' + pokemon_number +" : ", pokemon['name'])



    elif choice == 's':
        # Search current Pokémon.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
                                
        if len(data) == 0:           # Check if the Pokedex is empty
            print('Your Pokedex is empty.')

        else:
            # Ask the user for a search term.
            search_term = input_something('Please Enter search term: ').lower()

            found = False

            print('Search results:')

            # Go through each Pokemon in the list.
            for pokemon in data:

                # Check if the search term is in the name or category.
                if search_term in pokemon['name'].lower() or search_term in pokemon['category'].lower():

                    pokemon_number = str(pokemon['number'])
                    while len(pokemon_number) < 4:
                        pokemon_number = '0' + pokemon_number

                    print('#' + pokemon_number + ' : ' + pokemon['name'])

                    found = True

            # Display a message if no Pokemon matched.
            if found == False:
                print('No Pokemon found.')        


    elif choice == 'v':
        # View details of a Pokémon.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.

        if len(data) == 0:
            print('Your Pokedex is empty.')

        else:
            # Ask the user to choose a Pokemon.
            pokemon = choose_pokemon('Pokemon number to view: ', data)

            # Format the Pokemon number with four digits.
            pokemon_number = str(pokemon['number'])

            while len(pokemon_number) < 4:
                pokemon_number = '0' + pokemon_number

            # Display the Pokemon details.
            print(pokemon['name'] + ' [#' + pokemon_number + ']')
            print('  ' + pokemon['category'])

            # Display the Pokemon types.
            pokemon_types = ''

            for pokemon_type in pokemon['types']:
                if pokemon_types == '':
                    pokemon_types = pokemon_type.capitalize()
                else:
                    pokemon_types = pokemon_types + ', ' + pokemon_type.capitalize()

            print('  Type: ' + pokemon_types)

                # Use capitalize() to make the first letter of each Pokemon type uppercase.
                # Reference: Python Documentation - str.capitalize()
                # https://docs.python.org/3/library/stdtypes.html#str.capitalize

            # Display the Pokemon height and weight.
            print('  Size: ' + str(pokemon['height']) + 'm, ' + str(pokemon['weight']) + 'kg')

            # Display the previous evolution if it exists.
            if 'evolves_from' in pokemon:
                print('  Evolves from ' + pokemon['evolves_from'])        


    elif choice == 'd':
        # Delete a Pokemon.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
                                      
                                      
        if len(data) == 0:         # Check if the Pokedex is empty.
            print('Your Pokedex is empty.')

        else:
            # Ask the user to choose a Pokémon to delete.
            pokemon = choose_pokemon('Pokemon number to delete: ', data)

            # Delete the Pokemon from the list.
            data.remove(pokemon)

            # Delete the Pokemon image from the images folder.
            os.remove('images/' + str(pokemon['number']) + '.png')

            # Save the updated Pokemon list.
            save_data(data)

            print(pokemon['name'] + ' deleted from your Pokedex.')


    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        pass


    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        pass
