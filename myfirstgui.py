import tkinter as tk
from tkinter import messagebox
import os
import sys

# Create the main window
myfirstwindow = tk.Tk()
myfirstwindow.title("My first window")
myfirstwindow.geometry("400x300")

# Create a label for the entry field below
label = tk.Label(myfirstwindow, text="Please enter entry below:")
label.pack()

# Create an entry field to input an entry
entry = tk.Entry(myfirstwindow)
entry.pack()

# Define function to submit the entry
def submit_entry():
    submitted_entry = entry.get().strip()  # Remove leading/trailing whitespace
    print(f"Submitted entry: '{submitted_entry}'")  # Debugging: check what is being captured

    if submitted_entry:  # Only write to file if there is text
        with open("list_of_entries.txt", "a") as file:
            file.write(submitted_entry + "\n")  # Write the entry followed by a new line
        # Optional: Show a message box after saving the entry
        messagebox.showinfo("Success", "Entry added to file!")
        myfirstwindow.destroy()
    else:
        messagebox.showwarning("Warning", "Please enter some text.")

# Create submit button that calls the submit_entry function
submit = tk.Button(myfirstwindow, text="Click here to add entry to file", command=submit_entry)
submit.pack()

# Start the GUI loop
myfirstwindow.mainloop()
