# Word Guess Game
# Robyn Lesch
# 5 May 2020
# Mood: impressed

# user friendly introduction
import random
name = input("What is your name? ")
print("Good luck ", name, "!")

# random choice of word, hint to help
words = ["books", "paper", "phone"]
word = random.choice(words)
print("Hint: 5 letter word of things you could find on a desk.")

# while loop for guesses that aren't infinate 
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = (input("Guess: "))
    guess_count += 1
    if guess != word:
        print("Wrong! Try again.")
    if guess == word:
        print("YOU WON!")
        break

else:
    print("Sorry, you lost.")
