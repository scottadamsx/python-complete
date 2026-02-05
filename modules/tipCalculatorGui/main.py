#! usr/bin/env python3
#  tip calculator gui

# must import tkinter to use it in the program
import tkinter as tk
from tkinter import messagebox

# create main window as 'root' and a title and geometry
root = tk.Tk()
root.title("TIP CALCULATOR")
root.geometry("300x300")

# create labal for cost input
costLabel = tk.Label(root, text="Cost of Meal:")
costLabel.pack()

# create cost input
costInput = tk.Entry(root)
costInput.pack()

# create label for tip percent
tipLabel = tk.Label(root, text="Tip Percentage:")
tipLabel.pack()

# create tip percent input
tipPercentInput = tk.Entry(root)
tipPercentInput.pack()

# when submit is clicked, program will grab these values,
# perform the calculations and display them in a messagebox
def get_results():
    cost = float(costInput.get())
    tipPercent = float(tipPercentInput.get())

    tipAmount = round(cost * tipPercent / 100, 2)
    totalCost = round(cost + tipAmount, 2)

    messagebox.showinfo("results",f"Tip amount: {tipAmount}\nTotal Cost: {totalCost}")
    tipPercentInput.delete(0,tk.END)
    costInput.delete(0,tk.END)

# create submit button
submit = tk.Button(root,command=get_results,text="submit")
submit.pack()


def main():
    # open window and run app
    root.mainloop()

if __name__ == "__main__":
    main()
