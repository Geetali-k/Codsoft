import random

def get_computer_choice():
    """Generate a random choice for the computer"""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's choice and the computer's choice"""
    if user_choice == computer_choice:
        return 'tie'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    return 'computer'

def play_game():
    """Play a round of Rock, Paper, Scissors"""
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid input. Please enter rock, paper, or scissors: ").lower()
    
    computer_choice = get_computer_choice()
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}\n")
    
    winner = determine_winner(user_choice, computer_choice)
    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("You win!")
    else:
        print("Computer wins!")

def main():
    play_again = 'y'
    while play_again.lower() == 'y':
        play_game()
        play_again = input("\nDo you want to play again? (y/n): ")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()