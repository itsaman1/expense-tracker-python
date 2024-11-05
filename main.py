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


