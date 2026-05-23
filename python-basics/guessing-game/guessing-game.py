import random

secret_number = random.randint(1, 10)
attempts = 0

print("Welcome to the Guessing Game!")
print("You have 5 attempts to select the secret number.")
while attempts < 5:
    guess = int(input("Enter your guess (1-10): "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
        print(f"You have {5 - attempts} attempts left.")
    else:
        print("Too high! Try again.")
        print(f"You have {5 - attempts} attempts left.")
if attempts == 5 and guess != secret_number:
    print(f"Game over! The secret number was {secret_number}.")