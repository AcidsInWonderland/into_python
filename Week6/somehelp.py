# Some Help
# Robyn Lesch
# 13 June 2020
# Mood: bored

print("*** Some Help ***")
import random

# list of responses to return
ExpectedResponse = [
    "Have you tried it on a different operating system?",
    "Did you reboot it?",
    "What colour is it?",
    "You should consider installing anti-virus software.",
    "Contact Telkom.",
    "I should get that looked at if I were you."
]

def main():
    # main for automarking
    print("Welcome to the automated technical support system. Please describe your problem: ")

    running = True
    while running:
        answer = input(" ")

        # if user enters "quit", break the loop with a closing statement
        if answer.lower() == "quit":
            print("I trust my service has been satisfactory.")
            running = False
            # else continue with questions
        else:
            question = ExpectedResponse
            print(random.choice(question))


if __name__ == '__main__':
    main()
    
