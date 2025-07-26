"""
Module 08 Final Project
Dale Hendren
7/26/2025

This program manages a door prize game using a graphical interface. Participants enter their name and 
submit a guess between 1 and 10. Each entry is stored in a list and evaluated when the “Show Results” 
button is clicked.
A random winning number is generated, and any participants who guessed it correctly are declared Grand Prize Winners. 
Their names, guesses, and a prize image are displayed.
From the remaining non-winning participants, the program randomly selects up to two runner-up winners to receive 
additional prizes. These runner-up winners are presented in the order they were selected, each paired with a corresponding prize 
image.
All entries are listed, all winners are revealed with their prizes, and the randomly selected number that determined the outcome 
is announced at the top of the results window.

"""




import tkinter as tk
from tkinter import messagebox
# import the function from the second file
from prize_results import show_results  

# creates list for employee name and guess
employeeGuess = []

# creates DoorPrize class
class DoorPrize(tk.Tk):
    def __init__(self):
        super().__init__()
        # creates title
        self.title("Guess a Number to Win a Prize")
        # creates resizable window
        self.resizable(True, True)

        # create label and entry for employee name
        tk.Label(self, text="Employee Name").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self, width=20)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # creates label and entry for guess
        tk.Label(self, text="Guess a number from 1-10").grid(row=1, column=0, padx=5, pady=5)
        self.guess_entry = tk.Entry(self, width=10)
        self.guess_entry.grid(row=1, column=1, padx=5, pady=5)

        # creates button panel (frame) with black background
        button_frame = tk.Frame(self, bg="black")
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        # adds "Enter" button
        tk.Button(button_frame, text="Enter", command=self.enter).grid(row=0, column=0, padx=5)
        # adds "Result" button and calls "show_reselts" function from "prize_results.py"
        tk.Button(button_frame, text="Results", command=lambda: show_results(self, employeeGuess)).grid(row=0, column=1, padx=5)
        # adds "Quit" button to end program (destroy)
        tk.Button(button_frame, text="QUIT", command=self.destroy).grid(row=0, column=2, padx=5)

    # craete "enter" function
    def enter(self):
        # gets name from entry
        name = self.name_entry.get()
        # gets guess from entry
        guess = self.guess_entry.get()
        try:
            # validates name, makes sure it is not empty
            if not name:
                raise ValueError("Name cannot be empty.")
            if not guess:
                raise ValueError("Guess Missing")
             # converts guess to integer
            guess_num = int(guess)
            # validates gues, makes sure from 1 to 10
            if not (1 <= guess_num <= 10):
                raise ValueError("Guess must be between 1 and 10.")
            # if valid adds name and guess to the list
            employeeGuess.append([name, guess_num])
            # clear entry fields for next employee and guess
            self.name_entry.delete(0, tk.END)
            self.guess_entry.delete(0, tk.END)
        except ValueError as e:
            # Show error message for invalid input
            messagebox.showerror("ERROR", str(e))

def main():
    # create and runs the main application window
    app = DoorPrize()
    # starts Tkinter loop
    app.mainloop()

if __name__ == "__main__":
    main()