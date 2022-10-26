"""EX06."""

__author__ = "730554167"

from random import randint

points: int = 0 
player: str = "" 
num: int = 0
# Globals 

Grinning_Face: str = "\U0001f600"
Squinting_Face: str = "\U0001f600"
Laughing_face: str = "\U0001F923"
# Emojis that will be used at the end of the program


def main() -> None:
    """Main function of the program."""
    print(greet())

    Go_Forward = input(f" Hi {player}! Would you like to continue the game, get free points or exit? Enter Continue, Free or Exit to proceed (ᵔᴥᵔ) ")
    while Go_Forward != "Continue" and Go_Forward != "Exit" and Go_Forward != "Free":
        Go_Forward = input("Please enter Continue, Free or Exit to proceed (ᵔᴥᵔ) ")

    if Go_Forward == ("Continue"):
        print(dino())
    if Go_Forward == ("Exit"):
        print("Sorry to see you go!")
        quit()
    if Go_Forward == ("Free"):
        free = input(f"{player}, choose a random number 0 - 10. ")
        while int(free) > 10:
            free = input(f"{player}, choose a random number between 0 - 10. ")
        print(Free_Points(free))
        print(dino())
    return None 
# Main function runs program and offers choices on how to continue


def dino() -> None:
    """Outputs what Dinosaur you are!"""
    global points

    color = input("Do you prefer Davis or the UL? ")

    while color != "Davis" and color != "UL":
        color = input("Do you prefer Davis or the UL? ")
    if color == "Davis":
        points = points + 10
        print(f"You have {points} points")
    if color == "UL":
        points = points + 5
        print(f"You have {points} points")

    size = input("Do you enjoy Summer or Winter more? ")
    if size == "Summer":
        points = points + 10
        print(f"You have {points} points")
    if size == "Winter":
        points = points + 5
        print(f"You have {points} points")
    if points <= 15:
        print(f"Congrats! You're a Triceritops {Grinning_Face}.")
    elif points < 30:
        print(f"Congrats! You're a T-Rex {Squinting_Face}.")
    else:
        print(f"Congrats! You're a Spinosaurus {Laughing_face}.")
# dinosaur program tell the player what Dinosaur their are based on the number of points they had


def Free_Points(free: int) -> int: 
    """Gives the player free points."""
    global points
    points = int(free) + randint(1, 10)
    print(f"You have {points} points")
# free points function gives the player a boost in the game!


def greet() -> None:
    """Greets the player!"""
    global player
    print("Welcome to What_Dinosaur_are_You!")
    player = input("What is your name? ")
# greets function greets the player and asks for their name


if __name__ == "__main__":
    main()