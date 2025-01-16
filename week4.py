#1. Write a function that accepts a single integer as a parameter and returns True if the integer is in the range 0 to 100 (inclusive), or False otherwise.#
def validate_range(number):
    return 0 <= number <= 100

print(validate_range(50))  
print(validate_range(150))  


# 2. Write a function that takes a string as its parameter and returns the number of uppercase letters and the number of lowercase letters in the string.#
def count_case(string):
    uppercase = sum(1 for char in string if char.isupper())
    lowercase = sum(1 for char in string if char.islower())
    return uppercase, lowercase

print(count_case("Hello World"))  
print(count_case("Python123"))  


#3. Modify your "greetings" program so that the first letter of the name entered is always in uppercase, with the rest in lowercase.#
def greet_user():
    name = input("Enter your name: ").strip().capitalize()
    print(f"Hello, {name}!")

greet_user()

#4. Write a function that takes a string parameter and returns it with the last character removed. If the string contains one or fewer characters, return it unchanged.#
def remove_last_char(string):
    return string[:-1] if len(string) > 1 else string

print(remove_last_char("Hello"))  
print(remove_last_char("A"))  

#5. Write a function that converts a temperature in degrees centigrade to fahrenheit, and another that does the reverse conversion.#
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(celsius_to_fahrenheit(0))  
print(fahrenheit_to_celsius(32))  

#6.Write a program that takes a centigrade temperature input and displays the equivalent in fahrenheit. The input should be a number followed by a letter 'C'.#
def convert_temp():
    temp = input("Enter temperature in centigrade (e.g., 25C): ").strip()
    if temp[-1].upper() == 'C' and temp[:-1].isdigit():
        celsius = float(temp[:-1])
        fahrenheit = celsius * 9/5 + 32
        print(f"{fahrenheit}F")
    else:
        print("Invalid input.")

convert_temp()

#7. Write a program that reads 6 centigrade temperatures and displays the maximum, minimum, and mean of the values.#
def process_temps():
    temps = []
    for _ in range(6):
        temp = input("Enter temperature in centigrade (e.g., 25C): ").strip()
        if temp[-1].upper() == 'C' and temp[:-1].isdigit():
            temps.append(float(temp[:-1]))
        else:
            print("Invalid input.")
    print(f"Max: {max(temps)}C")
    print(f"Min: {min(temps)}C")
    print(f"Mean: {sum(temps) / len(temps)}C")

process_temps()

#8. Modify the previous program so it can process any number of values, terminating when the user presses "Enter" without input.#
def process_temps_dynamic():
    temps = []
    while True:
        temp = input("Enter temperature in centigrade (e.g., 25C) or press Enter to finish: ").strip()
        if not temp:
            break
        if temp[-1].upper() == 'C' and temp[:-1].isdigit():
            temps.append(float(temp[:-1]))
        else:
            print("Invalid input.")
    if temps:
        print(f"Max: {max(temps)}C")
        print(f"Min: {min(temps)}C")
        print(f"Mean: {sum(temps) / len(temps)}C")
    else:
        print("No temperatures entered.")

process_temps_dynamic()
