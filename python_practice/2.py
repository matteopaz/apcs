import random

rand = random.randint(1,50)

guess = 0
n_guesses = 0
while guess != rand:
    n_guesses += 1
    guess = int(input("Input your guess for a number between 1 and 50: "))
    if guess < rand:
        print("Too low")
    elif guess > rand:
        print("Too High")
    else:
        print(f"Correct in {n_guesses} guesses")

