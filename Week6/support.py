# Support
# Robyn Lesch
# 13 June 2020
# Mood: excited

print("\n *** Support ***")
def keyword(word):
    # selects phrase from dictionary
    key_phrases = {
        "Crashed": "Are the drivers up to date?",
        "Blue": "Ah, the blue screen of death. And then what happened?",
        "Hacked": "You should consider installing anti-virus software.",
        "Bluetooth": "Have you tried mouthwash?",
        "Apple": "You do mean the computer kind?",
        "Windows": "Ah, I think I see your problem. What version?",
        "Spam": "You should see if your mail client can filter messages.",
        "Connection": "Contact Telkom."
    }

    answer = key_phrases.get(word, "Curious, tell me more.")
    return answer


def main():
    # main for automarking
    welcome = "Welcome to the automated technical support. \nPlease describe your problem: "
    running = True

    while running:
        option = input(welcome + "\n").capitalize()
        if option == "Quit":
            running = False
            print("I trust my service has been satisfactory.")
            break 
        else:
            welcome = keyword(option)


if __name__ == "__main__":
    main()
