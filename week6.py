#Write a function that accepts a positive integer as a parameter and then returns a representation of that number in binary (base 2).#

def to_binary(number):
    return bin(number)[2:]

print(to_binary(10))  
print(to_binary(255)) 




#2. Write a function that takes an integer as its parameter and returns the factors of that integer.#
def factors(number):
    return [i for i in range(1, number + 1) if number % i == 0]

print(factors(28))  
print(factors(15))  




#3. Write a function that determines if a given integer is a prime number.#
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(29))  
print(is_prime(15))  


#4. Write a function that takes a string containing a message and encrypts it by removing the spaces and reversing the resulting string.#
def encrypt_message(message):
    return ''.join(message.split())[::-1]

print(encrypt_message("Hello World"))  
print(encrypt_message("Python is great"))  




#5. Write a function that encrypts a message by spacing the letters out randomly, using an interval between 2 and 20, and filling the gaps with random letters. The function should return the encrypted message and the interval used.#
import random
import string

def random_encrypt(message):
    interval = random.randint(2, 20)
    result = []
    index = 0
    for char in message:
        while len(result) < index:
            result.append(random.choice(string.ascii_lowercase))
        result.append(char)
        index += interval
    while len(result) < index:
        result.append(random.choice(string.ascii_lowercase))
    return ''.join(result), interval

encrypted_message, interval = random_encrypt("send cheese")
print(encrypted_message, interval)


#6. Write a program that decrypts messages encoded as above.#
def random_decrypt(encrypted_message, interval):
    return ''.join(encrypted_message[i] for i in range(0, len(encrypted_message), interval))

decrypted_message = random_decrypt(encrypted_message, interval)
print(decrypted_message)