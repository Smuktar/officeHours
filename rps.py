# create a rock, paper, scissor game
import random
from colorama import init, Fore

init(autoreset= True)
# 3 options to choose from
choices = ["rock", "paper", "scissors"]
player_score = 0
computer_score = 0

while True:
    # add a score
    print(f"Your score: {player_score} | Computer: {computer_score} \n")

    print("\nWelcome to Rock, Paper, Scissors")

    # need to be able to take a users input so they can select
    player = input("\nChoose either rock, paper, or scissors (or quit):").lower()

    if player == "quit":
        print("Thanks for playing!")
        print("Final score")
        print(f"Your score: {player_score} | Computer: {computer_score} \n")
        break
    if player not in choices:
        print("That is not an option. Please choose either rock, paper, or scissor \n")
        continue

    # need to give random choice to computer
    computer = random.choice(choices)
    print("Your opponent chooses: ", computer)

    # create what to do depending on different outcomes
    if player == computer:
        print(Fore.YELLOW+ "Oh - It's a tie!")
    elif player == 'rock' and computer == 'scissors':
        print(Fore.GREEN+ "\nYou Win Rockstar!")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print(Fore.GREEN+"You are really cutting down your opponents! You Win!!! ")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print(Fore.GREEN+ "You Win!!!")
        player_score += 1
    else:
        print(Fore.RED+ "haha - You Lose! Better luck next time!")
        computer_score += 1
