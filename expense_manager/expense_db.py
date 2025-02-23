from typing import List, Dict

type ExpenseDict = Dict[str, str]
type ExpenseListDict = List[ExpenseDict]

class ExpenseDB():
    def __init__(self) -> None:
        self.expense_list = []

    def add_expense(self, expense: Dict) -> ExpenseListDict:
        return self.expense_list.append(expense)

    def get_expense_by_id(self, id: str) -> ExpenseDict:
        for expense in self.expense_list:
            if expense["id"] == id:
                return expense
        return {
            "message": f"No expense with id {id} found.",
            "expense": {}
        }

    def get_expense_by_title(self, title: str) -> ExpenseDict:
        matched_expenses = []
        for expense in self.expense_list:
            if expense["title"] == title:
                matched_expenses.append(expense)
                return matched_expenses
        return {
            "message": f"No expense with title {title} found.",
            "expenses": matched_expenses
        }
    
    def remove_expense(self, id: str) -> bool:
        for expense in self.expense_list:
            if expense["id"] == id:
                self.expense_list.remove(expense)
                print(f"Expense with id {id} removed.")
                return True
        print(f"Expense with id {id} not found.")
        return False
    
    def get_expenses(self) -> ExpenseListDict:
        return self.expense_list