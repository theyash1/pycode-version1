# check the strength of entered password or generate a new strong password
import random
import re

# function to check the strength of password
def check_password_strength(password):
    missing_criteria = []
    
    # check if the password length is less than 12 characters
    if len(password) < 12:
        missing_criteria.append(">minimum password length is 12 characters.")
    
    # check if the password contains at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        missing_criteria.append(">at least one uppercase letter required.")
    
    # check if the password contains at least one lowercase letter
    if not re.search(r'[a-z]', password):
        missing_criteria.append(">at least one lowercase letter required.")
    
    # check if the password contains at least one digit
    if not re.search(r'\d', password):
        missing_criteria.append(">at least one digit required.")
    
    # check if the password contains at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        missing_criteria.append(">at least one special character required.")

    return missing_criteria

# function to generate a random password
def generate_random_password():
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    special_characters = "!@#$%^&*(),.?\":{}|<>"

    # start with one character from each category
    password = random.choice(lowercase_letters)
    password += random.choice(uppercase_letters)
    password += random.choice(digits)
    password += random.choice(special_characters)

    # add 8 more characters randomly from all categories
    password += ''.join(random.choices(uppercase_letters + lowercase_letters + digits + special_characters, k=8))

    return ''.join(random.sample(password, len(password)))

def main():
    # prompt the user to enter a new password
    password = input(">Enter new password: ")
    while True:
        # check the strength of the password
        missing_criteria = check_password_strength(password)
        if missing_criteria:
            # if the password doesn't meet the criteria, display the missing criteria
            print(">Password doesn't meet the following criteria: ")
            for criteria in missing_criteria:
                print(criteria)
            
            # ask the user if they want to generate a random password
            choice = input(">do you want to generate a random password? (Y/N): ")
            if choice.lower() == 'y':
                # generate a random password and hide it with asterisks
                password = generate_random_password()
                hidden_password = '*' * len(password)
                print(f"Generated Password: {hidden_password}")
                # ask the user if they want to unhide the characters
                unhide_choice = input(">write 'S' to unhide the characters: ")
                if unhide_choice.lower() == 's':
                    # if the user wants to unhide the characters, display the generated password
                    print(f"Generated Password: {password}")
                    break
            else:
                # if the user doesn't want to generate a random password, prompt them to enter a new password
                password = input(">Enter new password: ")
        else:
            # if the password meets all criteria, break the loop
            print(">password meets all criteria!")
            break

if __name__ == "__main__":
    main()
