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
            tkinter.messagebox.showerror('Empty Pokedex', 'No Pokemon data found.')
            return


        self.main = tkinter.Tk()    #create the main window 
        self.main.title("Thinura's Pokedex")

        self.index = 0  #keep track of the current pokemon

        self.top_frame = tkinter.Frame(self.main)
        self.bottom_frame = tkinter.Frame(self.main)

        #Create the Previous button.
        self.previous_button = tkinter.Button(
            self.top_frame,
            text='<',
            command=self.previous
        )
        self.previous_button.pack(side='left')

        #Create the Pokemon name label.
        self.name_label = tkinter.Label(
            self.top_frame,
            text='Pokemon Name [#0000]',
            font=('Arial', 14, 'bold')
        )
        self.name_label.pack(side='left', padx=15)

        #Create the Next button.
        self.next_button = tkinter.Button(
            self.top_frame,
            text='>',
            command=self.next
        )
        self.next_button.pack(side='left')

        #Create a label for the Pokemon image.
        self.photo = None
        self.image_label = tkinter.Label(
            self.bottom_frame,
            text='Pokemon image'
        )
        self.image_label.pack(side='left', padx=10)

        #Create a frame for the Pokemon details.
        self.details_frame = tkinter.Frame(self.bottom_frame)
        self.details_frame.pack(side='left', padx=10)

        #Create labels for the Pokemon details.
        self.category_label = tkinter.Label(
            self.details_frame,
            text='Category'
        )
        self.category_label.pack(anchor='w')

        self.types_label = tkinter.Label(
            self.details_frame,
            text='Type: '
        )
        self.types_label.pack(anchor='w')

        self.size_label = tkinter.Label(
            self.details_frame,
            text='Size: '
        )
        self.size_label.pack(anchor='w')

        self.evolves_label = tkinter.Label(
            self.details_frame,
            text=''
        )
        self.evolves_label.pack(anchor='w')

        #Display the frames in the main window.
        self.top_frame.pack(pady=5)
        self.bottom_frame.pack(padx=10, pady=10)

     
        self.show_pokemon()   #Display the first Pokemon.
        tkinter.mainloop()     #Start the GUI main loop.
        

    def show_pokemon(self):
        # This method displays the image and details of the current Pokémon in the GUI.
        # See Point 1 of the "Methods in the GUI class of pokedex.py" section of the assignment brief.
        pokemon = self.data[self.index]

        pokemon_number = str(pokemon['number'])  # Display the Pokemon name and number.

        while len(pokemon_number) < 4:
            pokemon_number = '0' + pokemon_number

        self.name_label.config(
            text=pokemon['name'] + ' [#' + pokemon_number + ']'
        )

     
        self.photo = tkinter.PhotoImage(                        # Display the Pokemon image.
            file='images/' + str(pokemon['number']) + '.png'
        )  

        self.image_label.config(image=self.photo, text='')

      
        self.category_label.config(text=pokemon['category'])   # Display the Pokemon category.

       
        pokemon_types = ''    # Display the Pokemon types.

        # Use capitalize() to make the first letter of each Pokemon type uppercase.
        # Reference: Python Documentation - str.capitalize()
        # https://docs.python.org/3/library/stdtypes.html#str.capitalize

        for pokemon_type in pokemon['types']:
            if pokemon_types == '':
                pokemon_types = pokemon_type.capitalize()
            else:
                pokemon_types = pokemon_types + ', ' + pokemon_type.capitalize()

        self.types_label.config(text='Type: ' + pokemon_types)

        # Display the Pokemon height and weight.
        self.size_label.config(
            text='Size: ' + str(pokemon['height']) + 'm, '
            + str(pokemon['weight']) + 'kg'
        )


        if 'evolves_from' in pokemon:                  # Display the previous evolution if it exists.
            self.evolves_label.config(
                text='Evolves from ' + pokemon['evolves_from']
            )
        else:
            self.evolves_label.config(text='')    


    def previous(self):
        # This method decreases the index attribute to navigate to the prior Pokémon.
        # See Point 2 of the "Methods in the GUI class of pokedex.py" section of the assignment brief.
        if self.index > 0:          # Go to the previous Pokemon if one exists.
            self.index = self.index - 1
            self.show_pokemon()


    def next(self):
        # See Point 3 of the "Methods in the GUI class of pokedex.py" section of the assignment brief.

        if self.index < len(self.data) - 1:         # Go to the next Pokemon if one exists.
            self.index = self.index + 1
            self.show_pokemon()  

# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
