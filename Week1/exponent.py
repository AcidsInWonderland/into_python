# Exponential Calculations
# Robyn Lesch
# 5 May 2020
# Mood: proud 

# fundamental calculation for exponential functions
base = int(input("Base: "))
exponent = int(input("Exponent: "))

def raise_to_power(base, exponent):
    result = 1
    for index in range(exponent):
        result *= base
    return(result)

# Have the computer calculate for you
print("Exponential value is: ", base ** exponent)

# have the computer calculate for you using thr maths module
print("Exponential value is: ", pow(base, exponent))

# another way to make the computer do it for you
print("Exponential value is: ", raise_to_power(base, exponent))
