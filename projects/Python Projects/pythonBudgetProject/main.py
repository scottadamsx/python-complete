# usr/bin/env python3
# Budget GUI

import tkinter as tk
import editValuesMenu

balance = 46.98
savings = 0.30
investments = 0.10
debt = 0.40

root = tk.Tk()
root.title("Scott's Budget")
root.geometry("300x300")

balanceLabel = tk.Label(root, text=f"Balance: ${balance}")
balanceLabel.grid(row=1,column=1)



# values menu
valuesTitle = tk.Label(root, text="Values")
valuesTitle.grid(row=1, column=19, columnspan=2)

savingsLabel = tk.Label(root, text=f"Savings: {savings}")
savingsLabel.grid(row=2, column="20")

investmentsLabel = tk.Label(root, text=f"Investments: {investments}")
investmentsLabel.grid(row=4, column="20")

savingsLabel = tk.Label(root, text=f"debt: {debt}")
savingsLabel.grid(row=5, column="20")



editValuesButton = tk.Button(root,  text="edit values", command=editValuesMenu.editValues)
editValuesButton.grid(row=6, column="20")

root.mainloop()