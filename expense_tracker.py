#!/usr/bin/env python3
# Expense Tracker - Main Entry Point
# Personal Expense Tracker Application
# Allows users to add, update, view, and remove expense entries

import csv
from expense_func import load_expenses, save_expenses, add_expense, remove_expense, update_expense, view_expenses

def main():
    """Main function to run the expense tracker application."""
    expense_file = "expenses.csv"
    
    # Load existing expenses from CSV file
    print("Loading expenses...")
    expenses = load_expenses(expense_file)
    print(f"Loaded {len(expenses)} expense categories.\n")

    while True:
        # Display menu
        print("\n" + "="*40)
        print("    EXPENSE MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. Update Expense")
        print("4. View Expenses")
        print("5. Save and Exit")
        print("="*40)

        choice = input("\nEnter your choice (1-5): ").strip()

        # Option 1: Add Expense
        if choice == '1':
            category = input("Enter expense category: ").strip()
            
            # Validate category name
            if not category:
                print("Error: Category name cannot be empty.")
                continue
            
            # Get and validate amount
            while True:
                amount_input = input("Enter amount: $").strip()
                try:
                    amount = float(amount_input)
                    if amount < 0:
                        print("Error: Amount cannot be negative. Please try again.")
                        continue
                    if amount == 0:
                        print("Warning: Amount is zero. Are you sure? (y/n): ", end="")
                        confirm = input().strip().lower()
                        if confirm != 'y':
                            continue
                    break
                except ValueError:
                    print("Error: Invalid number. Please enter a valid amount.")
            
            # Check if category exists and add expense
            category_existed = category in expenses
            old_amount = expenses.get(category, 0)
            
            add_expense(expenses, category, amount)
            
            if category_existed:
                print(f"Added ${amount:,.2f} to {category}. New total: ${expenses[category]:,.2f}")
            else:
                print(f"Created new category {category} with ${amount:,.2f}")

        # Option 2: Remove Expense
        elif choice == '2':
            # Show current expenses first
            if not expenses:
                print("\nNo expenses to remove.")
                continue
            
            print("\nCurrent expense categories:")
            for cat in expenses.keys():
                print(f"  - {cat}")
            
            category = input("\nEnter category to remove: ").strip()
            
            if not category:
                print("Error: Category name cannot be empty.")
                continue
            
            if remove_expense(expenses, category):
                print(f"Successfully removed {category}.")
            else:
                print(f"Category {category} not found.")

        # Option 3: Update Expense
        elif choice == '3':
            # Show current expenses first
            if not expenses:
                print("\nNo expenses to update.")
                continue
            
            print("\nCurrent expense categories:")
            for cat, amt in expenses.items():
                print(f"  - {cat}: ${amt:,.2f}")
            
            category = input("\nEnter category to update: ").strip()
            
            if not category:
                print("Error: Category name cannot be empty.")
                continue
            
            # Check if category exists
            if category not in expenses:
                print(f"Category {category} not found.")
                continue
            
            print(f"Current amount for '{category}': ${expenses[category]:,.2f}")
            
            # Get new amount
            while True:
                amount_input = input("Enter new amount: $").strip()
                try:
                    amount = float(amount_input)
                    if amount < 0:
                        print("Error: Amount cannot be negative. Please try again.")
                        continue
                    break
                except ValueError:
                    print("Error: Invalid number. Please enter a valid amount.")
            
            old_amount = expenses[category]
            if update_expense(expenses, category, amount):
                print(f"Updated {category} from ${old_amount:,.2f} to ${amount:,.2f}")
            else:
                print(f"Failed to update {category}.")

        # Option 4: View Expenses
        elif choice == '4':
            view_expenses(expenses)

        # Option 5: Save and Exit
        elif choice == '5':
            print("\nSaving expenses...")
            save_expenses(expenses, expense_file)
            print("\n" + "="*40)
            print("   Thank you for using Expense Tracker!")
            print("="*40)
            print("Goodbye!\n")
            break

        # Invalid choice
        else:
            print("Invalid choice. Please choose a number between 1-5.")

if __name__ == "__main__":
    main()

