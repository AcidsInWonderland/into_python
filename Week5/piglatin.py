# Pig Latin Exercise
# Robyn Lesch
# 10 June 2020
# Mood: okay

# for the program to identify what needs to be changed
vowels = ("A", "E", "I", "O", "U", "a", "e", "i", "o", "u")

# explains to the program how to change the sentence word by word 
def toPigLatin(s):
    sentence = s.split(" ")
    latin = ""
    for word in sentence:
        if word[0] in vowels:
            latin += word + "way" + " "
        else:
            vowel_index = 0
            for letter in word:
                if letter not in vowels:
                    vowel_index += 1
                    continue
                else:
                    break
            latin += word[vowel_index:] + "a" + word[:vowel_index] + "ay" + " "
    return latin[:len(latin) - 1]

# how to translate the word to english
def toEnglish(s):
    sentence = s.split(" ")
    english = ""
    for word in sentence:
        if word[:len(word) - 4:-1] == "yaw":
            english += word[:len(word) - 3] + " "
        else:
            noay = word[:len(word) - 2]
            firstconsonants = noay.split("a")[-1]
            consonantsremoved = noay[:len(noay) - (len(firstconsonants)+1)]
            english += firstconsonants + consonantsremoved + " "
    return english

# to test the module, input is needed 
userInput = input("(E)nglish or (P)ig Latin?")
if userInput.upper() == "E":
    text = input("Please enter English sentence: ")
    print(toPigLatin(text))
elif userInput.upper() == "P":
    text = input("Please enter Pig Latin sentence: ")
    print(toEnglish(text))
else:
    print("Invalid input.")
