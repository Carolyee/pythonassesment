#1. Write a program that, when run from the command line, reports what operating system platform is being used.#
import sys

print(sys.platform)


#2. Write a program that, when run from the command line, reports how many arguments were provided.#
import sys

print(len(sys.argv) - 1)

#3. Write a program that takes a bunch of command-line arguments and prints out the shortest argument.#
import sys

if len(sys.argv) > 1:
    print(min(sys.argv[1:], key=len))
else:
    print("No arguments provided.")

 #4. Write a program that takes a URL as a command-line argument and reports whether or not there is a working website at that address.#
    import sys
import requests

if len(sys.argv) > 1:
    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("The website is working.")
        else:
            print(f"The website returned status code {response.status_code}.")
    except requests.RequestException:
        print("The website is not accessible.")
else:
    print("No URL provided.")


 #5. Write a program that takes temperature readings from the command line and displays the maximum, minimum, and mean. Handle the case where no arguments are provided.#
    import sys

if len(sys.argv) > 1:
    try:
        temperatures = list(map(float, sys.argv[1:]))
        print(f"Max: {max(temperatures)}")
        print(f"Min: {min(temperatures)}")
        print(f"Mean: {sum(temperatures) / len(temperatures)}")
    except ValueError:
        print("Please provide valid numeric temperature readings.")
else:
    print("No temperature readings provided.")

#6. Write a program that takes the name of a file as a command-line argument and creates a backup copy of that file.#
    import sys
import shutil

if len(sys.argv) > 1:
    original_file = sys.argv[1]
    backup_file = original_file + ".backup"
    try:
        shutil.copy(original_file, backup_file)
        print(f"Backup created: {backup_file}")
    except FileNotFoundError:
        print("The specified file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("No file name provided.")
