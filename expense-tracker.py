
import csv
import os
from datetime import date, datetime

FILE_NAME = "expenses.csv"

expenses = []


# Load expenses from CSV file

def load_expenses():
    global expenses

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            expenses = []

            for row in reader:

                if not row.get("date"):
                    row["date"] = str(date.today())

                row["amount"] = float(row["amount"])

                expenses.append(row)

        save_expenses()

    print("Expenses loaded successfully!")


# Save expenses to CSV file
def save_expenses():
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["date", "amount", "category", "description"]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(expenses)

    print("Expenses saved successfully!")


# Add expense


def add_expense():

    # Validate amount
    while True:
        try:
            amount = float(input("Enter expense amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print("Invalid amount! Please enter numbers only.")

    # Validate category
    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    # Validate description
    while True:
        description = input("Enter description: ").strip()

        if description:
            break

        print("Description cannot be empty.")

    # Create expense
    expense = {
        "date": str(date.today()),
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    save_expenses()

    print("Expense added successfully!")



# View expenses
def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n----- All Expenses -----")

    for index, expense in enumerate(expenses, start=1):
        print(
            index,
            expense["date"],
            expense["amount"],
            expense["category"],
            expense["description"]
        )

def delete_expense():
    if not expenses:
        print("No expenses available to delete.")
        return

    view_expenses()

    try:
        expense_number = int(
            input("Enter expense number to delete: ")
        )

        if 1 <= expense_number <= len(expenses):

            deleted_expense = expenses.pop(expense_number - 1)

            save_expenses()

            print("Expense deleted successfully!")
            print("Deleted:", deleted_expense)

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")

def search_by_category():

    search_category = input(
        "Enter category to search: "
    ).strip().lower()

    found_expenses = []

    for expense in expenses:

        if expense["category"].lower() == search_category:
            found_expenses.append(expense)

    if not found_expenses:
        print("No expenses found in this category.")
        return

    print("\n----- Search Results -----")

    total = 0

    for expense in found_expenses:

        print(
            expense["date"],
            expense["amount"],
            expense["category"],
            expense["description"]
        )

        total += expense["amount"]

    print("Total for", search_category, ":", total)

def monthly_report():

    monthly_totals = {}

    for expense in expenses:

        expense_date = datetime.strptime(
            expense["date"], "%Y-%m-%d"
        )

        month = expense_date.strftime("%B %Y")

        amount = expense["amount"]

        if month in monthly_totals:
            monthly_totals[month] += amount
        else:
            monthly_totals[month] = amount

    if not monthly_totals:
        print("No expenses available.")
        return

    print("\n----- Monthly Expense Report -----")

    for month, total in monthly_totals.items():
        print(month, ":", total)


# Calculate total
def calculate_total():
    total = sum(expense["amount"] for expense in expenses)
    print("Total expenses:", total)


# Main menu
def show_menu():
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Category-wise Report")
    print("5. Delete Expense")
    print("6. Search Expenses by Category")
    print("7. Monthly Expense Report")
    print("8. Exit")

def main():
    load_expenses()

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            calculate_total()
        elif choice == "4":
            category_report()

        elif choice == "5":

            delete_expense()

        elif choice == "6":
            search_by_category()


        elif choice == "7":

            monthly_report()

        elif choice == "8":

            print("Thank you for using Expense Tracker!")

            break

        else:
            print("Invalid choice. Try again.")


def category_report():
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    print("\n----- Category-wise Report -----")

    for category, total in category_totals.items():
        print(category, ":", total)



if __name__ == "__main__":
    main()
