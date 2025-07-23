"""The main game class for the Hangman game."""

# Importing the external `os` module - used to clear the terminal text.
import os
# Importing the word selector functions, aliased as `select` for ease of use.
import hangman_word_selector as select


# Class containing game logic and state.
class Hangman:
    # Constant member variables - these will not change during program execution.
    components: list[str] = ['O', '/', '|', '\\', '-', '/', '\\']
    max_guesses: int = 7

    # Mutable member variables - these values will change during program execution.
    guessed: list[str] = []
    failed_guesses: int = 0
    unfortunate_soul: list[str] = []
    word: list[str] = []
    target_word: str = ""

    # Boilerplate __init__ method that triggers when class is instantiated.
    # `pass` is used to exit the method without doing anything because all
    # member variables are initialized at their declaration site.
    def __init__(self):
        pass

    # Gameplay loop method.
    def game_loop(self):
        # Initialize letter as an empty string.
        letter: str = ''

        # Game loop - runs until failed guesses matches or exceeds the maximum guesses.
        while self.failed_guesses < self.max_guesses:

            # Correctly prompt the player depending on whether they've guessed or not.
            if not letter:
                letter = input("Take a guess: ").upper()
            else:
                letter = input(f"'{letter}' already guessed, guess again: ").upper()

            # Ensure the player input is a single valid English character.
            while len(letter) != 1 and not letter.isalpha():
                letter = input("Please enter a single English letter character: ").upper()

            # Check if the player has guessed this letter already.
            # If they have, go back to the top of the loop to guess again.
            # If not, add the letter to the guessed list.
            if letter in self.guessed:
                continue
            else:
                self.guessed.append(letter)

            # Check if the letter is part of the secret word.
            # If it is not, increment the failed guesses counter and add a component to the hanged man.
            if not self.in_word(letter):
                self.failed_guesses += 1
                self.update_unfortunate_soul()

            # If the letter is part of the secret word, check if the player has won the game.
            # If they have, update the screen and notify the user of the win condition.
            elif self.game_won():
                self.update_screen()
                print(f"{self.target_word} - You got it!")
                return

            # Depending on how control flows through the game loop, the screen may not have been redrawn yet.
            # So we redraw the screen and set the letter back to an empty string so that input prompts are correct
            # when the game loop continues from the top.
            self.update_screen()
            letter = ''

        # If the game loop exits, it's because the user has exceeded the maximum guess and the
        # hanged man is swinging - inform the player of the loss condition.
        print("Game Over")
        print(f"The word was: {self.target_word}")

    # This method checks for a win condition - if there are no more underscores
    # in the displayed word,  the player has successfully guessed the word.
    def game_won(self) -> bool:
        return '_' not in self.word

    # This method checks if the guessed letter is in the secret word.
    # If it is, it loops through the displayed word and replaces the
    # underscores at the correct index with the letter.
    def in_word(self, letter: str) -> bool:
        if letter not in self.target_word:
            return False
        else:
            # The `enumerate` method generates an incrementing numeric
            # value for every loop iteration (0, 1, 2, ...) - this
            # value is captured in the `i` variable and used to index the word list.
            for i, char in enumerate(self.target_word):
                if char == letter:
                    self.word[i] = letter
            return True

    # This method initializes the game state, it's called at the start of every game.
    def init_game(self):
        self.guessed.clear()  # Clear the guessed word list.
        self.failed_guesses = 0  # Set the failed guesses count to zero.
        self.unfortunate_soul = [' '] * self.max_guesses  # Remove all components of the hanged man.
        self.target_word = self.select_word()  # Set the secret word based on user choice.
        self.word = ['_'] * len(self.target_word)  # Fill the word to be guessed list with underscores.
        self.update_screen()  # Redraw the screen.

    # This method is the entry point for the game, it contains the main loop.
    def play(self):
        # The main loop initializes a new game and plays the game.
        while True:
            self.init_game()
            self.game_loop()

            # When a game finishes, we ask the player if they want to play again.
            # This continues in a loop until the player enters a valid choice - 'y' or 'n'.
            while True:
                choice = input("Play again y/n?").lower()
                if choice == 'y':
                    # If the user wants to play again, we break from the "play again?" loop
                    # and the main loop continues from the top.
                    break
                if choice == 'n':
                    # If the user does not want to play again, we return from
                    # the `play()` method - this terminates the program.
                    return

    # This method displays the welcome message and returns a word to be guessed.
    # The `@staticmethod` annotation is used because the method does not access member data.
    @staticmethod
    def select_word() -> str:
        # Clear the screen and display a welcome message with word selection prompt.
        os.system("cls")
        print(" Welcome to Hangman")
        print("--------------------")
        print()
        print("Press `Ctrl + C` at any time to exit.")
        print()
        print("How do you want to play?")
        print("\t1. Have the game select a random word.")
        print("\t2. Provide a text file of words to be selected at random.")
        print("\t3. Provide your own word.")
        print()

        # Loop until the user makes a valid selection.
        while True:
            choice = input("Please enter 1, 2, or 3: ")

            if choice == '1':
                # Automatically generate a random word.
                return select.random_word()
            elif choice == '2':
                # Allow the user to provide their own list of words via a text file.
                return select.word_from_file()
            elif choice == '3':
                # Allow the user to enter their own word.
                # Loop until the user enters a valid word.
                while True:
                    # Read user input - removing white space and converting to uppercase.
                    user_word = input("Enter a word: ").strip().upper()

                    # If the user doesn't enter a word, ask again.
                    if len(user_word) < 1:
                        print("Can't play without a word...")
                        continue

                    # If the user enters numbers or symbols, ask again.
                    if not user_word.isalpha():
                        print("Only words containing strictly English letters are supported, try again.")
                        continue

                    # Ask the user if they are satisfied with the word they entered.
                    # If so, return the word, if not, the loop continues from the top.
                    happy = input(f"Use '{user_word}'? (y/n)").lower()
                    if happy == 'y':
                        return user_word

    # This method clears and redraws the screen to update the displayed game state.
    def update_screen(self):
        os.system('cls')
        print(f" {' '.join(self.word)}")
        print(f" .----.")
        print(f" |    |")
        print(f" |    {self.unfortunate_soul[0]}")
        print(f" |   {self.unfortunate_soul[1]}{self.unfortunate_soul[2]}{self.unfortunate_soul[3]}")
        print(f" |    {self.unfortunate_soul[4]}")
        print(f" |   {self.unfortunate_soul[5]} {self.unfortunate_soul[6]}")
        print(f" | ")
        print(f" ------------- ")
        print(f" {','.join(self.guessed)}")
        print()

    # This method adds components (body parts) to the hanged man.
    def update_unfortunate_soul(self):
        # We use the failed guesses counter to grab hanged man components from the
        # components list and copy them into the hanged man list.
        for i in range(0, self.failed_guesses):
            self.unfortunate_soul[i] = self.components[i]
