import sqlite3
import csv
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd

# Initialize SQLite database
conn = sqlite3.connect('expense_tracker.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute("CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, category TEXT, description TEXT, amount REAL, date TEXT)")
conn.commit()
conn.close()

# Main Class for the Expense Tracker


class ExpenseTracker:

    def __init__(self, master):
        self.master = master
        self.master.title('Expense Tracker')
        self.master.geometry('600x400')

        # Labels and Entry boxes
        Label(master, text='Category').grid(row=0, column=0)
        Label(master, text='Description').grid(row=1, column=0)
        Label(master, text='Amount').grid(row=2, column=0)

        self.category = Entry(master)
        self.description = Entry(master)
        self.amount = Entry(master)

        self.category.grid(row=0, column=1)
        self.description.grid(row=1, column=1)
        self.amount.grid(row=2, column=1)

        # Buttons
        Button(master, text='Add Expense',
               command=self.add_expense).grid(row=3, column=0)
        Button(master, text='Show Expenses',
               command=self.show_expenses).grid(row=3, column=1)
        Button(master, text='Visualize Data',
               command=self.visualize_data).grid(row=3, column=2)
        Button(master, text='Export to CSV',
               command=self.export_csv).grid(row=3, column=3)

    # Placeholder methods

    def add_expense(self):
        category = self.category.get()
        description = self.description.get()
        amount = self.amount.get()
        date = pd.to_datetime('today').strftime('%Y-%m-%d')

        if not category or not description or not amount:
            messagebox.showwarning(
                "Incomplete Entry", "Please fill all the fields")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showwarning(
                "Invalid Amount", "Please enter a valid number for amount")
            return

        conn = sqlite3.connect('expense_tracker.db')
        c = conn.cursor()
        c.execute("INSERT INTO expenses (category, description, amount, date) VALUES (?, ?, ?, ?)",
                  (category, description, amount, date))
        conn.commit()
        conn.close()

        self.category.delete(0, END)
        self.description.delete(0, END)
        self.amount.delete(0, END)

        messagebox.showinfo("Expense Added", "Expense successfully recorded.")

    def show_expenses(self):
        self.show_window = Toplevel(self.master)
        self.show_window.title("All Expenses")

        conn = sqlite3.connect('expense_tracker.db')
        c = conn.cursor()
        c.execute("SELECT * FROM expenses")
        records = c.fetchall()
        conn.close()

        tree = ttk.Treeview(self.show_window, columns=(
            "Category", "Description", "Amount", "Date"), show="headings")
        tree.heading("#1", text="Category")
        tree.heading("#2", text="Description")
        tree.heading("#3", text="Amount")
        tree.heading("#4", text="Date")

        for record in records:
            tree.insert("", END, values=(
                record[1], record[2], record[3], record[4]))

        tree.pack()

    def visualize_data(self):
        conn = sqlite3.connect('expense_tracker.db')
        df = pd.read_sql_query("SELECT * FROM expenses", conn)
        conn.close()

        if df.empty:
            messagebox.showwarning("No Data", "No data to visualize")
            return

        plt.figure(figsize=(14, 6))

        plt.subplot(1, 2, 1)
        df.groupby('category')['amount'].sum().plot(kind='bar')
        plt.title('Expenses by Category')

        plt.subplot(1, 2, 2)
        df['date'] = pd.to_datetime(df['date'])
        df.groupby('date')['amount'].sum().plot(kind='line')
        plt.title('Expenses over Time')

        plt.tight_layout()
        plt.show()

    def export_csv(self):
        conn = sqlite3.connect('expense_tracker.db')
        df = pd.read_sql_query("SELECT * FROM expenses", conn)
        conn.close()

        if df.empty:
            messagebox.showwarning("No Data", "No data to export")
            return

        filepath = 'expenses.csv'
        df.to_csv(filepath, index=False)

        messagebox.showinfo("Export Successful",
                            f"Data exported to {filepath}")


# Initialize Tkinter
root = Tk()
my_expense_tracker = ExpenseTracker(root)
root.mainloop()
