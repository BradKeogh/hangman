#### Hangman functions

# import dependances
from utils import check_letter_in_word, get_user_input, choose_random_word
from words_NO_PEAKING import words_list


class game(object):
    """class starts game when initialised and continues game until completed.
    """
    
    def __init__(self):
        #### init variables
        self._word = choose_random_word(words_list) # gets random word
        self._guesses_remain = 5
        self._guessed_letters_incor = []
        self._guessed_letters_cor = []
        self._word_status = len(self._word) * ' _' # setup word status
        #### print initial status
        self.status()
        # while loop makes game continue automatically
        self._start_guessing()
        #### print Win/Lose Message
        self._win_lose_message()
        
        return
    
    def status(self):
        """prints the status of game: the word and the hangman."""
        print('')
        print('Number of guesses remaining: ', self._guesses_remain)
        print('-'*40)
        print(self._word_status)
        print('-'*40)
        return True
    
    def make_guess(self):
        """requests user input,checks for guess."""
        #### take letter and change values based on guess
        Uinput = get_user_input() # change for function
        if check_letter_in_word(self._word,Uinput): #check in word
            self._guessed_letters_cor.append(Uinput)
            print('Good guess love!')
            # reveal letters
        else:
            self._guessed_letters_incor.append(Uinput)
            self._guesses_remain -= 1
            print('Sorry, bad guess :-(')
        
        #### display current status 
        self._word_status = self._reveal_letters()
        self.status()
        return True
    
    def _reveal_letters(self):
        """return string with letters revealed or blank based on current guesses"""
        word_updated = ''
        for char in self._word:
            word_updated += ' '
            if char in self._guessed_letters_cor:
                word_updated += char
            else: word_updated += '_'
        
        return word_updated
            
    def _win_lose_message(self):
        "prints win/lose message when called"
        print('call to win_lose')
        if (set(self._word) == set(self._guessed_letters_cor)):
            print("Congratulations! You've Won! :D ;D")
        else:
            print("YOU'VE LOST! Try again next time ;-(")
        return
            
    def _start_guessing(self):
        "begins while loop which continues guessing until either run out of guesses or all characters guessed correctly."
        while (self._guesses_remain > 0) & (set(self._word) != set(self._guessed_letters_cor)):
            self.make_guess()
        return True