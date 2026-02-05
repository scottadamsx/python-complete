import tkinter as tk

def editValues():
    editValuesWindow = tk.Toplevel()
    editValuesWindow.title("Edit Values")
    editValuesWindow.geometry("200x200")

    label = tk.Label(editValuesWindow, text="Edit Values")
    label.grid(row=1, column=1)

    savingsLabel = tk.Label(editValuesWindow, text="Savings: ")
    savingsLabel.grid(row=2, column=1)

    savingsInput = tk.Entry(editValuesWindow)
    savingsInput.grid(row=2, column=2)

    debtLabel = tk.Label(editValuesWindow, text="Debt: ")
    debtLabel.grid(row=3, column=1)

    debtInput = tk.Entry(editValuesWindow)
    debtInput.grid(row=3, column=2)

    investmentsLabel = tk.Label(editValuesWindow, text="Investments: ")
    investmentsLabel.grid(row=4, column=1)

    investmentsInput = tk.Entry(editValuesWindow)
    investmentsInput.grid(row=4, column=2)

    def submit_values():
        try:
            savings = float(savingsInput.get())
            debt = float(debtInput.get())
            investments = float(investmentsInput.get())

            if savings + debt + investments != 1.00:
                print("Must add up to 100%")
            else:
                print("Values submitted successfully!")
        except ValueError:
            print("Please enter valid numbers.")

    submitValuesButton = tk.Button(editValuesWindow, text="Submit New Values", command=submit_values)
    submitValuesButton.grid(row=5, column=2)
