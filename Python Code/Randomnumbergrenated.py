import random

# initiate a secret number
secret_number = random.randint(1, 100)
# user input = to guess what is the number from user
guess = int(input("Enter Number:"))

i = 0
while i < 3:
   # check the answer is correct
    if guess == secret_number:
     print("Bingo!")
   # give hint, is the guess number is too high
    elif guess > secret_number:
        print('too high')
   # if the number is too low
    elif guess < secret_number:
       print("too low")
    else:
       print("you lose")    
   # finish
       print("Thank you for joining the first game we made")
       print(secret_number)
       i += 1
print(i)
