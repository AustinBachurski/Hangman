import os
import random


def random_word():
    words = [
        "PYTHON",
        "HANGMAN",
        "COMPUTER",
        "PROGRAM",
        "FUNCTION",
        "VARIABLE",
        "KEYBOARD",
        "MONITOR",
        "PRINTER",
        "NETWORK",
        "INTERNET",
        "SOFTWARE",
        "HARDWARE",
        "ALGORITHM",
        "DEBUGGING",
        "DATABASE",
        "PROCESSOR",
        "LANGUAGE",
        "SYNTAX",
        "COMPILER"
    ]

    return words[random.randrange(0, len(words))]


def word_from_file():
    os.system("cls")

    while True:
        filename = input("Please enter the name of a text file in the local directory: ")

        if not filename.endswith(".txt"):
            print("Only accepting '.txt' files at this time, try again.")
            continue

        if not os.path.exists(filename):
            print(f"{filename} was not found in the local directory, try again.")
            continue

        with open(filename, 'r') as file:
            words = [word.strip() for word in file if len(word.strip()) > 0]

            if not words:
                print("No words found in file, try again.")
                continue

            selection = ""
            while len(selection) < 1:
                selection = words[random.randrange(0, len(words))]
                print(selection)

            return selection.upper()
