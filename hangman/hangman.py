import random
import os

# Hangman stages
hangman_stages = [
    """
      +---------|
            |   |
        (╥﹏╥)  |
        / | \   |
       /  |  \  |
          |     |
         / \    |
        /   \   |
                |  
        ==========
    """,
    """
      +---------|
            |   |
        (ಠ╭╮ಠ)  |
        / | \   |
       /  |  \  |
          |     |
         / \    |
                |
        ==========
    """,
    """
      +---------|
            |   |
        (ಠ‿ಠ)  |
        / |     |
       /  |     |
          |     |
         /      |
                |
        ==========
    """,
    """
      +---------|
            |   |
        (ಠ‿ಠ)  |
          |     |
          |     |
          |     |
                |
                |
        ==========
    """,
    """
      +---------|
            |   |
        (ಠ‿ಠ)  |
                |
                |
                |
                |
                |
        ==========
    """,
    """
      +---------|
            |   |
                |
                |
                |
                |
                |
                |
        ==========
    """
]

# Reverse the stages so index 0 is the empty hangman
hangman_stages = hangman_stages[::-1]

# Words to guess
words = [    "planet", "bright", "jumbo", "charm", "glove", "dough", "craft", "flame", 
    "spiky", "thorn", "vivid", "block", "jump", "fraud", "quest", "cloud", 
    "bring", "sharp", "cling", "proud", "swift", "pluck", "badge", "march", 
    "vocal", "prize", "dance", "flour", "blank", "grind", "spend", "truck", 
    "fight", "clamp", "shout", "drive", "brisk", "chest", "grape", "mount"]

# Game setup
word_to_guess = random.choice(words)
hidden_word = ["_"] * len(word_to_guess)
remaining_attempts = len(hangman_stages) - 1
guessed_letters = []



# Game loop
while remaining_attempts > 0 and "_" in hidden_word:
    os.system("clear")    
    print("Welcome to Hangman!")
    print(hangman_stages[len(hangman_stages) - 1 - remaining_attempts])
    print("\nWord: ", " ".join(hidden_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Remaining attempts: {remaining_attempts}\n")
    print(word_to_guess,"(debugging)")

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter! Try again.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print(f"Good job! '{guess}' is in the word.\n")
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                hidden_word[i] = guess
    else:
        print(f"Oops! '{guess}' is not in the word.\n")
        remaining_attempts -= 1

# Game over
if "_" not in hidden_word:
    os.system("clear") 
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⢾⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡔⠋⣀⣼⡏⣼⣏⣹⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣶⣿⣿⣿⣡⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡤⢾⣿⣿⣿⣿⣟⠋⣉⣉⠙⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠚⠁⣀⣴⣿⣿⣿⠿⢿⣿⠿⣿⣿⠟⢸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⠔⠚⠛⣇⣀⣠⣴⣿⠿⠋⠹⣿⣤⣾⣿⡦⣽⠇⠀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣤⣶⣿⠋⠀⢸⣿⣿⣿⣾⡟⠋⠉⠁⠀⠀⠀⢹⣿⣿⠛⠛⠂⢀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣴⡟⢹⣿⠇⠀⣠⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣶⣿⣴⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣾⠋⠠⡿⠋⣠⣾⣿⣿⣿⣿⣡⣤⣤⣄⡤⣊⣭⣿⣿⣿⣮⣍⣿⡿⠛⠉⢀⣸⣧⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀
⢻⣷⡆⠀⠀⣈⠁⠀⠴⠿⠿⠿⠿⣿⢿⣿⣿⣿⡿⠛⠛⠛⢿⣿⣿⣷⠴⣾⣿⣿⣿⣷⣦⡄⠑⢤⡀⠀⠀⠀⠀
⠈⠻⣿⣿⣿⣿⣿⣗⣀⣠⣤⣤⡀⠀⢀⣿⣿⣯⣀⣠⡆⠀⠈⢿⠋⠀⠾⠿⠿⠿⣿⣿⣿⣿⣶⣾⡿⠳⡀⠀⠀
⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣶⣤⣼⠀⢰⠀⠀⠀⠉⢁⡀⠀⠘⣿⡿⣁⠴⢳⣄⠀
⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⡦⢬⡛⠻⠿⣿⣿⣿⡄⢾⣶⣶⣾⣯⣿⡆⠀⠀⡉⠁⠹⣷⣿⢿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⡇⢸⣷⣄⣀⣠⣼⣿⠃⣰⣿⣿⣿⣿⣿⣷⡀⢠⣇⠀⢰⣿⣿⣌⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣧⣾⣿⣿⣿⣿⣿⡿⡄⢻⣿⣿⣿⡉⢻⣿⣷⣸⣿⢠⡟⠀⠙⢿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⡿⢀⣷⢸⣿⣿⣿⣷⣾⣿⣿⣿⣿⡿⠀⣤⠀⠘⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠟⣠⣾⣇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣾⣿⠀⠀⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣏⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⡴⢀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠙⠒⠒⠛⠿⢿⣿⣿⣿⣿⣟⡛⠛⠿⠿⣿⣿⣿⣿⣿⡿⣡⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⣶⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⠟⢿⣿⣿⣿⠟⢻⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣴⣼⣿⣿⣿⠀⣋⣿⠀⠀

    """)
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    os.system("clear") 
    print(hangman_stages[0])
    print("""

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠊⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠖⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣵⣇⣠⠂⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠣⡋⠛⠛⠗⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣌⢉⡀⠀⠑⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢏⠜⠀⣠⡇⡀⠰⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⡆⠀⣰⣿⣾⡇⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⠄⢀⣼⣿⣿⣿⣧⣾⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⢁⠄⢀⣼⣿⣿⣿⣿⣿⣷⢰⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠡⠄⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣄⡆⠀⠙⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⢳⠖⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⣴⠀⠙⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠃⠖⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣠⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡏⠞⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣠⠀⠹⣿⣿⣿⣿
⣿⣿⣿⣿⠡⠆⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡀⠀⢻⣿⣿⣿
⣿⣿⣿⣿⠔⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⢸⣿⣿⣿
⣿⣿⣿⣿⠖⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠚⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣠⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠖⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣧⡄⠀⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠱⠂⠀⣾⣿⣿⣿
⣿⣿⣿⣿⣿⣧⡆⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢛⡴⠛⢀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⣼⡀⡄⠈⠉⠻⠿⠿⠿⠿⢟⣛⡉⠴⠋⢁⣰⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣌⣢⡐⠄⠐⠤⠕⠒⠈⣉⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣾⣿⣿⣯⣿⣿⣽⣿⣟⣷⣾⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

            """)

    print("You lost! The word was:", word_to_guess)

