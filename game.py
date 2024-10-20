import random
def main():
# Get Player input

    player_choice = input("Rock, Paper or Scissors?: ")

    while player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":

        print("Please type rock, paper, or scissors: ")
        player_choice = (input("Rock, Paper or Scissors?: ")).lower()


#Generate opponent choice

    computer_choice_generation = random.randint(1,3)

    if computer_choice_generation == 1:
        computer_choice = "rock"
    elif computer_choice_generation == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"


#Check for winner and looser

    if computer_choice == player_choice:
        print("draw!")
        main()
    elif computer_choice == "rock" and player_choice == "paper":
        print("You win!")
    elif computer_choice == "rock" and player_choice == "scissors":
        print("Computer chose rock, you loose :(")
    elif computer_choice == "scissors" and player_choice == "paper":
        print("Computer chose scissors, you loose :(")
    elif computer_choice == "scissors" and player_choice == "rock":
        print("You win!")
    elif computer_choice == "paper" and player_choice == "rock":
        print("Computer chose paper, you loose :(")
    elif computer_choice == "paper" and player_choice == "scissors":
        print("You win!")

    restart_choice = input("Do you want to play again? Please type 'y' to restart or 'n' to end the game and hit enter: ")

    while restart_choice != "y" and restart_choice != "n":
        print("Please type 'y' to restart or 'n' to end the game and hit enter: ")
        restart_choice = input("Do you want to play again? Please type 'y' to restart or 'n' to end the game and hit enter: ")

    if restart_choice == "y":
            main()

if __name__ == '__main__':
    main()