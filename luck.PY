import random

guess=int(input("Enter a number between 1-100 \n"))

numb=random.randint(1,100)

if guess==numb:
    print("your Lucky day")
else:
    print (f"NAH the number was {numb}")