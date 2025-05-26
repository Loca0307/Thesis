import random

# List of possible words for the game
words = ['apple', 'banana', 'cherry', 'dragonfruit', 'elderberry', 'fig', 'grapefruit', 'honeydew']

def select_word():
    """Selects a random word from the list of possible words."""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Displays the current state of the word with guessed letters filled in."""
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    print(display)

def make_guess(guessed_letters):
    """Asks the player to guess a letter and adds it to the list of guessed letters."""
    while True:
        guess = input('Guess a letter: ').lower()
        if len(guess) == 1 and guess.isalpha() and guess not in guessed_letters:
            guessed_letters.append(guess)
            return guess
        else:
            print('Please enter a single letter that has not been guessed yet.')

def check_guess(word, guess, guessed_letters):
    """Checks whether the guessed letter is in the word and updates the list of guessed letters."""
    if guess in word:
        print('Correct!')
    else:
        print('Incorrect.')
    display_word(word, guessed_letters)

def play_game():
    """Plays a game of Hangman."""
    word = select_word()
    guessed_letters = []
    guesses_left = 6

    print('Welcome to Hangman!')
    display_word(word, guessed_letters)

    while True:
        guess = make_guess(guessed_letters)
        check_guess(word, guess, guessed_letters)

        if guess not in word:
            guesses_left -= 1
            print(f'You have {guesses_left} guesses left.')
            if guesses_left == 0:
                print(f'Sorry, you lost. The word was "{word}".')
                break

        if set(word).issubset(set(guessed_letters)):
            print(f'Congratulations, you won! The word was "{word}".')
            break

if __name__ == '__main__':
    play_game()