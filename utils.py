#### utils for hangman game
import numpy as np

def check_letter_in_word(word,letter):
    "checks if letter in word string"
    if letter in word:
        return True
    else:
        return False
    
def get_user_input():
    """demands user input and returns string of size 1.
    Correspond sto the first letter"""
    user_input = input("Please enter a letter: ")
    return user_input.lower()[0]

def choose_random_word(word_list):
    "return randomly select a word from a list of words"
    randint = np.random.randint(0,len(word_list))
    return word_list[randint]