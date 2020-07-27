# Column Program - spacing and alignment
# Robyn Lesch
# 8 May 2020 - 11 May 2020
# Mood: anxious

from __future__ import print_function                                                   # allows to print formatting

number = int(input("Please enter the start number which lies between -6 and 2: "))      # user input

i = number + 41                                                                         # upper limit of range

for number in list(range(number, i, 7)):                                                # function
        print("{0:2d}".format(number))                                                  # formatting the print
