"""
mymodule.py

"""
import random


choice_list = ['Rock', 'Paper', 'Scissors']


def make_choice():
    """Return either Rock, Paper or Scissors randomly."""
    choice = random.choice(choice_list)
    return choice

################### Below functions are for excersise #######################

def get_user_choice():
    """Get a choice from a user input"""
    while True:
        user_choice = input('Rock, Paper, Scissors:').strip()
        if user_choice not in choice_list:
            print(user_choice, 'is not a valid choice, pick from:', choice_list)
        else:
            print('You chose:', user_choice)
            break
    return user_choice


# Complete this function!
def determine_winner(player_choice, computer_choice):
    """Determine if player or cpu won the game"""
    #
    #
    #
    #
    return


def play_game():
    """Play a game of rock, paper, scissors"""
    user_choice = get_user_choice()
    cpu_choice = make_choice()
    print('Computer chose:', cpu_choice)
    determine_winner(user_choice, cpu_choice)

