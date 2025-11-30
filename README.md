# Personal Expense Tracker

## Group Assignment

### Overview
A basic Personal Expense Tracker application in Python that allows users to track their expenses by adding, updating, viewing, and removing expense entries. The application stores expense data in a CSV file and retrieves it when needed.

### Requirements

The program should support the following functionality:

- **Add** a new expense category and the amount spent in that category
- **Remove** an existing expense category
- **Update** the amount for an existing expense category
- **View** all expenses
- **Save** expenses and exit the program

### Detailed Instructions

#### 1. Data Storage

- Your program should **load existing expense data** from a CSV file (`expenses.csv`) at the start
- If no file exists, start with an empty list of expenses
- **Save the updated expense data** back into the CSV file before exiting

#### 2. Menu Options

Implement the following functionalities:

- **Add Expense**: Prompt the user for a category and amount. If the category already exists, update the amount by adding to the current amount.
- **Remove Expense**: Allow the user to delete an expense category entirely.
- **Update Expense**: Prompt the user for a new amount for a specific category.
- **View Expenses**: Display all expense categories and their corresponding amounts in a clean format.

#### 3. User Input Handling

- Handle invalid inputs appropriately (e.g., entering a string where a number is expected)
- Keep the program running in a loop until the user chooses to exit

#### 4. Testing

- Test your program to check whether your program behaves as expected (e.g., adding an expense, removing one, and updating an amount)

### Bonus Task (Optional)

Add a **total expenses summary** feature that displays the total amount spent across all categories when viewing the expenses.

### Getting Started

1. Clone this repository
2. Run the application:
   ```bash
   python3 expense_tracker.py
   ```
3. Follow the menu prompts to manage your expenses
4. Expenses will be automatically saved to `expenses.csv`

### Running Tests

Run the comprehensive test suite to verify all functionality:
```bash
python3 test_expense_tracker.py
```

All 13 tests should pass! ✅

### Project Files

- **`expense_tracker.py`** - Main application (recommended)
- **`expense_func.py`** - Core functions for expense management
- **`test_expense_tracker.py`** - Automated test suite
- **`USAGE_GUIDE.md`** - Detailed user guide with examples
- **`IMPLEMENTATION_STEPS.md`** - Step-by-step development guide
- **`IMPROVEMENTS_SUMMARY.md`** - Summary of enhancements made

### Features Implemented

✅ **All core requirements:**
- Add new expense category with amount
- Add to existing category (amounts accumulate)
- Remove existing expense category
- Update amount for existing category
- View all expenses in formatted table
- Save expenses to CSV file
- Load expenses from CSV file at startup
- Handle invalid inputs with clear error messages
- Program loop until user chooses to exit

✅ **Bonus feature:**
- Total expenses summary displayed when viewing

✅ **Additional enhancements:**
- Professional formatted output with visual indicators
- Context-aware operations (shows available categories)
- Comprehensive input validation
- Detailed user feedback for all operations
- Sorted display for consistency
- Robust error handling

### Technologies

- Python 3.x
- CSV file handling
- Built-in modules: `csv`, `os`

### Assignment Status

🎉 **COMPLETE** - All requirements met and tested!
