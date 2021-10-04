"""
mymodule.py

"""
import random


choice_list = ['Rock', 'Paper', 'Scissors']


def make_choice():
    """Return either Rock, Paper or Scissors randomly."""
    choice = random.choice(choice_list)
    return choice
    