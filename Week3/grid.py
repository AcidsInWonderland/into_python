# Grid Program - spacing and alignment
# Robyn Lesch
# 11 May 2020
# Mood: proud

number = int(input("Please enter the start number which lies between -6 and 2: "))                  # user input

i = number + 41                                                                                     # upper range limit

for leftmost in range(number, i, 7):                                                                # for loop
    for value in range(leftmost, leftmost + 6):                                                     # nested for loop
        print("{0:2d}".format(value), end=" ")                                                      # formatted print
    print("{0:2d}".format(leftmost+6))                                                              # original loop's output
