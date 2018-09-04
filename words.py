# My imported componants
import random
import os

win = False
wordBank = ['APPLE', 'PINEAPPLE', 'BANANA', 'PEAR', 'ORANGE', 'TOMATO', 'KIWI', 'PEACHE']
wordSelected = ""
lettersGuessed = []
guessesWrong = 0
guessesCorrect = 0
win = False
again = 'Y'

def initialize():
    global win
    global wordSelected
    global lettersGuessed
    global guessesWrong
    global guessesCorrect
    global win
    global again
    win = False
    wordSelected = ""
    lettersGuessed = []
    guessesWrong = 0
    guessesCorrect = 0
    win = False
    again = 'Y'

def printWord(word):
    for letter in word:
        if letter in lettersGuessed:
            print(letter, end=" ")
        else:
            print("_ ", end="")
    print(" ")

def drawMan() :
    if guessesWrong == 0:
        print("")
    else:
        print("")
    if guessesWrong >= 1:
        print(" O ")
    else:
        print("")
    if guessesWrong >= 2:
        print("/|\\")
    else:
        print("")
    if guessesWrong >= 3:
        print(" | ")
    else:
        print("")
    if guessesWrong >= 4:
        print("/ \\")
    else:
        print("")
    if guessesWrong == 5:
        print("You hangged your dude!")
    else:
        print("")
    print("")

def drawManWin() :
    print("")
    print(" O ")
    print("\|/")
    print(" | ")
    print("/ \\")
    print("")

def takeInput(word):
    global guessesWrong
    global guessesCorrect
    repeat = True
    while repeat == True:
        guess = input("Please, enter a letter as a guess:  ")
        guess= guess.upper()
        if guess in lettersGuessed:
            repeat = True
        else:
            repeat = False
    if guess not in word:
        guessesWrong += 1
    else:
        i = wordSelected.count(guess)
        guessesCorrect += i
    lettersGuessed.append(guess)
    return guessesCorrect

### MAIN ###
while again == 'Y' or again == 'y' :
    initialize()
    os.system('clear')
    print("!!! WELCOME TO PYTHON HANGMAN !!!")
    print("")
    print("i will select a word. You guess letters until you've spelled the word out.")
    print("You can make 5 wrong guesses before your dude is hangged.")
    print("If you enter any invalid characters (e.g. ! or >) those will count against your guesses.")
    print("")
    input("Are you ready to play? Press any key to continue.")
    wordSelected = random.choice(wordBank)
    while guessesWrong <= 4 and win == False:
        os.system('clear')
        drawMan()
        printWord(wordSelected)
        print(lettersGuessed)
        print(guessesCorrect, " / ", len(wordSelected))
        takeInput(wordSelected)
        if guessesCorrect == len(wordSelected):
            win = True
    if win == True:
        os.system('clear')
        drawManWin()
        printWord(wordSelected)
        print("")
        print("!!! YOU SAVED YOUR DUDE !!!")
    else:
        os.system('clear')
        drawMan()
    again = input("Do you want to play again (y/n)?  ")
print("Ciao")