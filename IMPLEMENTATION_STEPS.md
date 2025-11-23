# Implementation Steps for Personal Expense Tracker

This guide provides a step-by-step approach to completing the Personal Expense Tracker assignment.

## Step 1: Project Setup

- [ ] Create a new Python file (e.g., `expense_tracker.py`)
- [ ] Set up the basic file structure
- [ ] Add necessary import statements (`csv`, `os`)

## Step 2: Define Data Structure

- [ ] Decide on the data structure to store expenses in memory (e.g., dictionary with category as key and amount as value)
- [ ] Define the CSV file name as a constant (`expenses.csv`)

## Step 3: Implement CSV File Operations

### 3.1 Load Expenses Function
- [ ] Create a `load_expenses()` function that:
  - Checks if `expenses.csv` exists
  - If it exists, reads the CSV file and loads data into a dictionary
  - If it doesn't exist, returns an empty dictionary
  - Handles potential file reading errors

### 3.2 Save Expenses Function
- [ ] Create a `save_expenses(expenses)` function that:
  - Takes the expenses dictionary as input
  - Writes all expense data to `expenses.csv`
  - Uses proper CSV formatting (category, amount)
  - Handles potential file writing errors

## Step 4: Implement Core Functionality

### 4.1 Add Expense Function
- [ ] Create an `add_expense(expenses)` function that:
  - Prompts user for category name
  - Prompts user for amount (validate it's a number)
  - If category exists, adds to the existing amount
  - If category doesn't exist, creates new entry
  - Displays confirmation message
  - Handles invalid input (non-numeric amounts)

### 4.2 Remove Expense Function
- [ ] Create a `remove_expense(expenses)` function that:
  - Displays current expense categories
  - Prompts user for category to remove
  - Checks if category exists
  - Removes the category if found
  - Displays appropriate message (success or not found)

### 4.3 Update Expense Function
- [ ] Create an `update_expense(expenses)` function that:
  - Displays current expense categories
  - Prompts user for category to update
  - Checks if category exists
  - Prompts for new amount (validate it's a number)
  - Replaces the old amount with new amount
  - Displays confirmation message
  - Handles invalid input

### 4.4 View Expenses Function
- [ ] Create a `view_expenses(expenses)` function that:
  - Displays all categories and amounts in a formatted table
  - Handles empty expense list (display appropriate message)
  - **BONUS**: Calculate and display total expenses

## Step 5: Create Main Menu

- [ ] Create a `display_menu()` function that:
  - Prints a clear menu with all options:
    1. Add Expense
    2. Remove Expense
    3. Update Expense
    4. View Expenses
    5. Save and Exit
  - Returns the menu as a formatted string

## Step 6: Implement Main Program Loop

- [ ] Create a `main()` function that:
  - Loads expenses from CSV at startup
  - Displays welcome message
  - Enters a while loop that:
    - Displays the menu
    - Gets user choice
    - Validates the choice (1-5)
    - Calls appropriate function based on choice
    - Breaks loop when user chooses to exit
  - Saves expenses to CSV before exiting
  - Displays goodbye message

## Step 7: Input Validation and Error Handling

- [ ] Add try-except blocks for:
  - File operations (opening, reading, writing CSV)
  - User input conversion (string to float/int)
  - Menu choice validation
- [ ] Handle edge cases:
  - Empty category names
  - Negative amounts
  - Non-existent categories for update/remove
  - Invalid menu choices

## Step 8: Testing

Test each functionality thoroughly:

### Test Case 1: Adding Expenses
- [ ] Add a new expense category with an amount
- [ ] Add another expense to the same category (should sum amounts)
- [ ] Verify the amounts are correct

### Test Case 2: Viewing Expenses
- [ ] View expenses after adding multiple categories
- [ ] Verify all categories and amounts display correctly
- [ ] **BONUS**: Verify total expenses calculation is correct

### Test Case 3: Updating Expenses
- [ ] Update an existing expense category with a new amount
- [ ] Try to update a non-existent category
- [ ] Verify appropriate messages are displayed

### Test Case 4: Removing Expenses
- [ ] Remove an existing expense category
- [ ] Try to remove a non-existent category
- [ ] Verify the category is removed from the list

### Test Case 5: Data Persistence
- [ ] Add several expenses and exit the program
- [ ] Restart the program
- [ ] Verify all expenses are loaded correctly from CSV

### Test Case 6: Error Handling
- [ ] Enter invalid input for amounts (e.g., letters instead of numbers)
- [ ] Enter invalid menu choices
- [ ] Verify error messages are clear and program doesn't crash

## Step 9: Code Refinement

- [ ] Add comments to explain complex logic
- [ ] Ensure consistent naming conventions
- [ ] Format code for readability
- [ ] Remove any debug print statements
- [ ] Add docstrings to functions

## Step 10: Bonus Feature (Optional)

- [ ] Implement total expenses calculation
- [ ] Display total at the bottom when viewing expenses
- [ ] Format the total with currency symbol or appropriate formatting

## Additional Enhancements (Optional)

Consider adding these features for extra polish:

- [ ] Date tracking for each expense
- [ ] Export functionality to different formats
- [ ] Search/filter expenses by category
- [ ] Set budget limits and warnings
- [ ] Data visualization (simple text-based charts)
- [ ] Input validation for negative amounts
- [ ] Category name normalization (case-insensitive)

## Submission Checklist

Before submitting your assignment:

- [ ] All required features are implemented and working
- [ ] Code is well-commented and readable
- [ ] All test cases pass successfully
- [ ] CSV file is created and data persists correctly
- [ ] Error handling is in place for invalid inputs
- [ ] README.md is complete with instructions
- [ ] Code follows Python best practices (PEP 8)

---

**Good luck with your assignment! 🚀**

