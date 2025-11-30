# Personal Expense Tracker - Usage Guide

## Quick Start

### Running the Application

```bash
python3 expense_tracker.py
```

### Running the Tests

```bash
python3 test_expense_tracker.py
```

This will run comprehensive automated tests to verify all functionality.

## Features

### 1. Add Expense
- Enter a category name (e.g., "Groceries", "Rent", "Utilities")
- Enter an amount (must be a positive number)
- If the category already exists, the amount will be **added** to the current total
- If it's a new category, it will be created with that amount

**Example:**
```
Enter expense category: Groceries
Enter amount: $150.50
✅ Created new category 'Groceries' with $150.50

Enter expense category: Groceries
Enter amount: $45.25
✅ Added $45.25 to 'Groceries'. New total: $195.75
```

### 2. Remove Expense
- Displays all current expense categories
- Enter the category name you want to remove
- The category and its amount will be completely deleted

**Example:**
```
Current expense categories:
  - Groceries
  - Rent
  - Utilities

Enter category to remove: Utilities
✅ Successfully removed 'Utilities'.
```

### 3. Update Expense
- Displays all current expenses with their amounts
- Enter the category you want to update
- Enter the new amount (this **replaces** the old amount, not adds to it)

**Example:**
```
Current expense categories:
  - Groceries: $195.75
  - Rent: $1,200.00

Enter category to update: Rent
Current amount for 'Rent': $1,200.00
Enter new amount: $1,250.00
✅ Updated 'Rent' from $1,200.00 to $1,250.00
```

### 4. View Expenses
- Displays all expense categories with their amounts
- Shows formatted table with proper alignment
- Numbers display with comma separators (e.g., $14,000.00)
- **BONUS**: Displays total of all expenses at the bottom

**Example:**
```
========================================
         EXPENSE SUMMARY
========================================
Groceries : $195.75
Rent      : $1,250.00
Utilities : $14,000.00
----------------------------------------
TOTAL     : $15,445.75
========================================
```

### 5. Save and Exit
- Automatically saves all expenses to `expenses.csv`
- Exits the program gracefully
- Next time you run the program, all your expenses will be loaded automatically

## Error Handling

The application handles various error scenarios:

### Invalid Input
```
Enter amount: $abc
❌ Error: Invalid number. Please enter a valid amount.
```

### Negative Amounts
```
Enter amount: $-50
❌ Error: Amount cannot be negative. Please try again.
```

### Empty Category Names
```
Enter expense category: 
❌ Error: Category name cannot be empty.
```

### Non-existent Categories
```
Enter category to remove: Entertainment
❌ Category 'Entertainment' not found.
```

### Invalid Menu Choices
```
Enter your choice (1-5): 9
❌ Invalid choice. Please choose a number between 1-5.
```

## Data Storage

### CSV File Format
Expenses are stored in `expenses.csv` with the following format:
```csv
Groceries,195.75
Rent,1250.00
Utilities,85.30
```

### Automatic Loading
- When you start the program, it automatically loads existing expenses from `expenses.csv`
- If the file doesn't exist, it starts with an empty expense list
- The file is created automatically when you save and exit

### Data Persistence
All changes are saved when you:
- Choose option 5 (Save and Exit)
- The program will confirm: "✅ Expenses saved successfully to 'expenses.csv'!"

## Tips for Use

1. **Add vs Update**: 
   - Use **Add** when you want to accumulate expenses (e.g., multiple grocery trips)
   - Use **Update** when you want to set a new total amount (e.g., correcting an error)

2. **View Before Remove/Update**: 
   - The program automatically shows you the list of categories before removing or updating
   - This helps you avoid typos

3. **Zero Amounts**: 
   - If you enter 0, you'll get a confirmation prompt
   - This prevents accidental zero entries

4. **Save Your Work**: 
   - Always use option 5 to exit
   - This ensures all your changes are saved to the CSV file

## File Structure

```
personal-expense-tracker/
├── expense_tracker.py          # Main application
├── expense_func.py             # Core functions
├── test_expense_tracker.py     # Automated tests
├── expenses.csv                # Data storage (created automatically)
├── README.md                   # Project overview
└── USAGE_GUIDE.md             # This file
```

## Requirements Met

✅ **All assignment requirements completed:**
- [x] Add new expense category with amount
- [x] Add to existing category (accumulates)
- [x] Remove existing expense category
- [x] Update amount for existing category
- [x] View all expenses in clean format
- [x] Save expenses to CSV file
- [x] Load expenses from CSV file
- [x] Handle invalid inputs appropriately
- [x] Keep program running in loop until exit
- [x] **BONUS**: Total expenses summary

## Troubleshooting

### Problem: CSV file gets corrupted
**Solution**: Delete `expenses.csv` and start fresh. The program will create a new file.

### Problem: Can't find a category
**Solution**: Use option 4 to view all categories and check the exact spelling (case-sensitive).

### Problem: Amounts look wrong
**Solution**: Remember that "Add" accumulates amounts. Use "Update" to set a new total.

### Problem: Program doesn't save changes
**Solution**: Make sure you use option 5 to exit. Don't close the terminal directly.

## Support

For issues or questions about this assignment:
1. Review the `README.md` for assignment requirements
2. Run `test_expense_tracker.py` to verify functionality
3. Check that all files are present in the project directory

---

**Enjoy tracking your expenses! 💰**

