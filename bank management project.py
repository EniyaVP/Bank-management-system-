
"""# Bank Management System

balance = 1000   # Initial balance

print("Welcome to Simple Bank System")

for i in range(5):   # Allow 5 operations
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Amount Deposited Successfully")

    elif choice == 2:
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Current Balance:", balance)

    elif choice == 4:
        print("Thank you for using our bank")
        break

    else:
        print("Invalid Choice")

print("Program Ended")"""


# Bank Management System

account_holder = input("Enter Account Holder Name: ")
balance = 100000 # Initial balance

print("\nWelcome", account_holder)
print("Your Account Balance is:", balance)

for i in range(5):   # Allow 5 transactions
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Amount Deposited Successfully")

    elif choice == 2:
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Amount Withdrawn Successfully")
        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Account Holder:", account_holder)
        print("Current Balance:", balance)

    elif choice == 4:
        print("Thank you for banking with us,", account_holder)
        break

    else:
        print("Invalid Choice")

print("\nFinal Balance:", balance)
print("Program Ended")

