# First Day Program
# Robyn Lesch
# 7 May 2020 - 8 May 2020
# Mood: tired

import datetime                                                                     # module that understands dates

year_1 = int(input("Enter first year: "))                                           # user input
year_2 = int(input("Enter second year: ")) + 1                                      # "+1" allows for inclusive range

while year_1 < year_2:                                                              # while loop to continue output
    a = datetime.datetime(year_1, 1, 1)                                             # outputs first day (month 1, day 1)
    print("The 1st of January ", year_1, " falls on a", a.strftime("%A"),".")       # converts int to str
    year_1 += 1
    if year_1 == year_2:                                                            # ends when years are equivalent
        break
