'''
prize_results.py
Dale Hendren
7/26/2025

This module displays the result window, showing all entries and identifying winners.

'''



import tkinter as tk
import random

# creates lists to store winners and runner up winners
winners = []
randomWinners = []

# create the function "show_results"
def show_results(parent, employeeGuess):
    """
    Displays the results window with all entries, grand prize winner(s), and runner-up winners.
    Shows prize images and names for each winner.
    """
    # validates the entrys have been make
    if not employeeGuess:
        from tkinter import messagebox
        # creates error messgae if no entries have been made and ends
        messagebox.showinfo("Results", "No entries yet.")
        return

    # generate the random winning number (1 to 10)
    ranNo = random.randint(1, 10)
    # clears previous winner
    winners.clear()
    # clears previous runner up
    randomWinners.clear()

    # get all entries from "employeeGuess" that guessed the winning number
    for entry in employeeGuess:
        if entry[1] == ranNo:
            # add correct guesses to "winner" list
            winners.append(entry)

    # pick one random winner is no one guesses correctly
    if not winners and employeeGuess:
        # add the randomly picked winner to the "winner" list
        winners.append(random.choice(employeeGuess))

    # gets all entries in "employGuess" that are not in "winner"
    non_winners = [entry for entry in employeeGuess if entry not in winners]
    # checks if there are more entries than the two prizes
    if len(non_winners) >= 2:
        # randonmly selects 2 winners from the "non_winner" list as runner ups
        randomWinners.extend(random.sample(non_winners, 2))
    else:
        # if more prizes than entries, all "non_winners" added to "randomWinners" runner ups
        randomWinners.extend(non_winners)

    # path to prize image files
    prize_files = [
        "prizes/Grand Prize.png",      # Grand Prize
        "prizes/The Candle.png",      # 1st runner up
        "prizes/The Cool Pens.png"    # 2nd runner up
    ]

    # creates the results window and puts it on to
    result_win = tk.Toplevel(parent)
    # creates title for "Entries & Winners"
    result_win.title("Entries & Winners")
    # sets the dimension of the windows width x height
    result_win.geometry("600x1200")
    # sets the background to lightblue
    result_win.configure(bg="lightblue")

    # displays the random number
    tk.Label(result_win, text=f"Random Number: {ranNo}", font=("Arial", 16), bg="lightblue").pack(pady=5)

    # creates label for entries "All Entries"
    tk.Label(result_win, text="All Entries:", font=("Arial", 14, "bold"), bg="lightblue").pack()
    # displays all employees and guesses
    for entry in employeeGuess:
        tk.Label(result_win, text=f"{entry[0]} - Guess: {entry[1]}", bg="lightblue").pack()

    # display grand prize winners and their prize image
    tk.Label(result_win, text="\nGrand Prize Winner(s):", font=("Arial", 12, "bold"), bg="lightblue").pack()
    # display every winner and their guess
    for winner in winners:
        tk.Label(result_win, text=f"{winner[0]} - Guess: {winner[1]}", bg="lightblue").pack()
        # gets the grand prize image
        img_path = prize_files[0]
        # loads image using Tkinter PhotoImage (image must be PNG/GIF and already sized)
        photo = tk.PhotoImage(file=img_path)
        # craete label to display image
        img_label = tk.Label(result_win, image=photo, bg="lightblue")
        # holds image so it doesn't get removed
        img_label.image = photo 
        # display the image
        img_label.pack()
        # splits the file name at the "." and removes everything past it
        prize_name = img_path.split("/")[-1].rsplit(".", 1)[0]
        # displays the stripped filename as the prize name
        tk.Label(result_win, text=prize_name, font=("Arial", 10), bg="lightblue").pack() 
                    
    # display for the runner up winners and their prize images
    tk.Label(result_win, text="\nRunner-Up Prizes:", font=("Arial", 12, "bold"), bg="lightblue").pack()
    # uses index to go through each runner up and images for each loop
    for idx, runnerUp in enumerate(randomWinners):
        # displays the runner up name and guess
        tk.Label(result_win, text=f"{runnerUp[0]} - Guess: {runnerUp[1]}", bg="lightblue").pack()
        # gets the next image for the runner up, counter using index
        img_path = prize_files[idx+1]
        # loads image using Tkinter PhotoImage (image must be PNG/GIF and already sized)
        photo = tk.PhotoImage(file=img_path)
        # creates label to display image
        img_label = tk.Label(result_win, image=photo, bg="lightblue")
        # holds image so it doesn't get removed
        img_label.image = photo
        # displays the image
        img_label.pack()
        # splits the file name at the "." and removes everything past it
        prize_name = img_path.split("/")[-1].rsplit(".", 1)[0]
        # displays the stripped filename as the prize name
        tk.Label(result_win, text=prize_name, font=("Arial", 10), bg="lightblue").pack()