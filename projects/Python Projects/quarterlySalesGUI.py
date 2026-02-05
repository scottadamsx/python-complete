#! /usr/bin/env python3

# The Quarterly Sales Program GUI

import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("The Quarterly Sales Program")
root.geometry("400x400")

# Create label and entry for Q1
q1_label = tk.Label(root, text="Enter sales for Q1: ")
q1_label.grid(row=0, column=0)
quarter1 = tk.Entry(root)
quarter1.grid(row=0, column=1)

# Create label and entry for Q2
q2_label = tk.Label(root, text="Enter sales for Q2: ")
q2_label.grid(row=1, column=0)
quarter2 = tk.Entry(root)
quarter2.grid(row=1, column=1)

# Create label and entry for Q3
q3_label = tk.Label(root, text="Enter sales for Q3: ")
q3_label.grid(row=2, column=0)
quarter3 = tk.Entry(root)
quarter3.grid(row=2, column=1)

# Create label and entry for Q4
q4_label = tk.Label(root, text="Enter sales for Q4: ")
q4_label.grid(row=3, column=0)
quarter4 = tk.Entry(root)
quarter4.grid(row=3, column=1)


# Function to process the sales data
def submit_button():
    try:
        Q1 = float(quarter1.get())
        Q2 = float(quarter2.get())
        Q3 = float(quarter3.get())
        Q4 = float(quarter4.get())

        quarterly_sales = [Q1, Q2, Q3, Q4]
        total = sum(quarterly_sales)
        average = total / 4
        sorted_quarterly_sales = sorted(quarterly_sales)
        lowest = sorted_quarterly_sales[0]
        highest = sorted_quarterly_sales[-1]

        # Display the results in a message box
        messagebox.showinfo(
            "Sales Evaluation",
            f"Total Sales: {total:.2f}\n"
            f"Average Quarter: {average:.2f}\n"
            f"Lowest Quarter: {lowest}\n"
            f"Highest Quarter: {highest}"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for all quarters.")


# Submit button
submit = tk.Button(root, text="Submit Sales for Evaluation", command=submit_button)
submit.grid(row=4, column=1)

# Run the application
root.mainloop()
