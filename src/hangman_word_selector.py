import os
import random


def random_word() -> str:
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


def is_letter(char: str) -> bool:
    return char.isalpha()


def word_from_file() -> str:
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
            words = [word.strip() for word in file if len(word.strip()) > 0 and word.strip().isalpha()]

        if not words:
            print("No valid words found in file.")
            print("Only words containing strictly English letters are supported, try again.")
            continue

        return words[random.randrange(0, len(words))].upper()
