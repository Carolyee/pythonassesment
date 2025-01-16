#1. Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's'].# 

def unique_letters(string):
    return sorted(set(char.lower() for char in string if char.isalpha()))

print(unique_letters("cheese"))  
print(unique_letters("Hello World!"))  



#2.Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
Hint: These could all be done programmatically, but consider carefully what topic we
have been discussing this week! Each function can be exactly one line.#

def letters_in_either(word1, word2):
    return sorted(set(word1.lower()) | set(word2.lower()))

def letters_in_both(word1, word2):
    return sorted(set(word1.lower()) & set(word2.lower()))

def letters_in_either_not_both(word1, word2):
    return sorted(set(word1.lower()) ^ set(word2.lower()))

print(letters_in_either("cheese", "bread"))         
print(letters_in_both("cheese", "bread"))           
print(letters_in_either_not_both("cheese", "bread"))  


#3. Write a program that manages a list of countries and their capital cities. It should
prompt the user to enter the name of a country. If the program already "knows"
the name of the capital city, it should display it. Otherwise it should ask the user to
enter it. This should carry on until the user terminates the program (how this
happens is up to you).
Note: A good solution to this task will be able to cope with the country being entered
variously as, for example, "Wales", "wales", "WALES" and so on.#

def manage_countries():
    countries = {}
    while True:
        country = input("Enter the name of a country (or type 'quit' to exit): ").strip().capitalize()
        if country.lower() == 'quit':
            print("Exiting program. Final data:", countries)
            break
        if country in countries:
            print(f"The capital of {country} is {countries[country]}.")
        else:
            capital = input(f"I don't know the capital of {country}. Please enter it: ").strip().capitalize()
            countries[country] = capital
            print(f"Thank you! Added {country}: {capital} to the database.")

manage_countries()



#4. One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the different symbols in the message can be us
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same.
Hint: There are many ways to do this. It is obviously a dictionary, but we will want
zero counts, so some initialisation is needed. Also, sorting dictionaries is tricky, so
best to ignore that initially, and then check the usual resources for the runes.#

from collections import Counter

def frequency_analysis(message):
    message = message.lower()
    letter_counts = Counter(char for char in message if char.isalpha())
    most_common = letter_counts.most_common(6)
    for letter, count in most_common:
        print(f"{letter}: {count}")

frequency_analysis("This is an example message with repeated letters!")
