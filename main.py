import bank
import date
import Emmily
import melgar
from melgar import score
from datetime import datetime
correct_pin=3099
balance=3500
x=datetime.now()
readable_date = x.strftime("%B %d, %Y")
print (readable_date)

entered_pin=int(input("Enter the pin:"))
if entered_pin == correct_pin:
    print("Menu")
    print("Option 1: Check balance")
    print("Option 2: Withdraw money")
    print("Option 3: Deposit money")
    print("Option 4: Exit ATM")

    option=int(input("Choose an option:"))
    if option == 1:
        print(f"Balance is {balance}")
    elif option == 2:
        withdraw_amount=int(input("How much are you withdrawing?"))
        if withdraw_amount <= balance:
            print("Money is withdrawn")
            balance=bank.withdraw(balance, withdraw_amount)
            print(f"Balance is now: {balance}")
        else:
            print("Amount cannot be withdrawn")
    elif option == 3:
        deposit_amount=int(input("How much are you depositing?"))
        balance=bank.deposit(balance,deposit_amount)
        print(f"Balance is now: {balance}")
    elif option == 4:
        print("Exited ATM")
        exit

#belongs to date.py
date.date(7)        
#belongs to Emmily.py
add_result=Emmily.add(5,3,2)
print (add_result)
Number=10
Letters=["a","b","c","d"]
print (Letters[2])
Numbers=[0,1,2,3]
#belongs to Emmily.py
addition_result=Emmily.addition(Numbers[0],Numbers[3])
print (addition_result)
#belongs to melgar.py
convert_result=melgar.convert(60)
print(convert_result)
#this is for melgar.py
percentage=score(8)
print(percentage)

if percentage <= 40:
    print("You got a F")
elif percentage > 40 and percentage < 50:
    print("You got a D")
elif percentage > 50 and percentage < 60:
    print("You got a C")
elif percentage > 60 and percentage < 70:
    print("You got a B")
elif percentage > 70 and percentage < 100:
    print("You got an A")