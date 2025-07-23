"""Free functions for selecting a word to be guessed."""

# Importing the external `os` module - used to clear the terminal text.
import os
# Importing the external `random` module - used to generate random numbers.
import random


# Free function for automatically selecting a secret word.
def random_word() -> str:
    # A list of secret words.
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

    # A word is selected at random by generating a random number
    # from zero to the number of words in the list.
    return words[random.randrange(0, len(words))]


# Free function for selecting a word from a player provided list via text file.
def word_from_file() -> str:
    # Clear the screen.
    os.system("cls")

    # Prompt the user for a file name.
    while True:
        filename = input("Please enter the name of a text file in the local directory: ")

        # Read only .txt files.
        if not filename.endswith(".txt"):
            print("Only accepting '.txt' files at this time, try again.")
            continue

        # Ensure the file exists before trying to open it.
        if not os.path.exists(filename):
            print(f"{filename} was not found in the local directory, try again.")
            continue

        # Open the file with a context manager so that the file will be closed automatically.
        with open(filename, 'r') as file:
            # List comprehension to add all words found in the file to a list - IF:
                # The word is at least one letter.
                # And the word is all English letters.
            words = [word.strip() for word in file if len(word.strip()) > 0 and word.strip().isalpha()]

        # If there are no words in the word list because none of the provided words were valid,
        # we ask the user to try again.
        if not words:
            print("No valid words found in file.")
            print("Only words containing strictly English letters are supported, try again.")
            continue

        # A word is selected at random by generating a random number
        # from zero to the number of words in the list.
        return words[random.randrange(0, len(words))].upper()
