import datetime

expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (food/travel/shopping/other): ")
    note = input("Add a note (optional): ")
    date = datetime.date.today()

    expenses.append({
        "amount": amount,
        "category": category,
        "note": note,
        "date": str(date)
    })

    print("\nExpense added successfully!\n")


def view_expenses():
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return

    print("\n--- All Expenses ---")
    for exp in expenses:
        print(f"Amount: {exp['amount']} | Category: {exp['category']} | Date: {exp['date']} | Note: {exp['note']}")
    print()


def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expense: ₹{total}\n")


def category_wise_total():
    if not expenses:
        print("\nNo expenses to calculate.\n")
        return

    category_totals = {}

    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    print("\n--- Category Wise Expense ---")
    for cat, amt in category_totals.items():
        print(f"{cat}: ₹{amt}")
    print()


def main():
    while True:
        print("----- Expense Tracker -----")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expense")
        print("4. Category Wise Total")
        print("5. Exit")

        choice = input("Choose option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_wise_total()
        elif choice == "5":
            print("\nExiting... Bye!\n")
            break
        else:
            print("\nInvalid choice. Try again.\n")


main()
