'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, get_guessed_word, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def hangman(secret_word):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("welcome to the game, hangman!")
    print("Iam thinking of a word that is:",str(len(secret_word)),"long")
    letters_guessed = []
    guess_chances = 8
    win_flag = 0
    while(guess_chances > 0 and win_flag != 1):
        print("-------------------------------------------------------------------")
        print("you have", str(guess_chances),"left")
        print("available letters:", get_available_letters(letters_guessed))
        guessed_letter = list(input("please enter a letter: "))
        if guessed_letter[0] in letters_guessed:
            print("Oops! you have already guessed that letter :", get_guessed_word(secret_word,letters_guessed))
        else:
            letters_guessed = letters_guessed+guessed_letter
            if is_word_guessed(secret_word,guessed_letter) == True:
                print("good guess_chances", get_guessed_word(secret_word,letters_guessed))
                if secret_word == get_guessed_word(secret_word,letters_guessed):
                    win_flag = 1
            else:
                print("Oops! that letter is  not in my word:", get_guessed_word(secret_word,letters_guessed))
                guess_chances -= 1
    if win_flag ==1:
        print("you won")
    else:
        print("sorry, you ran out of guesses, The word was:"+secret_word)



def is_word_guessed(secret_word, letters_guessed):
    '''
    :param secret_word: string, the word the user is guessing
    :param letters_guessed: list, what letters have been guessed so far
    :return: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    count = 0
    if letters_guessed[count] in secret_word:
        return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    :param secret_word: string, the word the user is guessing
    :param letters_guessed: list, what letters have been guessed so far
    :returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    r_a = []
    temp = '_'
    for char in secret_word:
        if char in letters_guessed:
            r_a.append(char)
        else:
            r_a.append(temp)
    return ''.join(r_a)
import string
def get_available_letters(letters_guessed):
    '''
    :param letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    str2 = ""
    check_str = string.ascii_lowercase
    for i in check_str:
        if i not in letters_guessed:
            str2 += i
    return str2
def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secret_word = chooseWord(wordlist).lower()
    hangman(secret_word)


if __name__ == "__main__":
    main()
