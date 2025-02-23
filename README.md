
# Expenses Manager

Expenses Manager is an Object Oriented Programming project for managing daily expenses. The functionalities includes creating and saving of Expense, updating expense, finding expense by **ID** & **Title**, deleting expenses.

The goal of this project is to assess my understanding of object-oriented e.g defining classes, utilizing class attributes and methods,and handling time-related functionalities in programming (OOP) concepts in Python.

## Built With

- **Python**

## Getting Started

### Prerequisites

- [Python](https://www.python.org/): Python is a programming language that lets you work quickly and integrate systems more effectively.

## Installation

Clone the repo

```bash
  git clone https://github.com/olaishola05/expense_manager.git
```

```bash
  cd expense_manager
```

## Running Tests

To run tests, run the following command

- To create expense

```python
  
  # Instantiate the expenseDB instance
  expense_db = ExpenseDB()
  
  expense = Expense('Lunch', 10, created_at)

  # Convert expense to dict and Add expense to DB
  expense_db.add_expense(expense.to_dict())
```

- Getting All Expenses

```python
  expenses = expense_db.get_expenses()
  print(expenses)
```

- Get Expense by ID

```python
  expense = expense_db.get_expense_by_id(expenses[0]['id']
  print(expense)
```

- Get List of Expense by Title

```python
  expenses = expense_db.get_expense_by_title('Lunch')
  print(expenses)
```

- Update Expense

```python
  updated_expense = expense.update_expense(expenses[0], 15.0, 'Date Night')
  print(updated_expense)
```

- Remove Expense

```python
  print(expense_db.remove_expense(expenses[0]['id'])
```

- Run the program

```bash
  python3 main
```

## Author

- GitHub: [@olaishola05](https://github.com/@olaishola05)
- Twitter: [@olaishola05](https://twitter.com/@olaishola05)
- LinkedIn: [Oladipupo Ishola](https://www.linkedin.com/in/olaishola05/)
- Medium: [@olaishola](https://medium.com/@olaishola)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/olaishola05/expense_manager/issues) here

### Show your support

- Give a ⭐ if you like this project

## Acknowledgements

- Thanks to everyone @ AltSchool Africa for doing an amazing job

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
