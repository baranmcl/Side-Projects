# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/mbaron/Desktop/GitHub/Side Projects/Python Hangman/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    secretWordLetters = [str(i) for i in secretWord]
    for i in secretWordLetters:
        if i not in lettersGuessed: return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guessedWord = ""
    secretWordLetters = [str(i) for i in secretWord]
    for i in secretWordLetters:
        if i not in lettersGuessed:
            guessedWord += "_ "
        else:
            guessedWord += "%s" %(i)
    return guessedWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    availableLetters = ""
    for i in string.ascii_lowercase:
        if i not in lettersGuessed:
            availableLetters += "%s" %(i) 
    return availableLetters
    

def hangman(secretWord):
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
    import string
    lettersGuessed = []
    guessCounter = 8
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %s letters long." %(len(secretWord))
    print "-------------"
    while isWordGuessed(secretWord, lettersGuessed) == False:
        print "You have %s guesses left." %(guessCounter)
        print "Available letters: " + str(getAvailableLetters(lettersGuessed))
        guess = raw_input("Please guess a letter: ", )
        lowercaseGuess = guess.lower()
        if lowercaseGuess in lettersGuessed:
            print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed))
        elif (lowercaseGuess not in string.ascii_lowercase) or (len(lowercaseGuess) >= 2) or (len(lowercaseGuess) < 1):
            print "Sorry, I didn't understand that. Guess again"
        elif lowercaseGuess in secretWord:
            lettersGuessed.append(lowercaseGuess)
            print "Good guess: " + str(getGuessedWord(secretWord, lettersGuessed))
        else:
            guessCounter -= 1
            lettersGuessed.append(lowercaseGuess)
            print "Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed))
        print "-------------"
        if isWordGuessed(secretWord, lettersGuessed) == True: 
            print "Congratulations, you won!"
        elif guessCounter <= 0: 
            print "Sorry, you ran out of guesses. The word was " + str(secretWord)
            break

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
