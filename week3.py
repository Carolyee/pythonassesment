#1. Modify your greeting program so that if the user does not enter a name, the program responds "Hello, Stranger!". Otherwise, it should print a greeting with their name.#

def greet_user():
    name = input("Enter your name: ").strip()
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, Stranger!")

greet_user()


#2. Write a program that simulates the way a user might choose a password. The program should prompt for a new password twice. If the two passwords match, the program should say "Password Set"; otherwise, it should report an error.#

def set_password():
    password1 = input("Enter a new password: ")
    password2 = input("Re-enter the password: ")
    if password1 == password2:
        print("Password Set")
    else:
        print("Error: Passwords do not match.")

set_password()


#3. Modify the previous program so that the password must be between 8 and 12 characters long.#

def set_password():
    password1 = input("Enter a new password: ")
    password2 = input("Re-enter the password: ")
    if password1 == password2 and 8 <= len(password1) <= 12:
        print("Password Set")
    else:
        print("Error: Passwords do not match or do not meet length requirements.")

set_password()


#4. Modify the program so that the chosen password cannot be one of a list of common passwords.#

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

def set_password():
    password1 = input("Enter a new password: ")
    password2 = input("Re-enter the password: ")
    if password1 == password2 and 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
        print("Password Set")
    else:
        print("Error: Invalid password.")

set_password()


#5. Modify the program so that it executes until the user successfully chooses a password.#

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

def set_password():
    while True:
        password1 = input("Enter a new password: ")
        password2 = input("Re-enter the password: ")
        if password1 == password2 and 8 <= len(password1) <= 12 and password1 not in BAD_PASSWORDS:
            print("Password Set")
            break
        else:
            print("Error: Invalid password. Try again.")

set_password()


#6. Write a program that displays the "Seven Times Table".#

def seven_times_table():
    for i in range(13):
        print(f"{i} x 7 = {i * 7}")

seven_times_table()

#7. Modify the "Times Table" program so that the user enters the number of the table they require. The number should be between 0 and 12 inclusive.#

def times_table():
    number = int(input("Enter a number between 0 and 12 for the times table: "))
    if 0 <= number <= 12:
        for i in range(13):
            print(f"{i} x {number} = {i * number}")
    else:
        print("Error: Number out of range.")

times_table()


#8. Modify the "Times Table" program so that if the number is negative, the table is printed backward.#

def times_table():
    number = int(input("Enter a number for the times table: "))
    if number >= 0:
        for i in range(13):
            print(f"{i} x {number} = {i * number}")
    else:
        for i in range(12, -1, -1):
            print(f"{i} x {abs(number)} = {i * abs(number)}")

times_table()













