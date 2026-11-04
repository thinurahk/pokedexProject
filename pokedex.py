# Name:  Thinura Hewa Koonputugodage  
# Student Number:  10727799


# This is a starter file for "pokedex.py" in the Project of CSP1150 in Semester 2, 2026.
# It gives you just enough code to help ensure that your program is well structured.
# Use this file as the basis of your work.  You are not required to reference it.

# The "pass" commands do nothing:  They are placeholders to make the starter file run smoothly.
# Replace them with your own code as you complete the assignment.


# Import the required modules.
import tkinter
import tkinter.messagebox
import json


class ProgramGUI:
    def __init__(self):
        # This is the constructor of the class.
        # It is responsible for loading the data from the text file and creating the user interface.
        # See the "Constructor of the GUI Class of pokedex.py" section of the assignment brief.
        # Load the saved Pokemon data from the file.
        file = None

        try:
            file = open('pokemon.txt', 'r')
            self.data = json.load(file)

        except:
            tkinter.messagebox.showerror('File Error', 'Unable to load Pokemon data.')
            return

        finally:
            if file != None:
                file.close()

        # Check if the Pokemon list is empty.
        if len(self.data) == 0:
            tkinter.messagebox.showerror('Empty Pokédex', 'No Pokemon data found.')
            return

    def show_pokemon(self):
        # This method displays the image and details of the current Pokémon in the GUI.
        # See Point 1 of the "Methods in the GUI class of pokedex.py" section of the assignment brief.
        pass


    def previous(self):
        # This method decreases the index attribute to navigate to the prior Pokémon.
        # See Point 2 of the "Methods in the GUI class of pokedex.py" section of the assignment brief.
        pass


    def next(self):
        # This method decreases the index attribute to navigate to the next Pokémon.
        # See Point 3 of the "Methods in the GUI class of pokedex.py" section of the assignment brief.
        pass


# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
