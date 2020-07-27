# Vector Math
# Robyn Lesch
# 13 June 2020
# Mood: confident

print("\n *** Vector Math ***")
# importing math module
import math

# inputs and how to interpret
A = input("Enter vector A: ")
A = list(map(int, A.split()))
B = input("Enter vector B: ")
B = list(map(int, B.split()))

# formulas and functions 
def addition(vectorA, vectorB):
   return [i + j for i, j in zip(vectorA, vectorB)]


def dotProduct(vectorA, vectorB):
   return sum([i * j for i, j in zip(vectorA, vectorB)])


def getNorm(vectorA):
   norm = math.sqrt(sum(map(lambda x: x * x, vectorA)))
   return format(norm, ".2f")


def gettingNorm(vectorB):
   norm = math.sqrt(sum(map(lambda x: x * x, vectorB)))
   return format(norm, ".2f")

# ouputs 
print("A+B = "+str(addition(A, B)))
print("A.B = "+str(dotProduct(A, B)))
print("|A| = "+str(getNorm(A)))
print("|B| = "+str(gettingNorm(B)))
