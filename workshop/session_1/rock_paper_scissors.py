"""
rock_paper_scissors.py
"""
import random

choice_list = ['Rock', 'Paper', 'Scissors']

# Function to get a random choice from the computer
def get_cpu_choice():
    choice = random.choice(choice_list)  # Randomly select 'Rock', 'Paper', or 'Scissors'
    return choice

# Function to get the player's choice
def get_player_choice():
    while True:
        # Prompt player to enter their choice, removing any leading/trailing whitespace
        player_choice = input('Chose Rock, Paper or Scissors:').strip()
        # Check if the choice is valid
        if player_choice not in choice_list:
            print(player_choice, 'is not a valid choice, pick from:', choice_list)
        else:
            print('\nYou chose:', player_choice)
            break  # Exit the loop once a valid choice is made
    return player_choice

def determine_winner(player_choice, computer_choice):
    # Complete the function to print the winner to the screen and determine whether player or CPU wins the game
    print()

# Main function to play the game
def play_game():
    print('Rock, Paper, Scissors Game!')
    print('-' * 27, '\n')
    # Get choices from both player and computer
    user_choice = get_player_choice()
    cpu_choice = get_cpu_choice()
    print('Computer chose:', cpu_choice, '\n')  # Display the computer's choice
    determine_winner(user_choice, cpu_choice)  # Determine and display the winner

play_game()

"""
After completing the function, try running this file in Terminal using `python3 PythonWorkshop/workshop/session_1/rock_paper_scissors.py`
"""