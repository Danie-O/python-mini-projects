# import dependencies
import random
import string

# Generate a random password given a number of params as specified by a user 
def generate_pwd(min_length: int, numbers: bool=True, special_characters: bool=True) -> string:
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    # initialise 'password bank' to contain only letters and update based on params supplied as arguments
    password_bank = letters
    if numbers:
        password_bank += digits
    if special_characters:
        password_bank += special_characters

    password = ""
    criteria_met = False
    has_numbers = False
    has_special_characters = False

    # create password by randomly selecting a character from the password bank until criteria are met or length is exceeded
    while not criteria_met or len(password) < min_length:
        next_char = random.choice(password_bank)
        password += next_char

        # check kind of added character to help with checking whether criteria has been met
        if next_char in digits:
            has_numbers = True
        elif next_char in special_characters:
            has_special_characters = True

        # update criteria_met based on added character
        criteria_met = True
        if numbers:
            criteria_met = has_numbers
        if special_characters:
            criteria_met = criteria_met and has_special_characters
        
    return password


# Test function
min_length = int(input('Enter the minimum length of your password: '))
numbers = input("Do you want your password to contain numbers (y/n)").lower() == "y"
special_characters = input("Do you want your password to contain special characters (y/n)").lower() == "y"

password = generate_pwd(min_length, numbers, special_characters)
print(f"Your randomly generated password is: {password}")
