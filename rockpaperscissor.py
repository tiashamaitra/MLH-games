import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Let's play Rock, Paper, Scissors!")

    while True:
        print("\nMenu:")
        print("1. Play a round")
        print("2. Quit")
        
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()

            print(f"You chose {user_choice}.")
            print(f"Computer chose {computer_choice}.")

            result = determine_winner(user_choice, computer_choice)
            print(result)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Run the game
play_game()
