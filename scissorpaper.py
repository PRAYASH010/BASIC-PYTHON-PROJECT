import random

choices = ["scissor", "paper", "rock"]

while True:
    computer_choice = random.choice(choices)
    player_choice = input("\nEnter your choice (Rock, Paper, Scissor): ").strip().lower()

    if player_choice not in choices:
        print("Invalid choice! Please choose Rock, Paper, or Scissor.")
        continue

    print(f"Computer choice is: {computer_choice.capitalize()}")
    print(f"Your choice is: {player_choice.capitalize()}")
    print("-" * 30)

    if computer_choice == player_choice:
        print("The match is a Draw!")
    elif (computer_choice == 'rock' and player_choice == 'scissor') or \
         (computer_choice == 'paper' and player_choice == 'rock') or \
         (computer_choice == 'scissor' and player_choice == 'paper'):
        print("Computer is the winner!")
    else:
        print("You win! 🎉")
        
    print("-" * 30)
    
    rematch = input("Do you want to play again? (yes/no): ").strip().lower()
    
    if rematch in ['no', 'n']:
        print("\nThanks for playing! Goodbye! 👋")
        break