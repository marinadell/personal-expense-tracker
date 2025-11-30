# expense_func.py
# Core functions for the Personal Expense Tracker
# Handles loading, saving, adding, removing, updating, and viewing expenses

import csv
import os

def load_expenses(filename="expenses.csv"):
    """
    Load expenses from a CSV file.
    
    Args:
        filename (str): Path to the CSV file containing expenses
        
    Returns:
        dict: Dictionary with category names as keys and amounts as values
    """
    expenses = {}
    
    if not os.path.exists(filename):
        return expenses
    
    try:
        with open(filename, "r", newline="") as file:
            reader = csv.reader(file)
            for row_num, row in enumerate(reader, 1):
                if len(row) == 2:
                    category, amount = row
                    category = category.strip()
                    
                    # Skip empty categories
                    if not category:
                        print(f"Warning: Skipping empty category on line {row_num}.")
                        continue
                    
                    try:
                        amount_val = float(amount)
                        if amount_val < 0:
                            print(f"Warning: Skipping negative amount for '{category}' on line {row_num}.")
                        else:
                            expenses[category] = amount_val
                    except ValueError:
                        print(f"Warning: Skipping invalid amount for '{category}' on line {row_num}.")
                elif len(row) > 0:  # Non-empty row with wrong format
                    print(f"Warning: Skipping malformed row {row_num}.")
    
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return {}
    
    return expenses


def save_expenses(expenses, filename="expenses.csv"):
    """
    Save expenses to a CSV file.
    
    Args:
        expenses (dict): Dictionary of expenses to save
        filename (str): Path to the CSV file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            for category, amount in sorted(expenses.items()):  # Sort for consistency
                writer.writerow([category, amount])
        print(f"Expenses saved successfully to '{filename}'!")
        return True
    except Exception as e:
        print(f"Error saving expenses: {e}")
        return False


def add_expense(expenses, category, amount):
    """
    Add a new expense or update an existing one by adding to the current amount.
    
    Args:
        expenses (dict): Dictionary of current expenses
        category (str): Expense category name
        amount (float): Amount to add
        
    Raises:
        ValueError: If category is empty or amount is negative
    """
    category = category.strip()
    
    if not category:
        raise ValueError("Category name cannot be empty.")
    
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount


def remove_expense(expenses, category):
    """
    Remove an expense category entirely.
    
    Args:
        expenses (dict): Dictionary of current expenses
        category (str): Category name to remove
        
    Returns:
        bool: True if removed successfully, False if category not found
    """
    category = category.strip()
    
    if not category:
        return False
    
    if category in expenses:
        del expenses[category]
        return True
    
    return False


def update_expense(expenses, category, amount):
    """
    Update the amount for an existing expense category (replaces the old amount).
    
    Args:
        expenses (dict): Dictionary of current expenses
        category (str): Category name to update
        amount (float): New amount to set
        
    Returns:
        bool: True if updated successfully, False if category not found or invalid input
    """
    category = category.strip()
    
    if not category or amount < 0:
        return False
    
    if category in expenses:
        expenses[category] = amount
        return True
    
    return False


def view_expenses(expenses):
    """
    Display all expenses in a formatted table with a total.
    
    Args:
        expenses (dict): Dictionary of current expenses
    """
    if not expenses:
        print("\n" + "="*40)
        print("No expenses recorded yet.")
        print("="*40 + "\n")
        return

    print("\n" + "="*40)
    print("         EXPENSE SUMMARY")
    print("="*40)
    
    # Sort expenses by category name for consistent display
    sorted_expenses = sorted(expenses.items())
    
    # Find the longest category name for formatting
    max_category_length = max(len(cat) for cat in expenses.keys())
    
    for category, amount in sorted_expenses:
        print(f"{category:<{max_category_length}} : ${amount:,.2f}")
    
    print("-" * 40)
    total = sum(expenses.values())
    print(f"{'TOTAL':<{max_category_length}} : ${total:,.2f}")
    print("="*40 + "\n")
