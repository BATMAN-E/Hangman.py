
import random

HANGMAN_ART = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]


def display_game(word, guessed_letters, attempts):

    print("\n" + "=" * 35)
    print("          HANGMAN GAME")
    print("=" * 35)

    print(HANGMAN_ART[6 - attempts])

    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in word
    )

    print("Word:", display_word)
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    print("Attempts remaining:", attempts)


def load_words():

    with open("new_words.txt", "r") as file:
        words = [
            line.strip().lower()
            for line in file
            if line.strip().isalpha()
        ]

    if not words:
        raise ValueError("No valid words found in new_words.txt")

    return words


def hangman():

    word_list = load_words()
    word = random.choice(word_list)

    guessed_letters = set()
    attempts = 6

    print("\nWelcome to Hangman!")
    print("You have", attempts, "attempts to guess the word.")

    while attempts > 0:

        display_game(word, guessed_letters, attempts)

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You've guessed the word:", word)
            print("YOU WIN!")
            break

        guess = input("\nGuess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess.")
            attempts -= 1

    else:
        print("\n" + "=" * 35)
        print("             GAME OVER")
        print("=" * 35)
        print(HANGMAN_ART[6])
        print("Sorry, you've run out of attempts.")
        print("The correct word was:", word)


if __name__ == "__main__":
    hangman()
