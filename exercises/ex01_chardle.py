"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730554167"

guess = input(str("Enter a 5-character word: "))
if len(guess) != 5: 
    print("Error: Word must contain 5 characters")
    exit()
character = input(str("Enter a single character: "))
if len(character) != 1: 
    print("Error: Character must be a single character.")
    exit()
    print("Character must be a single character.")
print("Searching for " + character + " in " + guess + ".")

instances = 0

if guess[0] == character:
    print(character + " found at index 0")
    instances = instances + 1 
if guess[1] == character:
    print(character + " found at index 1")
    instances = instances + 1 
if guess[2] == character:
    print(character + " found at index 2")
    instances = instances + 1 
if guess[3] == character:
    print(character + " found at index 3")
    instances = instances + 1 
if guess[4] == character:
    print(character + " found at index 4")
    instances = instances + 1 

if instances == 0:
    print("No instances of " + character + " found in " + guess)
elif instances == 1:
    print("1 instance of " + character + " found in " + guess)
elif instances == 2:
    print("2 instances of " + character + " found in " + guess)
elif instances == 3:
    print("3 instances of " + character + " found in " + guess)
elif instances == 4:
    print("4 instances of " + character + " found in " + guess)
else:
    print("5 instances of " + character + " found in " + guess)

    