import random

def guessing_game():
    print("====================================")
    print("🎯 Welcome to the Number Guessing Game! 🎯")
    print("I'm thinking of a number between 1 and 100.")
    print("====================================")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! 📉 Try again.")
            elif guess > secret_number:
                print("Too high! 📈 Try again.")
            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                break
                
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")


guessing_game()