"""Make a Wordle"""

__author__: str = "730642386"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # Establishes state of game and listing variables
    secret_word: str = "codes"
    secret_word_len: int = len(secret_word)
    guess_word: str = ""
    color_emojis: str = ""
    turns: int = 1

    while turns <= 6:
        print(f"=== Turn {turns}/6 ===")
        # Gathers player guess and produces emoji colors from correctness of characters
        guess_word = input_guess(secret_word_len)
        color_emojis = emojified(guess_word, secret_word)
        print(color_emojis)

        # Announces if and when player wins
        if guess_word == secret_word:
            print(f"You won in {turns}/6 turns!")
            turns = 7
        elif guess_word != secret_word and turns < 6:
            turns += 1
        else:
            turns += 1
            print("X/6 - Sorry, try again tomorrow!")


def contains_char(word_with_char: str, char: str) -> bool:
    """Reveals whether word contains correct character"""
    assert len(char) == 1, f"len('{char}') is not 1"
    i: int = 0
    word_len = int(len(word_with_char))

    # Checks for match in word characters
    while i < word_len:
        if word_with_char[i] == char:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Returns emoji color as indicator of correctness of guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    # Defines named constants for emjoi
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji: str = ""
    count: int = 0
    guess_len = int(len(guess))

    # Checks if guess contains specific character
    while count < guess_len:
        if guess[count] == secret[count]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[count]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        count += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Prompts user for guess"""
    proper_guess: str = input(f"Enter a {expected_length} character word: ")
    # Ensures that guess will be the proper length to match the secret word
    while len(proper_guess) != expected_length:
        proper_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return proper_guess


if __name__ == "__main__":
    main(secret="codes")
