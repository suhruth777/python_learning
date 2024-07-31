# Make a two-player Rock-Paper-Scissors game. 


while True:
    player_one = input("Player 1 - Rock, Paper, Scissors?: ")
    player_two = input("Player 2 - Rock, Paper, Scissors?: ")
    if player_one == 'rock' and player_two == "scissors":
        print("Rock beats Scissors! Player 1 Wins!!")
    elif player_one == 'paper' and player_two == "rock":
        print("Paper beats Rock! Player 1 Wins!!")
    elif player_one == 'scissors' and player_two == "paper":
        print("Scissors beats Paper! Player 1 Wins!!")
    elif player_two == 'rock' and player_one == "scissors":
        print("Rock beats Scissors! Player 2 Wins!!")
    elif player_two == 'paper' and player_one == "rock":
        print("Paper beats Rock! Player 2 Wins!!")
    elif player_two == 'scissors' and player_one == "paper":
        print("Scissors beats Paper! Player 2 Wins!!")
    elif player_two == player_one:
        print('You tied! Go again!')
  