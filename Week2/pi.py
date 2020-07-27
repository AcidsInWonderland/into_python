# Area of a Circle and Turtle
# Robyn Lesch
# 8 May 2020
# Mood: relieved

from math import sqrt                                                       # used for the while loop calculation

root = 2*(2/sqrt(2))                                                        # separating fraction for easy understanding
denominator = sqrt(2)
pi = root

while 2 / sqrt(2 + denominator) > 1:                                        # while loop as instructed
    pi = pi * 2 / sqrt(2 + denominator)
    denominator = sqrt(2 + denominator)
print("Approximation of pi: %s" % (round(pi, 3)))                           # rounding pi off to 3 decimal points

radius = float(input("Please enter the radius of the circle: "))            # users input for calculation

area = round(pi * radius * radius, 3)                                       # formula for area of a circle
print("Area of circle : ", area, "square units.")                            # printed answer with units
