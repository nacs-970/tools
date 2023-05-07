import os
import tkinter as tk
from playsound import playsound

# Function to play a sound file
def play_sound(sound_file):
    playsound(sound_file)

# Function to create the soundboard
def create_soundboard():
    # Get the list of sound files in the sounds directory
    sound_files = os.listdir('sounds')
    
    # Create a new window
    root = tk.Tk()
    root.title('Soundboard')
    
    # Loop over the sound files and create a button for each one
    for i, sound_file in enumerate(sound_files):
        # Compute the row and column of the button
        row = i // 3
        col = i % 3
        
        # Create a button
        button = tk.Button(root, text=sound_file, command=lambda sound=sound_file: play_sound(f'sounds/{sound}'))
        
        # Add the button to the grid
        button.grid(row=row, column=col)
    
    # Start the GUI main loop
    root.mainloop()

# Call the create_soundboard function to create the GUI
create_soundboard()

