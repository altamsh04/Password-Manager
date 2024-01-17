import hashlib
import random
import time

def print_header(title):
    print("\n" + "*"*37)
    print(f"{'*'*(12 + len(title))}\n*{title:^{35}}*")
    print(f"{'*'*(12 + len(title))}\n" + "*"*37)

def string_to_hash_converter():
    print("-"*36 + "\n1] String To Hash Converter\n")
    user_input = input(">Enter Your String : ")
    print("Processing......")
    time.sleep(3)
    hashed_value = hashlib.md5(user_input.encode()).hexdigest()
    print(f"\nMd5 Value: {hashed_value}")

def password_strength_checker():
    print("-"*36 + "\n2] Password Strength Checker\n")
    print("*Disclaimer: Password must contain Uppercase, Lowercase, Special Symbols, Digits and be greater than 8 characters*\n")
    password = input(">Enter Your password : ")

    requirements = [
        any(char.isupper() for char in password),
        any(char.islower() for char in password),
        any(char.isdigit() for char in password),
        any(char in "(){}[]\\|:;,.<>?/!@#%^&*-+=_" for char in password),
        len(password) > 8
    ]

    if all(requirements):
        print("\nPassword is Strong: " + password)
    else:
        print("Password is not Strong & does not meet all requirements!")
        print("Try Again!")

def random_password_generator():
    print("-"*36 + "\n3] Random Password Generator\n")
    pass_length = int(input(">Enter Password Length : "))

    if pass_length <= 8:
        print("Password must be greater than 8!")
    else:
        all_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+={}[]\\|;:*'<>/?,."
        password = "".join(random.sample(all_characters, pass_length))

        print("Generating password.....\n")
        time.sleep(2)
        print(f"Password Is: {password}\n")

        for char in password:
            time.sleep(0.3)
            print(f"Shuffling password: {char}")

        time.sleep(1)
        shuffled_password = "".join(random.sample(password, pass_length))
        print(f"\nRandom strong password is: {shuffled_password}")

def create_strong_password():
    print("-"*36 + "\n4] Create Strong Password\n")

    name = input(">Enter Any Name, Target Name (no commas): ")
    pet_name = input(">Enter Any Pet Name (no commas): ")
    nick_name = input(">Enter Any Nick Name, Fav movies, Organization: ")
    birth_date = input(">Enter Any Birth Date (dd/mm/yy): ")
    email_id = input(">Enter Any Email_Id Related To Target: ")
    old_password = input(">Enter Any Old Password: ")
    pass_length = int(input(">Enter Any Password length: "))

    guess = name + pet_name + nick_name + birth_date + email_id + old_password

    if len(guess) <= 8:
        print("\nPassword must be greater than 8!")
    else:
        print("\nCreating strong password...")
        time.sleep(2)
        strong_password = "".join(random.sample(guess, pass_length))
        print(f"\nYour Strong Password Is: {strong_password}")

if __name__ == "__main__":
    print("\n\n" + "*"*37)
    print_header("PYTHON PASSWORD MANAGER TOOL")
    print_header("Made by - Altamsh Bairagdar")
    time.sleep(2)
    print("\n1.String To Hash Converter\n2.Password Strength Checker\n3.Random Password Generator\n4.Create Strong Password")

    user_input = int(input("\n>Enter Your Choice : "))

    if user_input == 1:
        string_to_hash_converter()
    elif user_input == 2:
        password_strength_checker()
    elif user_input == 3:
        random_password_generator()
    elif user_input == 4:
        create_strong_password()
