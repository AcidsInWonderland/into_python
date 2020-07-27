# Password Generator
# Robyn Lesch
# 7 May 2020
# Mood: proud 

import string                                                  # imports the library

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
special = string.punctuation
everything = lower + upper + numbers + special                 # makes the password more difficult to crack

import random                                                  # allows program to randomize components

password = random.choice(everything) + random.choice(lower) + random.choice(everything) + random.choice(upper) + random.choice(everything) + random.choice(numbers) + random.choice(everything) + random.choice(special) + random.choice(everything)

print("Password is: ", password)                                                # generates strong password because its completely random
