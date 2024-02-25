import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = ''
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("Please include at least one character set for the password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Password length should be a positive integer.")

        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
        print(f"Generated Password: {password}")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid input.")

password_generator()
