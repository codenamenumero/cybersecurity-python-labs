import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits 
    include_special = input("Include special characters? (y/n): ").lower()
    if include_special == 'y':
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
length = int(input("Enter the desired password length: "))
password = generate_password(length)
print("Generated password:", password)