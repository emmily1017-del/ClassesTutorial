correct_pin=8524
balance=1000

entered_pin=int(input("Enter your pin:"))
if entered_pin == 8524:
    print("Atm menu")
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. Exit")

    option=int(input("Select an option:"))
    if option == 1:
        print("Balance is $1000")
    elif option == 2:
        withdraw_amount=int(input("How much do you want to withdraw?"))
        if withdraw_amount <= balance:
            print("Your money has been withdrawn")
            balance=balance-withdraw_amount
            print(f"your balance is now: {balance}")
        else:
            print("Amount cannot be withdrawn")
    elif option == 3:
        deposit_amount=int(input("How much money do you want to deposit?"))
        balance=balance+deposit_amount
        print(f"Your balance is now: {balance}")
    elif option == 4:
        print("You have exited")
        exit

else:
    print("Pin doesn't match")