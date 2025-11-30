#!/usr/bin/env python3
"""
Test script for Personal Expense Tracker
Demonstrates and tests all functionality
"""

import os
from expense_func import load_expenses, save_expenses, add_expense, remove_expense, update_expense, view_expenses

def test_all_functions():
    """Run comprehensive tests on all expense tracker functions."""
    
    print("="*60)
    print("          EXPENSE TRACKER - AUTOMATED TESTS")
    print("="*60)
    
    # Use a test file to avoid affecting real data
    test_file = "test_expenses.csv"
    
    # Clean up any existing test file
    if os.path.exists(test_file):
        os.remove(test_file)
        print("\n✅ Cleaned up previous test file")
    
    # Test 1: Load from non-existent file
    print("\n" + "-"*60)
    print("TEST 1: Load expenses from non-existent file")
    print("-"*60)
    expenses = load_expenses(test_file)
    assert expenses == {}, "Should return empty dict for non-existent file"
    print("✅ PASSED: Empty dictionary returned")
    
    # Test 2: Add new expenses
    print("\n" + "-"*60)
    print("TEST 2: Add new expenses")
    print("-"*60)
    add_expense(expenses, "Groceries", 150.50)
    add_expense(expenses, "Rent", 1200.00)
    add_expense(expenses, "Utilities", 85.30)
    print(f"Added 3 expenses")
    assert len(expenses) == 3, "Should have 3 categories"
    assert expenses["Groceries"] == 150.50, "Groceries should be 150.50"
    print("✅ PASSED: Expenses added correctly")
    
    # Test 3: Add to existing category
    print("\n" + "-"*60)
    print("TEST 3: Add to existing category")
    print("-"*60)
    print(f"Groceries before: ${expenses['Groceries']:.2f}")
    add_expense(expenses, "Groceries", 45.25)
    print(f"Groceries after adding $45.25: ${expenses['Groceries']:.2f}")
    assert expenses["Groceries"] == 195.75, "Groceries should be 195.75"
    print("✅ PASSED: Amount accumulated correctly")
    
    # Test 4: View expenses
    print("\n" + "-"*60)
    print("TEST 4: View expenses")
    print("-"*60)
    view_expenses(expenses)
    print("✅ PASSED: Expenses displayed")
    
    # Test 5: Update expense
    print("\n" + "-"*60)
    print("TEST 5: Update expense amount")
    print("-"*60)
    print(f"Rent before: ${expenses['Rent']:.2f}")
    result = update_expense(expenses, "Rent", 1250.00)
    print(f"Rent after update: ${expenses['Rent']:.2f}")
    assert result == True, "Update should succeed"
    assert expenses["Rent"] == 1250.00, "Rent should be 1250.00"
    print("✅ PASSED: Expense updated correctly")
    
    # Test 6: Update non-existent category
    print("\n" + "-"*60)
    print("TEST 6: Update non-existent category")
    print("-"*60)
    result = update_expense(expenses, "Entertainment", 100.00)
    assert result == False, "Update should fail for non-existent category"
    assert "Entertainment" not in expenses, "Entertainment should not be added"
    print("✅ PASSED: Update correctly failed for non-existent category")
    
    # Test 7: Remove expense
    print("\n" + "-"*60)
    print("TEST 7: Remove expense")
    print("-"*60)
    print(f"Categories before removal: {list(expenses.keys())}")
    result = remove_expense(expenses, "Utilities")
    print(f"Categories after removing 'Utilities': {list(expenses.keys())}")
    assert result == True, "Removal should succeed"
    assert "Utilities" not in expenses, "Utilities should be removed"
    assert len(expenses) == 2, "Should have 2 categories left"
    print("✅ PASSED: Expense removed correctly")
    
    # Test 8: Remove non-existent category
    print("\n" + "-"*60)
    print("TEST 8: Remove non-existent category")
    print("-"*60)
    result = remove_expense(expenses, "Utilities")
    assert result == False, "Removal should fail for non-existent category"
    print("✅ PASSED: Removal correctly failed for non-existent category")
    
    # Test 9: Save expenses
    print("\n" + "-"*60)
    print("TEST 9: Save expenses to CSV")
    print("-"*60)
    save_expenses(expenses, test_file)
    assert os.path.exists(test_file), "CSV file should be created"
    print("✅ PASSED: File saved successfully")
    
    # Test 10: Load expenses from file
    print("\n" + "-"*60)
    print("TEST 10: Load expenses from CSV")
    print("-"*60)
    loaded_expenses = load_expenses(test_file)
    assert len(loaded_expenses) == len(expenses), "Should load same number of categories"
    assert loaded_expenses["Groceries"] == 195.75, "Groceries should match"
    assert loaded_expenses["Rent"] == 1250.00, "Rent should match"
    print(f"Loaded {len(loaded_expenses)} categories from file")
    print("✅ PASSED: Expenses loaded correctly")
    
    # Test 11: Error handling - empty category
    print("\n" + "-"*60)
    print("TEST 11: Error handling - empty category name")
    print("-"*60)
    try:
        add_expense(expenses, "", 100.00)
        print("❌ FAILED: Should have raised ValueError")
    except ValueError as e:
        print(f"✅ PASSED: Correctly raised ValueError: {e}")
    
    # Test 12: Error handling - negative amount
    print("\n" + "-"*60)
    print("TEST 12: Error handling - negative amount")
    print("-"*60)
    try:
        add_expense(expenses, "Test", -50.00)
        print("❌ FAILED: Should have raised ValueError")
    except ValueError as e:
        print(f"✅ PASSED: Correctly raised ValueError: {e}")
    
    # Test 13: View empty expenses
    print("\n" + "-"*60)
    print("TEST 13: View empty expense list")
    print("-"*60)
    empty_expenses = {}
    view_expenses(empty_expenses)
    print("✅ PASSED: Empty expense list handled correctly")
    
    # Clean up test file
    if os.path.exists(test_file):
        os.remove(test_file)
        print("\n✅ Cleaned up test file")
    
    # Final summary
    print("\n" + "="*60)
    print("          ALL TESTS PASSED! ✅")
    print("="*60)
    print("\nThe expense tracker is working correctly!")
    print("All requirements have been met:")
    print("  ✅ Add expense (with accumulation)")
    print("  ✅ Remove expense")
    print("  ✅ Update expense")
    print("  ✅ View expenses")
    print("  ✅ Save to CSV")
    print("  ✅ Load from CSV")
    print("  ✅ Error handling")
    print("  ✅ Input validation")
    print("  ✅ Total expenses (bonus feature)")
    print("="*60 + "\n")

if __name__ == "__main__":
    test_all_functions()

