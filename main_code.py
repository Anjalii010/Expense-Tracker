import tkinter as tk
from tkinter import messagebox

categories = ["Food", "Transportation", "Entertainment", "Utilities", "Others"]
expenses = {category: [] for category in categories}

def add_expense(category, amount):
    if category in expenses:
        expenses[category].append(float(amount))
        messagebox.showinfo("Expense Tracker", f"Added Rs{float(amount):.2f} to {category} expenses.")
    else:
        messagebox.showerror("Error", "Invalid category! Please choose from the predefined categories.")

def view_expenses():
    total_expenses = 0
    expense_report = "--- Total Expenses ---\n"
    for category, amounts in expenses.items():
        category_total = sum(amounts)
        total_expenses += category_total
        expense_report += f"{category}: Rs{category_total:.2f}\n"
    expense_report += f"Overall total expenses: Rs{total_expenses:.2f}"
    messagebox.showinfo("Expense Report", expense_report)

def category_expenses(category):
    if category in expenses:
        return sum(expenses[category])
    else:
        messagebox.showerror("Error", "Invalid category!")
        return 0

def add_expense_callback():
    category = category_var.get()
    amount = amount_entry.get()
    if not amount:
        messagebox.showerror("Error", "Please enter an amount!")
        return
    try:
        amount = float(amount)
        add_expense(category, amount)
        amount_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid amount! Please enter a valid number.")

def view_category_expenses_callback():
    category = category_var.get()
    category_total = category_expenses(category)
    messagebox.showinfo(f"{category} Expenses", f"Total {category} expenses: ${category_total:.2f}")

# Main application window
root = tk.Tk()
root.title("Expense Tracker")

# Category selection
category_var = tk.StringVar(root)
category_var.set(categories[0]) # default value

category_label = tk.Label(root, text="Choose Category:")
category_label.pack()

category_menu = tk.OptionMenu(root, category_var, *categories)
category_menu.pack()

# Amount entry
amount_label = tk.Label(root, text="Enter Amount:")
amount_label.pack()

amount_entry = tk.Entry(root)
amount_entry.pack()

# Add Expense button
add_button = tk.Button(root, text="Add Expense", command=add_expense_callback)
add_button.pack()

# View Total Expenses button
view_total_button = tk.Button(root, text="View Total Expenses", command=view_expenses)
view_total_button.pack()

# View Category Expenses button
view_category_button = tk.Button(root, text="View Category Expenses", command=view_category_expenses_callback)
view_category_button.pack()

# Run the Tkinter event loop
root.mainloop()
