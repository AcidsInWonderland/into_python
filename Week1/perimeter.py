# Perimeter
# Robyn Lesch
# 5 May 2020
# Mood: Proud

# user inputs to calculate
width_1 = float(input("Please enter Width 1: "))                     
height_1 = float(input("Please enter Height 1: "))

perimeter_1 = 2 * (width_1 + height_1)

width_2 = float(input("Please enter Width 2: "))
height_2 = float(input("Please enter Height 2: "))

perimeter_2 = 2 * (width_2)

# formula to calculate perimeter 
total_perimeter = perimeter_1 + perimeter_2
print("Total fence required = ", total_perimeter, " meters")

price = float(input("Please enter the price per meter (rands): "))

# price calculation
total_price = total_perimeter * price
print("The total price = R ", total_price)
