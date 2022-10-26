"""EX03 -  Wordle."""

__author__ = "730554167"


def contains_char(word: str, character: str) -> bool:
    """Returns true or false if the character is present or not."""
    assert len(character) == 1
    counter = 0
    correct = False
    while correct is False and counter < len(word):
        if word[counter] == character:
            correct = True
            return correct
        else: 
            counter += 1 
    return correct


# Completes the contains_char function 
def emojified(guess: str, secret: str) -> str: 
    """Creates emoji line."""
    assert len(guess) == len(secret)
    
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    x = 0
    boxes: str = ""
    exists = False
    while x < len(guess): 
        if guess[x] == secret[x]: 
            boxes += GREEN_BOX
        else:
            exists = contains_char(secret, guess[x])
            if exists is True:
                boxes += YELLOW_BOX
            else:
                boxes += WHITE_BOX
        x += 1
    return (boxes)


# Completes the emojifed function
def input_guess(char: int) -> str:
    """Limits a word to the inputed characters."""
    num = input("Enter a " + str(char) + " character word: ")
    while len(num) != char: 
        num = input("That wasn't " + str(char) + " chars! Try again: ")
    return (num)


# Completes the input_guess function
def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns = 0 
    secret = "codes"
    while turns <= 5:
        turns += 1 
        print("=== Turn " + str(turns) + "/6 ===")
        value = input_guess(5)
        attempt = emojified(value, secret)
        print(attempt)
        if value == secret: 
            print("You won in " + str(turns) + "/6 turns!")
            return
    if turns > 5: 
        print("X/6 - Sorry, try again tomorrow!")
        return


# Completes the main() function
if __name__ == "__main__":
    main()