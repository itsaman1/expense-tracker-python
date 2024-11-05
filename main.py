import csv
from datetime import datetime

# Expense class to represent each expense entry
class Expense:
    def __init__(self, amount, date, category, description):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

    def to_dict(self):
        return {
            "amount": self.amount,
            "date": self.date,
            "category": self.category,
            "description": self.description
        }


# Main execution block
def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Update Expense")
        print("5. Filter by Category")
        print("6. Generate Report")
        print("7. Save Expenses")
        print("8. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(amount, date, category, description)
        
        elif choice == '2':
            tracker.view_expenses()
        
        elif choice == '3':
            index = int(input("Enter expense index to delete: "))
            tracker.delete_expense(index)
        
        elif choice == '4':
            index = int(input("Enter expense index to update: "))
            amount = input("Enter new amount (or leave blank): ")
            date = input("Enter new date (YYYY-MM-DD) (or leave blank): ")
            category = input("Enter new category (or leave blank): ")
            description = input("Enter new description (or leave blank): ")
            tracker.update_expense(index, amount, date, category, description)
        
        elif choice == '5':
            category = input("Enter category to filter: ")
            tracker.filter_by_category(category)
        
        elif choice == '6':
            period = input("Enter report period (daily, weekly, monthly): ")
            tracker.generate_report(period)
        
        elif choice == '7':
            tracker.save_expenses()
        
        elif choice == '8':
            tracker.save_expenses()  # Save data before exiting
            print("Exiting application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()