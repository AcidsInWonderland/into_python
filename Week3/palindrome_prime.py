# Palindrome Prime  - prime number program
# Robyn Lesch
# 12 May 2020
# Mood: content

print(" ")  # to make the output screen look aesthetic 

N = int(input("Enter the start point (N): "))                             # User input
M = int(input("Enter the end point (M): "))
print("The palindromic primes are:")                                      # output heading


def palindrome(number):                                                   # Palindrome test
    return str(number) == str(number)[::-1]


def is_prime(number):                                                      # Prime test
    if number < 0:
        number *= -1
    index = 2
    while index * index <= number:
        if number % index == 0:
            return False
        index += 1
    return True


for y in range(N, M):                                                      # range does not include last inputs
    if palindrome(y) and is_prime(y):                                      # Check for palindrome and prime number
        print(y)                                                           # print result
