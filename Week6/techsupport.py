# Tech Support
# Robyn Lesch
# 14 June 2020
# Mood: happy

print("\n *** Tech Support ***")

def keyword(word):
    # selects phrase from dictionary which contains keyword
    key_phrases = {
        "Crashed": "Are the drivers up to date?",
        "Blue": "Ah, the blue screen of death. And then what happened?",
        "Hacked": "You should consider installing anti-virus software.",
        "Bluetooth": "Have you tried mouthwash?",
        "Apple": "You do mean the computer kind?",
        "Windows": "Ah, I think I see your problem. What version?",
        "Spam": "You should see if your mail client can filter messages.",
        "Connection": "Contact Telkom.",
        " ": "Curious, tell me more."
    }

    # None set up for looping through sentence
    answer = key_phrases.get(word, None)
    return answer


def find(sentence):
    # searches if a word in sentence is connected to  response
    words = sentence.split(" ")
    # append a space to the end of list to terminate loop
    # when all options have been searched and returned unsuccessful.
    words.append(" ")
    i = 0
    response = None
    while not response:
        w = words[i]
        response = keyword(w)
        i += 1
    return response


def main():
    # main for automarking
    welcome = "Welcome to the automated technical support. \nPlease describe your problem: "
    running = True

    while running:
        option = input(welcome + "\n").title()
        if option == "Quit":
            print("I trust my service has been satisfactory.")
            running = False
        else:
            welcome = find(option)


if __name__ == "__main__":
    main()
