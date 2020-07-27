# Row Program - spacing and alignment
# Robyn Lesch
# 8 May 2020
# Mood: relaxed

from __future__ import print_function                                       # allows to print formatted string

number = int(input("Please enter start number: ")) - 1                      # "-1" to include input in output

i = number + 8

if -6 < number < 93:
    while i > number:                                                       # while loop to make continuous
        number = number + 1
        print(format(" ".join(str(i) for i in range(number, i))), sep="  ")  # formatted string
        break
