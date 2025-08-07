class Transaction:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.category}: ${self.amount:.2f} - {self.description}"


class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, description):
        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)
        print("Transaction added.")

    def show_summary(self):
        income = sum(t.amount for t in self.transactions if t.amount > 0)
        expense = sum(-t.amount for t in self.transactions if t.amount < 0)
        balance = income - expense

        print("\n--- Budget Summary ---")
        print(f"Total Income: ${income:.2f}")
        print(f"Total Expenses: ${expense:.2f}")
        print(f"Net Balance: ${balance:.2f}")

    def show_category_summary(self, category):
        filtered = [t for t in self.transactions if t.category.lower() == category.lower()]
        if not filtered:
            print(f"No transactions found for category: {category}")
            return

        total = sum(t.amount for t in filtered)
        print(f"\n--- Summary for '{category}' ---")
        for t in filtered:
            print(f"  {t}")
        print(f"Total: ${total:.2f}")


# Main CLI Loop
def main():
    tracker = BudgetTracker()
    print("Welcome to Budget Tracker")

    while True:
        command = input("\nEnter command (add, summary, summary category, exit): ").strip().lower()

        if command == "add":
            try:
                t_type = input("Income or Expense? ").strip().lower()
                amount = float(input("Amount: "))
                if t_type == "expense":
                    amount = -abs(amount)  # Ensure it's negative
                elif t_type == "income":
                    amount = abs(amount)   # Ensure it's positive
                else:
                    print("Invalid type. Use 'income' or 'expense'.")
                    continue
                category = input("Category: ").strip()
                description = input("Description: ").strip()
                tracker.add_transaction(amount, category, description)
            except ValueError:
                print("Invalid input, please enter numeric amount.")

        elif command == "summary":
            tracker.show_summary()

        elif command.startswith("summary category"):
            _, _, category = command.partition("category")
            tracker.show_category_summary(category.strip())

        elif command == "exit":
            print("Goodbye")
            break

        else:
            print("Unknown command. Try 'add', 'summary', 'summary category', or 'exit'.")


if __name__ == "__main__":
    main()
