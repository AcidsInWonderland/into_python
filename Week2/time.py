# Testing the validity of Input Time
# Robyn Lesch
# 7 May 2020
# Mood: enthusiastic 

# user inputs
hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

# testing validity if it falls within range
if int(hours) in range(0, 24) and int(minutes) in range(0, 60) and int(seconds) in range(0, 60):
    print("Your time is valid.")
else:
    print("Your time is invalid.")
