def balance_checkbook():
    print("Welcome to the Checkbook Balancer!")
    print("Enter your transactions below. Type 'done' when finished.\n")

    # Get the initial balance
    try:
        balance = float(input("Enter your starting balance: $"))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    transactions = []

    while True:
        transaction = input("Enter a transaction (e.g., +50 for deposit, -30 for withdrawal): ")
        if transaction.lower() == 'done':
            break
        try:
            amount = float(transaction)
            transactions.append(amount)
            balance += amount
            print(f"Transaction recorded. Current balance: ${balance:.2f}")
        except ValueError:
            print("Invalid transaction. Please enter a numeric value (e.g., +50 or -30).")

    print("\nSummary:")
    print(f"Starting Balance: ${balance - sum(transactions):.2f}")
    print("Transactions:")
    for i, t in enumerate(transactions, 1):
        print(f"  {i}. {'Deposit' if t > 0 else 'Withdrawal'}: ${t:.2f}")
    print(f"Final Balance: ${balance:.2f}")

if __name__ == "__main__":
    balance_checkbook()