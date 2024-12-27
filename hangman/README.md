Hangman Game 🎮

This is a Python implementation of the classic Hangman game. Players try to guess a hidden word by suggesting letters one at a time. The game features ASCII art for different stages of the hangman and provides a fun and interactive terminal-based experience.
Features

    Random Word Selection: A word is randomly selected from a predefined list of words.
    ASCII Art: Visual hangman stages depict progress and attempts left.
    Interactive Gameplay: Allows user input for guessing letters.
    Feedback on Progress: Displays guessed letters, remaining attempts, and current state of the word.
    Win/Loss Screens: Celebratory or consoling ASCII art for game results.
    Debug Mode: Displays the word being guessed for testing purposes (optional; can be removed).

Requirements

    Python 3.x
    Operating system that supports os.system("clear") for terminal clearing (e.g., Linux, macOS). Replace clear with cls for Windows if needed.

How to Run

    Clone the repository:

git clone https://github.com/ghostasguest/hangman-game.git
cd hangman-game

Run the game:

    python hangman.py

    Follow the on-screen instructions to play the game!

How to Play

    A random word will be selected for you to guess.
    The word will be represented by underscores (_) indicating unguessed letters.
    Enter one letter at a time to guess the word.
    If the guessed letter is in the word, it will replace the corresponding underscore(s).
    Incorrect guesses will reduce your attempts and progress the hangman drawing.
    The game ends when:
        You correctly guess the entire word (You win 🎉).
        You run out of attempts (You lose ☹️).

Customization

    Words List: You can modify the list of words by editing the words array in the script.
    Hangman Art: Customize the ASCII art for each stage in the hangman_stages list.

Example Gameplay

Welcome to Hangman!

      +---------|
            |   |
        (ಠ‿ಠ)  |
          |     |
          |     |
          |     |
                |
                |
        ==========

Word:  _ _ _ _ _
Guessed letters: a, e
Remaining attempts: 4

Enter a letter:

Debugging

    A debugging feature is included to display the word being guessed (print(word_to_guess, "(debugging)")). Comment or remove this line when deploying the final version.

Screenshots
Winning Screen

Congratulations! You guessed the word: planet
<celebratory ASCII art>

Losing Screen

You lost! The word was: bright
<sad ASCII art>

Contributions

Contributions, bug reports, and suggestions are welcome! Feel free to open an issue or submit a pull request.
License

This project is licensed under the MIT License. See the LICENSE file for details.
