# Personal Expense Tracker

A simple command-line Personal Expense Tracker built with Python. It allows users to add, view, search, summarize, and delete expenses. Expense data is stored locally in a CSV file.

## Features

- Add a new expense
- View all saved expenses
- Search expenses by description or category
- View spending by category
- View total spending and average expense
- View expenses for a selected month
- Delete an expense using its ID
- Automatic creation of the `expenses.csv` data file
- Input validation for amount, date, category, and description

## Expense Categories

The application supports these categories:

- Food
- Travel
- Shopping
- Bills
- Education
- Health
- Entertainment
- Other

## Technologies Used

- Python 3
- CSV module
- OS module
- Datetime module

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python expense_tracker.py
```

5. Follow the menu shown in the terminal.

## Data Storage

The application stores expense records in `expenses.csv`.

Each record contains:

- ID
- Date
- Category
- Description
- Amount

The CSV file is created automatically when the program is run if it does not already exist.

## Menu Options

1. Add Expense
2. View All Expenses
3. Search Expenses
4. Category Summary
5. Total Spending
6. Monthly Summary
7. Delete Expense
8. Exit

## Example

```text
==============================
     PERSONAL EXPENSE TRACKER
==============================
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Category Summary
5. Total Spending
6. Monthly Summary
7. Delete Expense
8. Exit
```

## Project Structure

```text
Personal-Expense-Tracker/
│
├── expense_tracker.py
├── expenses.csv
└── README.md
```

`expenses.csv` is generated automatically by the program and may not exist in a fresh clone until the program is run.

## Conclusion

This project demonstrates basic Python programming concepts such as functions, loops, conditional statements, input validation, file handling, CSV data storage, and date processing. It provides a simple way to manage and analyze personal expenses from the command line.
