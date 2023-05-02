import random

def play_round():
    player_choice = input("""Enter your choice: rock paper or scissors
    
    """).lower()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chooses {computer_choice}.")

    if player_choice == computer_choice:
        print("It's a tie!")
        return 0, 0
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print("You win this round!")
        return 1, 0
    else:
        print("You lose this round :(")
        return 0, 1

def play_game(rounds):
    player_score = 0
    computer_score = 0
    for i in range(rounds):
        print(f"\nRound {i+1}:")
        p_score, c_score = play_round()
        player_score += p_score
        computer_score += c_score
        print(f"Current score: Player - {player_score}, Computer - {computer_score}")
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("Sorry, you lost the game.")
    else:
        print("The game is tied.")

inf = 0
def play_infinite_game():
    player_score = 0
    computer_score = 0
    while inf < 1:
        print("""New round:""")
        p_score, c_score = play_round()
        player_score += p_score
        computer_score += c_score
        print(f"Current score: Player - {player_score}, Computer - {computer_score}")
        if input("Do you want to play again? (Y/N)").lower() == "n":
            break

# Introduction
print("Welcome to Rock, Paper, Scissors!")
mode = input("Select game mode: 1 - fixed number of rounds, 2 - infinite: ")
if mode == "1":
    rounds = int(input("Enter the number of rounds: "))
    play_game(rounds)
elif mode == "2":
    play_infinite_game()
else:
    print("Invalid mode selected. Please choose either a fixed amount of rounds or infinite.")
