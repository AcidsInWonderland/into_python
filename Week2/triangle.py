# Area of Triangle
# Robyn Lesch
# 7 May 2020
# Mood: excited

# user inputs
side_1 = int(input("Enter the length of the first side: "))
side_2 = int(input("Enter the length of the second side: "))
side_3 = int(input("Enter the length of the third side: "))

import math                                                         # math module used for calculations
semiperimeter = 0.5 * (side_1 + side_2 + side_3)                    # semiperimeter is "s" used in area calculation

# formula to calculate using inputs and printing the answer
area = math.sqrt(semiperimeter * (semiperimeter - side_1) * (semiperimeter - side_2) * (semiperimeter - side_3))
print("The area of the triangle with sides of length ", side_1, "and " , side_2 , " and ",  side_3, "is " , area , "square units.")
