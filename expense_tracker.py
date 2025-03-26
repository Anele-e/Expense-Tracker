import json
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="Expanse tracker")

parser.add_argument(
    "action",
    choices=["add", "list", "summary", "delete", "update"],
    help="Action to perform",
)
parser.add_argument(
    "--description", help="Description of what you're adding to your expenses", type=str
)
parser.add_argument(
    "--amount", help="Amount of what you're adding to your expenses", type=int
)
parser.add_argument(
    "--id", help="ID of what you're deleting in your expenses", type=int
)
parser.add_argument("--month", help="summary of specific month", type=int)

args = parser.parse_args()


def reading_file():
    try:
        with open("my_expenses.json", "r") as file:
            expenses = json.load(file)
        return expenses
    except FileNotFoundError:
        expenses = []


def writing_file(dumping_this):
    with open("my_expenses.json", "w") as file:
        json.dump(dumping_this, file, indent=4)


def list():
    expenses = reading_file()

    if not expenses:
        print("No expenses found")
        return

    print(f"{'id':<5} {'Date':<10} {'description':<20} {'amount'}")

    for expense in expenses:
        amount = f"R{expense['amount']}"
        print(
            f"{expense['id']:<5} {expense['date']:<10} {expense['description']:<20} {amount}"
        )


def delete(id):
    expenses = reading_file()

    if not expenses:
        print("No expenses found")
        return

    orig_expense = len(expenses)
    expenses = [expense for expense in expenses if expense["id"] != id]
    if len(expenses) == orig_expense:
        print("There is no expense with that ID")
        return
    writing_file(expenses)
    print("Expense deleted successfully")


def add(description, amount):
    current_date = datetime.now().strftime("%Y-%m-%d")
    expenses = reading_file()

    next_id = expenses[-1]["id"] + 1 if expenses else 1

    new_entry = {
        "id": next_id,
        "description": description,
        "amount": amount,
        "date": current_date,
    }

    expenses.append(new_entry)

    writing_file(expenses)

    print(f"Expense added successfully (ID: {next_id})")


def summary():
    expenses = reading_file()
    if not expenses:
        print("No expenses found")
        return
    if args.month:
        filtered_data = [
            expense
            for expense in expenses
            if datetime.strptime(expense["date"], "%Y-%m-%d").month == args.month
        ]
        k = sum(f["amount"] for f in filtered_data)
        month_name = datetime.strptime(filtered_data[0]["date"], "%Y-%m-%d").strftime(
            "%B"
        )
        print(f"Total expenses for {month_name} : R{k}")
    else:
        k = sum(expense["amount"] for expense in expenses)
        print(f"Total expenses: R{k}")


def update(id, description=None, amount=None):
    expenses = reading_file()

    for expense in expenses:
        if expense["id"] == id:
            if description is not None:
                expense["description"] = description
            if amount is not None:
                expense["amount"] = amount

            writing_file(expenses)
            print(f"Expense with ID {id} updated successfully")
            return

    print(f"No expense found with the ID {id}")


if args.action == "add":
    if not args.description or args.amount is None:
        print("Please provide both description and amount for adding an expense")
    else:
        add(args.description, args.amount)

elif args.action == "list":
    list()

elif args.action == "summary":
    summary()
elif args.action == "delete":
    delete(args.id)
elif args.action == "update":
    if args.id is None:
        print("Please provide an ID to update an expense")
    elif args.description is None and args.amount is None:
        print("Please provide either a description or amount to update")
    else:
        update(args.id, args.description, args.amount)


