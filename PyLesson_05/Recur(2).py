import random

def recursion():
    guess = int(input("Pick a number between 1 and 10:"))
    number = random.randint(1, 10)
    print("The number is", number)
    if guess >= 1 and guess <= 10:
        if guess == number:
            print("Correct! The number is right!")
        else:
            print("Wrong!")
    else:
        print("Please make it 1-10")
        recursion()

recursion()
