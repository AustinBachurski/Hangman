import os
import hangman_word_selector as select


class Hangman:
    components: list[str] = ['O', '/', '|', '\\', '-', '/', '\\']
    max_guesses: int = 7

    guessed: list[str] = []
    failed_guesses: int = 0
    unfortunate_soul: list[str] = []
    word: list[str] = []
    target_word: str = ""

    def __init__(self):
        pass

    def game_loop(self):
        letter: str = ''
        while self.failed_guesses < self.max_guesses:

            if not letter:
                letter = input("Take a guess: ").upper()
            else:
                letter = input(f"'{letter}' already guessed, guess again: ").upper()

            while len(letter) != 1:
                letter = input("Please enter a single character: ").upper()

            if letter in self.guessed:
                continue
            else:
                self.guessed.append(letter)

            if not self.in_word(letter):
                self.failed_guesses += 1
                self.update_unfortunate_soul()
            elif self.game_won():
                self.update_screen()
                print(f"{self.target_word} - You got it!")
                return

            self.update_screen()
            letter = ''

        print("Game Over")
        print(f"The word was: {self.target_word}")

    def game_won(self):
        return '_' not in self.word

    def in_word(self, letter: str) -> bool:
        if letter not in self.target_word:
            return False
        else:
            for i, char in enumerate(self.target_word):
                if char == letter:
                    self.word[i] = letter.upper()
            return True

    def init_game(self):
        self.guessed.clear()
        self.failed_guesses = 0
        self.unfortunate_soul = [' '] * self.max_guesses
        self.target_word = self.select_word()
        self.word = ['_'] * len(self.target_word)
        self.update_screen()

    def play(self):
        while True:
            self.init_game()
            self.game_loop()
            while True:
                choice = input("Play again y/n?").lower()
                if choice == 'y':
                    break
                if choice == 'n':
                    return

    @staticmethod
    def select_word() -> str:
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
        while True:
            choice = input("Please enter 1, 2, or 3: ")

            if choice == '1':
                return select.random_word()
            elif choice == '2':
                return select.word_from_file()
            elif choice == '3':
                while True:
                    user_word = input("Enter a word: ").upper()
                    if len(user_word) < 1:
                        print("Can't play without a word...")
                        continue

                    happy = input(f"Use '{user_word}'? (y/n)").lower()
                    if happy == 'y':
                        return user_word

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

    def update_unfortunate_soul(self):
        for i in range(0, self.failed_guesses):
            self.unfortunate_soul[i] = self.components[i]
