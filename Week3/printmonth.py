# Print Month - calender program
# Robyn Lesch
# 11 May 2020 - 26 May 2020
# Mood: bleh

# user inputs for functionality of program
month_name = input("Please enter the month e.g. January: ").capitalize()
first_weekday = input("Please enter the day you'd like your calender to start on e.g. Sunday: ").capitalize()

# dictionary to store keys
days = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

# because dictionary, keys are false
week_full = False

# formatting the numbers with the heading
print("Mo", "Tu", "We", "Th", "Fr", "Sa", "Su")
for space in range(days[first_weekday]):
    print("  ", end=" ")

# if statement to determine number of days in month and to format the range
if month_name == "February":
    for leftmost in range(1, 29, 7):
        for value in range(leftmost, leftmost + 6):
            if (days[first_weekday] + value) % 7 == 0:
                week_full = True
            if week_full:
                print("{:2d}".format(value))
                week_full = False
            else:
                print("{:2d}".format(value), end=" ")
        print("{:2d}".format(leftmost + 6), end=" ")

# if statement to determine number of days in month and to format the numbers
elif month_name in ["April", "June", "September", "November"]:
    for leftmost in range(1, 31, 7):
        for value in range(leftmost, leftmost + 6):
            if (days[first_weekday] + value) % 7 == 0:
                week_full = True
            if week_full and value < 31:
                print("{:2d}".format(value))
                week_full = False
            elif value < 31:
                print("{:2d}".format(value), end=" ")
        if value < 31:
            print("{:2d}".format(leftmost + 6), end=" ")

# if statement to determine number of days in month and how to format accordingly
elif month_name in ["January", "March", "May", "July", "August", "October", "December"]:
    for leftmost in range(1, 32, 7):
        for value in range(leftmost, leftmost + 6):
            if (days[first_weekday] + value) % 7 == 0:
                week_full = True
            if week_full and value < 31:
                print("{:2d}".format(value))
                week_full = False
            elif value < 32:
                print("{:2d}".format(value), end=" ")
        if value < 32:
            print("{:2d}".format(leftmost + 6), end=" ")
