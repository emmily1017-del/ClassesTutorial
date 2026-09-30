#Simple Lottery Game
import random

#5 Lottery numbers
winning_numbers = sorted(random.sample(range(1,50),5))

#user chooses numbers
user_numbers = []
print("Please enter five unqiue numbers between 1 and 50")

while len(user_numbers) < 5:
    try:
        guess = int(input(f"Enter Number {len(user_numbers) + 1}: "))

        if guess < 1 or guess > 50:
            print("Out of range. Choose a number between 1 and 50.")
        elif guess in user_numbers:
            print("You already picked that number")
        else:
            user_numbers.append(guess)
    except ValueError:
        print("Please enter a valid whole number.")

#match to find winning numbers
matches = set(winning_numbers).intersection(set(user_numbers))
num_matches = len(matches)

#find out if user won
if num_matches == 5:
    print("You won the lottery!")
else:
    print("Better luck next time!")