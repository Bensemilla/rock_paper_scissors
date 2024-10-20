player_choice = input("Rock, Paper or Scissors?: ")

while player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":

    print("Please type rock, paper, or scissors: ")
    player_choice = (input("Rock, Paper or Scissors?: ")).lower()
    
    

print(player_choice)