# Bukiyip
# Robyn Lesch
# 10 June 2020
# Mood: lost

# defining bukiyip module
def digit_to_character(digit):
    if digit < 10: return chr(ord('0') + digit)
    else: return chr(ord('a') + digit - 10)

def str_base(number,base):
    if number < 0:
        return '-' + str_base(-number,base)
    else:
        (d,m) = divmod(number,base)
    if d:
        return str_base(d,base) + digit_to_character(m)
    else:
        return digit_to_character(m)

# functions to determine output
def bukiyip_to_decimal(a):
    return int(str(a),3)

def decimal_to_bukiyip(a):
    return str_base(int(a),3)

def bukiyip_add(a,b):
    n1 = bukiyip_to_decimal(a) + bukiyip_to_decimal(b)
    return decimal_to_bukiyip(n1)

def bukiyip_multiply(a, b):
    n1 = bukiyip_to_decimal(a) * bukiyip_to_decimal(b)
    return decimal_to_bukiyip(n1)

# so the user knows how to format input
print("d <number> : convert given decimal number to base-3.")
print("b <number> : convert given base-3 number to decimal.")
print("a <number> <number>: add the given base-3 numbers.")
print("m <number> <number> : multiply the given base-3 numbers.")
print("q: quit.")

# commands for the program to follow
while(1):
    command = input("Enter a command (d, b, a, m, or q): ")
    attributes = command.split(" ")
    function = attributes[0]

    if function == 'd':
        print(decimal_to_bukiyip(attributes[1]))
    elif function == 'b':
        print(bukiyip_to_decimal(attributes[1]))
    elif function == 'a':
        print(bukiyip_add(attributes[1],attributes[2]))
    elif function == 'm':
        print(bukiyip_multiply(attributes[1],attributes[2]))
    else:
        print("Quitting the program.")
    break
    
