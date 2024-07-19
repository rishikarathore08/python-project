#Simple personal Budget Tracker
class BudgetTracker:
    def __init__(self):
        self.balance = 0.0
        self.transaction = []

    def add_income(self,amount,description):
        self.balance +=amount
        self.transactions.append((amount,description,'income'))
        print(f"Income of ${amount} added.New balnce: ${self.balance}")

    def add_expense(self,amount,description):
        self.balance -= amount
        self.transactions.append((amount,description,'expense'))
        print(f"Expense of ${amount} added. New balance: ${self.balance}")

    def view_balance(self):
        print(f"Current balance: ${amount} added. New balance: ${self.balance}")

    def view_balance(self):
        print("transactions:")
        for transaction in self.transactions:
            amount,description,type = transaction
            print(f"{type.capitalize()}: ${amount} - {description}")

    def main():
        budget_tracker = BudgetTracker()

        while True:
            print("\n--- Personal Budget Tracker ---")
            print("1.Add Income")
            print("2.Add Expense")
            print("3. View Balance")
            print("4. View Transaction")
            print("5. Exit")
            choice = input("Enter your choice(1-5):")

            if choice == '1':
                amount = float(input("Enter income amount: "))
                description = input("enter Description: ")
                budget_tracker.add_expense(amount,description)
            elif choice == '2':
                amount = float(input("Enter income amount: "))
                description = input("Enter description: ")
                budget_tracker.add_expense(amount,description)
            elif choice == '3':
                budget_tracker.view_balance()
            elif choice == '4':
                budget_tracker.view_transaction()
            elif choice == '5':
                print("Exiting the budget tracker. Goodbye!")
                break
            else:
                print("Invalid choice.Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

        



