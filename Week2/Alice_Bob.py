# Hacker Rank Problem - Alice_Bob
# Robyn Lesch
# 7 May 2020
# Mood: lol, big

# Compare Triplets Challenge

# user inputs
Alice = list(map(int, input("Please enter Alice's 3 integers (separated by spaces): ").split()))
Bob = list(map(int, input("Please enter Bob's 3 integers (separated by spaces): ").split()))

# initial scoring
alice_score = 0
bob_score = 0

# basis for comparison
for i in range(3):
    if Alice[i] > Bob[i]:
        alice_score += 1

    elif Alice[i] < Bob[i]:
        bob_score += 1

# printing final results
print("Alice scored" , alice_score,"point(s) and" , "Bob scored", bob_score, "point(s).")
