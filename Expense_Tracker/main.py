import csv
from datetime import datetime

expenses = []
monthly_budget = None
file_name = "expenses.csv"

# Load expenses from CSV at start
def load_expenses():
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row['amount'] = float(row['amount'])
                    expenses.append(row)
                except ValueError:
                    continue
        print("✅ Expenses loaded successfully.")
    except FileNotFoundError:
        print("ℹ️ No previous expense file found. Starting fresh.")

# Save expenses to CSV
def save_expenses():
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
    print("✅ Expenses saved successfully.")

# Add an expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g., Food, Travel): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")
        return
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("✅ Expense added.")

# View all expenses
def view_expenses():
    if not expenses:
        print("ℹ️ No expenses to show.")
        return
    for idx, expense in enumerate(expenses, 1):
        if all(key in expense and expense[key] for key in ['date', 'category', 'amount', 'description']):
            print(f"{idx}. {expense['date']} | {expense['category']} | ₹{expense['amount']} | {expense['description']}")
        else:
            print(f"{idx}. ❌ Incomplete entry skipped.")

# Set and track budget
def track_budget():
    global monthly_budget
    if monthly_budget is None:
        try:
            monthly_budget = float(input("Set your monthly budget: "))
        except ValueError:
            print("❌ Invalid amount.")
            return

    total_spent = sum(exp['amount'] for exp in expenses)
    remaining = monthly_budget - total_spent
    if remaining < 0:
        print(f"⚠️ You have exceeded your budget by ₹{-remaining:.2f}!")
    else:
        print(f"✅ You have ₹{remaining:.2f} left for the month.")

# Menu
def menu():
    while True:
        print("\n📊 Personal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 5.")

# Run program
if __name__ == "__main__":
    load_expenses()
    menu()
