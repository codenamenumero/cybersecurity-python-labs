import random

secret_number = random.randint(1, 10)
attempts = 0

print("Welcome to the Guessing Game!")
print("Choose a difficulty level:")
print("1. Easy (1-10, 5 attempts)")
print("2. Medium (1-50, 7 attempts)")
print("3. Hard (1-100, 10 attempts)")



difficulty = int(input("Enter your choice (1-3): "))

if difficulty == 1:
    max_number = 10
    max_attempts = 5
elif difficulty == 2:
    max_number = 50
    max_attempts = 7
else:
    max_number = 100
    max_attempts = 10

while difficulty not in [1, 2, 3]:
    print("Invalid choice. Please select a difficulty level (1-3).")
    difficulty = int(input("Enter your choice (1-3): "))

secret_number = random.randint(1, max_number)
attempts = 0

print(f"You have {max_attempts} attempts to guess the number between 1 and {max_number}.")
while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
        print(f"You have {max_attempts - attempts} attempts left.")
    else:
        print("Too high! Try again.")
        print(f"You have {max_attempts - attempts} attempts left.")
if attempts == max_attempts and guess != secret_number:
    print(f"Game over! The secret number was {secret_number}.")