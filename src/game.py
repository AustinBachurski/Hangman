"""Terminal clone of the classic Hangman word guess game."""

# Importing the game class.
from hangman import Hangman

# __name__ boilerplate – prevents the program from being ran if this file is imported.
if __name__ == "__main__":
    # Instantiate a game object.
    game = Hangman()

    # Play the game.
    game.play()
