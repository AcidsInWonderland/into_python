# Acronym
# Robyn Lesch
# 17 June 2020
# Mood: exhausted

ignoreStrings = input("Enter words to be ignored separated by commas: \n")
ignoreList = ignoreStrings.split(",")
title = input("Enter a title to generate its acronym: \n")
titleList = title.split()

from builtins import any as b_any
print("The acronym is:")
for x in titleList:
    if (b_any(x.lower() in y.lower() for y in ignoreList)):
        print("", end="")
    else:
        print(x[0].upper(), end="")
