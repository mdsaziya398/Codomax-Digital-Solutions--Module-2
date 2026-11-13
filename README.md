# Codomax-Digital-Solutions--Module-2
# Personal Expense Tracker

## Project Description

The Personal Expense Tracker is a simple Python application developed to manage and track daily expenses. It allows users to add expenses, view all recorded transactions, and calculate total spending with category-wise summaries.

The application uses JSON file handling to store expense information permanently, allowing users to access their previous records whenever they run the program.

## Features

- Add new expenses with description, category, and amount.
- View all recorded expenses in a formatted table.
- Generate total spending summaries.
- Calculate category-wise expenses.
- Display the percentage of spending for each category.
- Automatically record the date and time of each expense.
- Store expense records using JSON.
- Validate user inputs and handle errors.

## Technologies Used

- Python 3
- JSON
- Visual Studio Code

## Python Concepts Used

- Variables and data types
- Lists and dictionaries
- Functions
- Loops
- Conditional statements
- Exception handling
- File handling
- JSON data storage
- Python modules (`json`, `os`, `datetime`)

## Project Structure

```text
Personal-Expense-Tracker/
│
├── expense_tracker.py
├── expenses.json
├── README.md
└── screenshots/
```

## How to Run the Project

1. Install Python 3 on your computer.
2. Clone or download this repository.
3. Open the project folder in Visual Studio Code.
4. Open the terminal.
5. Execute the following command:

```bash
python expense_tracker.py
```

6. Select an option from the menu.
7. Add expenses, view records, or generate a spending summary.

## Available Operations

1. Add Expense
2. View All Expenses
3. View Spending Summary
4. Exit

## Data Storage

All expense details are stored in `expenses.json` using JSON format. The application automatically loads existing records when it starts and saves new expenses whenever they are added.

## Future Improvements

- Add monthly and yearly expense reports.
- Add expense update and delete options.
- Set monthly spending budgets.
- Generate expense charts and graphs.
- Develop a graphical user interface using Streamlit.

## Author

Developed as part of Python programming practice.

## Project Status

Completed
