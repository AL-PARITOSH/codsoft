import random
import string

def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=True):
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set (uppercase, lowercase, digits, special characters) must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")

        uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        digits = input("Include digits? (y/n): ").lower() == 'y'
        special_chars = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, uppercase, lowercase, digits, special_chars)
        print("Generated Password:", password)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
