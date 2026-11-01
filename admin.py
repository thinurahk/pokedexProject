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
    pass


# This function finds some desired English text from a list of dictionaries.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def extract_english(entries, key):
    pass


# This function repeatedly prompts for input until a valid Pokémon number is entered.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def choose_pokemon(prompt, data):
    pass


# This function opens the text file in write mode and writes data to it in JSON format.
# See Point 4 of the "Functions in admin.py" section of the assignment brief.
def save_data(data):
    pass


# Here is where you attempt to open the text file and read the data into a "data" variable.
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
        pass

        
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
