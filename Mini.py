import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"


def load_expenses():
    """Load existing expenses from the JSON file, or return an empty list."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []


def save_expenses(expenses):
    """Save the current list of expenses to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    """Prompt the user for expense details and add it to the list."""
    print("\n--- Add New Expense ---")
    description = input("Description (e.g., Groceries, Coffee): ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    category = (
        input("Category (e.g., Food, Transport, Bills, Fun): ").strip().title()
    )
    if not category:
        category = "Uncategorized"

    while True:
        try:
            amount = float(input("Amount: $"))
            if amount <= 0:
                print("Please enter an amount greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value (e.g., 12.50).")

    expense = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "description": description,
        "category": category,
        "amount": round(amount, 2),
    }

    expenses.append(expense)
    save_expenses(expenses)
    print(f"Added: {description} (${amount:.2f}) under [{category}]")


def view_expenses(expenses):
    """Display all recorded expenses in a formatted table."""
    print("\n--- All Expenses ---")
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(
        f"{'#':<4} {'Date':<18} {'Category':<15} {'Description':<22} {'Amount':>10}"
    )
    print("-" * 73)

    for idx, item in enumerate(expenses, start=1):
        print(
            f"{idx:<4} {item['date']:<18} {item['category']:<15} "
            f"{item['description'][:20]:<22} ${item['amount']:>9.2f}"
        )


def view_summary(expenses):
    """Calculate total spending and break it down by category."""
    print("\n--- Spending Summary ---")
    if not expenses:
        print("No expenses to summarize.")
        return

    total = sum(item["amount"] for item in expenses)
    by_category = {}

    for item in expenses:
        cat = item["category"]
        by_category[cat] = by_category.get(cat, 0) + item["amount"]

    for cat, cat_total in sorted(
        by_category.items(), key=lambda x: x[1], reverse=True
    ):
        percentage = (cat_total / total) * 100
        print(f"{cat:<18}: ${cat_total:>8.2f} ({percentage:.1f}%)")

    print("-" * 38)
    print(f"{'Total Spent':<18}: ${total:>8.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Spending Summary")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_summary(expenses)
        elif choice == "4":
            print("Goodbye! Your expenses are saved.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()