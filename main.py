from expense_manager.expense import Expense
from expense_manager.expense_db import ExpenseDB
from utils import date_formatter as create_utc_timestamp, json_formatter
from pprint import pprint

created_at = create_utc_timestamp.create_date()

def main():
    expense_db = ExpenseDB()

    # Adding Expenses
    expense = Expense('Lunch', 10, created_at)
    expense_db.add_expense(expense.to_dict())

    expense = Expense('Bolt Ride', 20.0, created_at)
    expense_db.add_expense(expense.to_dict())

    expense = Expense('Breakfast', 5.0, created_at)
    expense_db.add_expense(expense.to_dict())

    # Listing Expenses
    expenses = expense_db.get_expenses()
    print(json_formatter.format_list_of_dicts(expenses))

    # Get Expense by ID
    # pprint(expense_db.get_expense_by_id(expenses[2]['id']))

    # Get Expense by Title
    # pprint(expense_db.get_expense_by_title('Lunch'))

    # Update Expense
    # updated_expense = expense.update_expense(expenses[0], 15.0, 'Date Night')
    # pprint(updated_expense)

    # Remove Expense
    # print(expense_db.remove_expense(expenses[1]['id']))

if __name__ == '__main__':
    main()
