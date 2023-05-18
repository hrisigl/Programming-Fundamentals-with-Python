import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, [p]aper, [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

comp_random_num = random.randint(1, 3)
computer_move = ""


if comp_random_num == 1:
    computer_move = rock
elif comp_random_num == 2:
    computer_move = paper
else:
    computer_move = scissors

print(f"The computer chose: {computer_move}")

if (computer_move == rock and
    player_move == paper) or (computer_move == paper and
                              player_move == scissors) or (computer_move == scissors and player_move == rock):
    print("You win!")
elif computer_move == player_move:
    print("Draw")
else:
    print("You lose!")
