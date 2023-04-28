import random
#this says hello
print("Hello and welcome to rock paper scissors, you will play against an AI, choose either Rock Paper or Scissors.")
player_score = 0
computer_score = 0
j = 0
#this is the loop
amountofrounds = int(input("How many rounds would you like to play?"))
for i in range(amountofrounds):
    player_choice = input("Enter your choice: ").lower()

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

 
    if player_choice == computer_choice:
        print("It's a draw...")
    elif player_choice == 'rock' and computer_choice == 'scissors':
        print("You win this round! Rock beats scissors.")
        player_score += 1
    elif player_choice == 'paper' and computer_choice == 'rock':
        print("You win this round! Paper beats rock.")
        player_score += 1
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print("You win this round! Scissors beat paper.")
        player_score += 1
    elif player_choice == "quit" or "q":
        print("thanks for playing!")
        break
    elif player_choice == 'rock' and computer_choice == 'paper':
        print("you lose this round")
        computer_score += 1
    elif player_choice == 'paper' and computer_choice == 'scissors':
        print("you lose this round")
        computer_score += 1
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print("you lose this round")
        computer_score += 1
    else:
        print("You lose this round.")
        computer_score += 1


    print(f"Your score: {player_score} | Computer score: {computer_score}")

    if player_score == amountofrounds:
        print("Congratulations, you won!")
        break
    elif computer_score == amountofrounds:
        print("Sorry, you lost.")
        break