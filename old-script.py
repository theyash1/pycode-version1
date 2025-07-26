import random
import re

def check_password_strength(password):
    missing_criteria = []
    
    if len(password) < 12:
        missing_criteria.append(">minimum password length is 12 characters.")
    
    if not re.search(r'[A-Z]', password):
        missing_criteria.append(">at least one uppercase letter required.")
    
    if not re.search(r'[a-z]', password):
        missing_criteria.append(">at least one lowercase letter required.")
    
    if not re.search(r'\d', password):
        missing_criteria.append(">at least one digit required.")
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        missing_criteria.append(">at least one special character required.")

    return missing_criteria

def generate_random_password():
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    special_characters = "!@#$%^&*(),.?\":{}|<>"

    password = random.choice(lowercase_letters)
    password += random.choice(uppercase_letters)
    password += random.choice(digits)
    password += random.choice(special_characters)

    password += ''.join(random.choices(uppercase_letters + lowercase_letters + digits + special_characters, k=8))

    return ''.join(random.sample(password, len(password)))

def main():
    password = input(">Enter new password: ")
    while True:
        missing_criteria = check_password_strength(password)
        if missing_criteria:
            print(">Password doesn't meet the following criteria: ")
            for criteria in missing_criteria:
                print(criteria)
            
            choice = input(">do you want to generate a random password? (Y/N): ")
            if choice.lower() == 'y':
                password = generate_random_password()
                hidden_password = '*' * len(password)
                print(f"Generated Password: {hidden_password}")
                unhide_choice = input(">write 'S' to unhide the characters: ")
                if unhide_choice.lower() == 's':
                    print(f"Generated Password: {password}")
                    break
            else:
                password = input(">Enter new password: ")
        else:
            print(">password meets all criteria!")
            break

if __name__ == "__main__":
    main()
