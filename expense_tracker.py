import csv
import os
from datetime import datetime

DATA_FILE = "expenses.csv"
CATEGORIES = ["Food", "Travel", "Shopping", "Bills", "Education", "Health", "Entertainment", "Other"]
FIELDS = ["id", "date", "category", "description", "amount"]


def setup_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(FIELDS)


def load_expenses():
    setup_file()
    with open(DATA_FILE, "r", newline="") as file:
        return list(csv.DictReader(file))


def save_expenses(expenses):
    with open(DATA_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)


def get_next_id(expenses):
    if not expenses:
        return 1
    return max(int(item["id"]) for item in expenses) + 1


def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: ₹"))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid amount.")


def get_date():
    while True:
        value = input("Enter date (DD-MM-YYYY), or press Enter for today: ").strip()
        if not value:
            return datetime.now().strftime("%d-%m-%Y")
        try:
            date = datetime.strptime(value, "%d-%m-%Y")
            return date.strftime("%d-%m-%Y")
        except ValueError:
            print("Invalid date. Use DD-MM-YYYY.")


def choose_category():
    print("\nCategories:")
    for i, category in enumerate(CATEGORIES, 1):
        print(f"{i}. {category}")

    while True:
        choice = input("Choose category: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        print("Please choose a valid category number.")


def add_expense():
    expenses = load_expenses()
    expense_id = get_next_id(expenses)

    print("\n--- Add Expense ---")
    date = get_date()
    category = choose_category()
    description = input("Enter description: ").strip()

    while not description:
        print("Description cannot be empty.")
        description = input("Enter description: ").strip()

    amount = get_amount()

    expenses.append({
        "id": str(expense_id),
        "date": date,
        "category": category,
        "description": description,
        "amount": f"{amount:.2f}"
    })

    save_expenses(expenses)
    print(f"Expense added successfully. ID: {expense_id}")


def show_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "-" * 78)
    print(f"{'ID':<5}{'Date':<13}{'Category':<16}{'Description':<25}{'Amount':>10}")
    print("-" * 78)

    for item in expenses:
        description = item["description"][:23]
        print(
            f"{item['id']:<5}{item['date']:<13}{item['category']:<16}"
            f"{description:<25}₹{float(item['amount']):>8.2f}"
        )

    print("-" * 78)


def view_all():
    print("\n--- All Expenses ---")
    show_expenses(load_expenses())


def search_expenses():
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses found.")
        return

    keyword = input("Enter description or category to search: ").strip().lower()
    if not keyword:
        print("Search cannot be empty.")
        return

    results = [
        item for item in expenses
        if keyword in item["description"].lower()
        or keyword in item["category"].lower()
    ]

    print(f"\n--- Search Results ({len(results)}) ---")
    show_expenses(results)


def category_summary():
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses found.")
        return

    totals = {}
    for item in expenses:
        category = item["category"]
        totals[category] = totals.get(category, 0) + float(item["amount"])

    print("\n--- Category Summary ---")
    for category, total in sorted(totals.items()):
        print(f"{category:<18} ₹{total:.2f}")

    print("-" * 30)
    print(f"{'Total':<18} ₹{sum(totals.values()):.2f}")


def total_spending():
    expenses = load_expenses()
    total = sum(float(item["amount"]) for item in expenses)

    print("\n--- Total Spending ---")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Total spent: ₹{total:.2f}")

    if expenses:
        print(f"Average expense: ₹{total / len(expenses):.2f}")


def monthly_summary():
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses found.")
        return

    value = input("Enter month and year (MM-YYYY): ").strip()

    try:
        datetime.strptime(value, "%m-%Y")
    except ValueError:
        print("Invalid format. Use MM-YYYY.")
        return

    selected = []
    for item in expenses:
        try:
            date = datetime.strptime(item["date"], "%d-%m-%Y")
            if date.strftime("%m-%Y") == value:
                selected.append(item)
        except ValueError:
            continue

    print(f"\n--- Summary for {value} ---")
    show_expenses(selected)

    total = sum(float(item["amount"]) for item in selected)
    print(f"Total for {value}: ₹{total:.2f}")


def delete_expense():
    expenses = load_expenses()
    if not expenses:
        print("\nNo expenses found.")
        return

    show_expenses(expenses)

    value = input("\nEnter expense ID to delete: ").strip()
    if not value.isdigit():
        print("Enter a valid ID.")
        return

    new_expenses = [item for item in expenses if item["id"] != value]

    if len(new_expenses) == len(expenses):
        print("Expense ID not found.")
        return

    save_expenses(new_expenses)
    print("Expense deleted successfully.")


def main():
    setup_file()

    while True:
        print("\n==============================")
        print("     PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expenses")
        print("4. Category Summary")
        print("5. Total Spending")
        print("6. Monthly Summary")
        print("7. Delete Expense")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            total_spending()
        elif choice == "6":
            monthly_summary()
        elif choice == "7":
            delete_expense()
        elif choice == "8":
            print("\nThank you for using Personal Expense Tracker.")
            break
        else:
            print("Invalid choice. Please select 1-8.")


if __name__ == "__main__":
    main()
