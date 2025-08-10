import random
number_to_guess=random.randint(1,100)
guess=None
attempt=0
print("Welcome to number guessing challenge!!")
print("I am thinking of a number from 1 to 100")
while guess!=number_to_guess:
    try:
        guess=int(input("Enter your guess:"))
        attempt+=1
        if guess<number_to_guess:
            print("Too low..,Try again")
        elif guess>number_to_guess:
            print("Too high..,Try again")
        else:
            print(f"Congratulation!!!!, You guessed the number on {attempt} tr{'y'if attempt==1 else 'ies'}.")
    except valueError:
        print("Invalid input. Please enter a valid number")