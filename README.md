# Hangman Game – Python

A classic command-line Hangman game built with Python. The game randomly selects a word from an external text file, and players must guess the hidden word before running out of attempts.

## Features

- **Random Word Selection:** Words are loaded from an external `new_words.txt` file.
- **ASCII Gallows Art:** Visual hangman stages update after every incorrect guess.
- **Limited Attempts:** Players get 6 incorrect guesses.
- **Input Validation:** Prevents invalid inputs and repeated guesses.
- **Victory & Defeat Screens:** Displays the result and reveals the correct word when the player loses.
- **Lightweight:** Uses Python's built-in modules. No external dependencies required.

## Project Structure

```text
Hangman/
│
├── hangman.py
├── new_words.txt
└── README.md
```

## Requirements

- Python 3.8 or higher
- A terminal or command-line interface

No additional Python packages are required.

## Installation & Setup

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd Hangman
```

**3. Prepare the word list**

Make sure `new_words.txt` exists in the project directory.

Add words to the file, with one word per line:

```text
python
computer
programming
developer
keyboard
algorithm
database
software
```

**4. Run the game**

```bash
python hangman.py
```

On some systems, you may need:

```bash
python3 hangman.py
```

## How to Play

1. Run the game using the command above.
2. The game randomly selects a hidden word.
3. Enter one letter at a time to guess the word.
4. Correct guesses reveal the matching letters.
5. Incorrect guesses add a part to the hangman drawing.
6. Guess the entire word before using all 6 attempts to win.

## Game Rules

- You have 6 incorrect guesses.
- Only one alphabetic character is accepted per guess.
- Repeated guesses are not counted as additional attempts.
- Guess all letters correctly to win.
- If you run out of attempts, the game ends and reveals the word.

## Technologies Used

- **Python**
- `random` module
- File Handling (`open()`)
- Lists and Sets
- Functions
- Loops and Conditional Statements
- ASCII Art

## Future Improvements

- Add difficulty levels (Easy, Medium, Hard).
- Add a play-again option.
- Implement a scoring system.
- Prevent consecutive word repetition.
- Add categorized word lists.

## Author

Developed as a Python programming project to practice fundamental programming concepts, file handling, and game logic.

---

**Enjoy playing Hangman!**
