"""EX02 -  Wordle."""

__author__ = "730554167"

secret = str("python")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess = input(str("What is your " + str(len(secret)) + "-letter guess? "))

x = 0
result = ""

while len(guess) != len(secret): 
    guess = input("That was not " + str(len(secret)) + " letters! Try again: ")

while x < len(guess): 
    if guess[x] == secret[x]: 
        result = result + GREEN_BOX
    else:
        exists = False
        counter = 0
        while exists is False and counter < len(secret):
            if guess[x] == secret[counter]:
                exists = True
            counter += 1
        if exists is True:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX  
    x += 1
print(result) 

if guess == secret: 
    print("Woo! You got it!")
else: 
    print("Not quite. Play again soon!")