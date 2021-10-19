"""
mymodule.py

"""
import random


choice_list = ['Rock', 'Paper', 'Scissors']


def make_choice():
    """Return either Rock, Paper or Scissors randomly."""
    choice = random.choice(choice_list)
    return choice


################### Below functions are for exercises #######################


"""
Complete the function below to print the winner to the screen.

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

"""


def determine_winner(player_choice, computer_choice):
    """Determine if player or cpu won the game"""
    #
    #
    #
    #
    #
    print('Winner cannot be determined (task not completed!)')  # delete this line
    
    
def get_player_choice():
    """Get a choice from a user input"""
    while True:
        player_choice = input('Chose Rock, Paper or Scissors:').strip()
        if player_choice not in choice_list:
            print(player_choice, 'is not a valid choice, pick from:', choice_list)
        else:
            print('\nYou chose:', player_choice)
            break
    return player_choice


def play_game():
    """Play a game of rock, paper, scissors"""
    print('Rock, Paper, Scissors Game!')
    print('-' * 27, '\n')
    user_choice = get_player_choice()
    cpu_choice = make_choice()
    print('Computer chose:', cpu_choice, '\n')
    determine_winner(user_choice, cpu_choice)

