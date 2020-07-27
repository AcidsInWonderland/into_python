# Calender Utilities - Calutil
# Robyn Lesch
# 10 June 2020
# Mood: ugh

import os

import re

# functions used in python
class calutils():
    def __init__(self):
        print("Test harness for Calender utilities");

# defining the functions
    def findleapYear(self, year):
        print
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

# choice of functions
    def userSelected(self, userChoice):
        global month_number
        if (userChoice == 0):
            print("Terminating program.")

        if (userChoice == 1):
            year = int(input("Enter a year: "))
            # selected year sent to function
            if c.findleapYear(year):
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))

        if (userChoice == 2):
            monthDict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                         7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
            for i in range(0, 12):
                    i += 1
                    print(F"Month {i} is {monthDict[i]}.")

        if (userChoice == 3):
            year = int(input("Enter the year (4 digits): "))
            month_number = int(input("Enter month number: "))
            days_in_month = 0
            if month_number in [1, 3, 5, 7, 8, 10, 12]:
                days_in_month = 31
            elif month_number in [4, 6, 9, 11]:
                days_in_month = 30
            elif month_number == 2:
                if c.findleapYear(year):
                    days_in_month = 29
                else:
                    days_in_month = 28
            print("The days in the month with number " + str(month_number) + " in year " + str(year) + " is " + str(days_in_month) + ".")

        if (userChoice == 4):
            year = int(input("Enter the year (4 digits): "))
            import datetime
            a = datetime.datetime(year, 1, 1)
            print("The 1st of January ", year, " falls on a", a.strftime("%A"), ".")

        if (userChoice == 5):
            year = int(input("Enter the year (4 digits): "))
            month_number = int(input("Enter month number: "))
            import datetime
            a = datetime.datetime(year, month_number, 1)
            (print("The 1st day of month ", month_number, "of", year, " falls on a", a.strftime("%A"), "."))

# printing the options for easy use 
c = calutils()
print("Choose one the following options: ")
print("0. quit")
print("1. Test is_leap_year().")
print("2. Test month_name().")
print("3. Test days_in_month().")
print("4. Test first_day_of_year().")
print("5. Test first_day_of_month().")

userChoice = int(input("Your selection: "))
# selected choice sent to function

c.userSelected(userChoice);

