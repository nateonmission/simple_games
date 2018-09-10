# My imported componants
import random
import time
import os
# This is a comment
# My global variables
possibleMoves = ['a',  'c', 'g', 'i', 'b', 'd', 'e', 'f', 'h']
playerNames = []
compPlayer = False
playerFunction = []
prompt = ""
boxes = {}
xWin = False
oWin = False
winner = False
counter = 1
again = 'y'
movesMade = []


# Resets the variables to play again
def initialize():
    global boxes, xWin, yWin, winner, counter, again, movesMade, playerNames, compPlayer, playerFunction
    playerNames = []
    compPlayer = False
    playerFunction = []
    prompt = ""
    boxes = {
        'a': ' ',
        'b': ' ',
        'c': ' ',
        'd': ' ',
        'e': ' ',
        'f': ' ',
        'g': ' ',
        'h': ' ',
        'i': ' '
    }
    xWin = False
    oWin = False
    winner = False
    counter = 1
    again = 'y'
    movesMade[:] = []


# Instructions and game setup
def intro():
    os.system('clear')
    global playerNames, compPlayer, playerFunction
    repeatNum = True
    repeatOrd = True
    print("Hello! Welcome to Tic-Tac-Toe!\n")
    print("Two humans can play against each other or one human can play against the Computer.\n")
    while repeatNum == True:
        humNum = input("How many humans want to play? (1 or 2): ")
        humNum = int(humNum)
        if humNum == 2:
            for player in range(0, 2):
                print("Player 1 will be Xs and Player 2 will be Os.")
                name = input("What is the name of player {num}?: ".format(num=player + 1))
                playerNames.append(name)
            compPlayer = False
            playerFunction.append(1)
            playerFunction.append(1)
            repeatNum = False
        elif humNum == 1:
            while repeatOrd == True:
                order = input("Do you want to be Xs (and go first) or Os (and go second)? (x/o): ")
                if order == 'o':
                    playerFunction.append(0)
                    playerFunction.append(1)
                    name = input("What is your name?: ")
                    playerNames.append("Computer")
                    playerNames.append(name)
                    compPlayer = True
                    repeatOrd = False
                    repeatNum = False
                elif order == 'x':
                    playerFunction.append(1)
                    playerFunction.append(0)
                    name = input("What is your name?: ")
                    playerNames.append(name)
                    playerNames.append("Computer")
                    compPlayer = True
                    repeatOrd = False
                    repeatNum = False
                else:
                    print("Uh, I do not understand...")
                    repeatOrd = True
            repeatNum == False
        else:
            print("Uh, I do not understand...")
            repeatNum = True


# The actual game execution
def gameplay():
    os.system('clear')
    printboard()
    global counter, playerFunction, playerNames
    if counter % 2 == 0:
        if playerFunction[1] == 1:
            prompt = "{name}, where would you like to put your O-marker?  ".format(name=playerNames[1])
            entry = human()
        else:
            entry = computer()
            print("Computer chososes {entry}".format(entry=entry))
            time.sleep(2)
        boxes[entry] = 'O'
    else:
        if playerFunction[0] == 1:
            entry = human()
        else:
            entry = computer()
            print("Computer chososes {entry}".format(entry=entry))
            time.sleep(2)
        boxes[entry] = 'X'
    movesMade.append(entry)
    counter += 1
    findwinner()


# The human function
def human():
    global movesMade
    global prompt
    redo = True
    while redo == True:
        if counter % 2 == 0:
            prompt = "{name}, where would you like to put your O-marker?  ".format(name=playerNames[1])
        else:
            prompt = "{name}, where would you like to put your X-marker?  ".format(name=playerNames[0])
        humanEntry = input(prompt)
        if humanEntry == 'q':
            exit()
        if humanEntry not in possibleMoves:
            print("I'm sorry. Please enter a single lower-case letter from 'a' to 'i'.")
            redo = True
        elif humanEntry in movesMade:
            print("I'm sorry. That box has been take, already.")
            redo = True
        else:
            redo = False
    return humanEntry


# The computer function
def computer():
    global movesMade, playerNames
    if playerNames[0] == 'Computer':
        marker = 'X'
        oppMarker = 'O'
    else:
        marker = 'O'
        oppMarker = 'X'
    same = True
    if boxes['a'] == marker and boxes['c'] == marker and ('b' not in movesMade):
        compMove = 'b'
    elif boxes['d'] == marker and boxes['f'] == marker and ('e' not in movesMade):
        compMove = 'e'
    elif boxes['g'] == marker and boxes['i'] == marker and ('h' not in movesMade):
        compMove = 'h'
    elif boxes['a'] == marker and boxes['g'] == marker and ('d' not in movesMade):
        compMove = 'd'
    elif boxes['b'] == marker and boxes['h'] == marker and ('e' not in movesMade):
        compMove = 'e'
    elif boxes['c'] == marker and boxes['i'] == marker and ('f' not in movesMade):
        compMove = 'f'
    elif boxes['a'] == marker and boxes['i'] == marker and ('e' not in movesMade):
        compMove = 'e'
    elif boxes['c'] == marker and boxes['g'] == marker and ('e' not in movesMade):
        compMove = 'e'
    elif boxes['a'] == oppMarker and boxes['c'] == oppMarker and ('b' not in movesMade):
        compMove = 'b'
    elif boxes['d'] == oppMarker and boxes['f'] == oppMarker and ('e' not in movesMade):
        compMove = 'e'
    elif boxes['g'] == oppMarker and boxes['i'] == oppMarker and ('h' not in movesMade):
        compMove = 'h'
    elif boxes['a'] == oppMarker and boxes['g'] == oppMarker and ('d' not in movesMade):
        compMove = 'd'
    elif boxes['b'] == oppMarker and boxes['h'] == oppMarker and ('e' not in movesMade):
        compMove = 'e'
    elif boxes['c'] == oppMarker and boxes['i'] == oppMarker and ('f' not in movesMade):
        compMove = 'f'
    elif boxes['a'] == oppMarker and boxes['i'] == oppMarker and ('e' not in movesMade):
        compMove = 'e'
    elif boxes['c'] == oppMarker and boxes['g'] == oppMarker and ('e' not in movesMade):
        compMove = 'e'
    else:
        if boxes['a'] == ' ' or boxes['g'] == ' ' or boxes['c'] == ' ' or boxes['i'] == ' ':
            validMoves = ['a',  'c', 'g', 'i', 'e', 'a', 'c', 'g', 'i']
        else:
            validMoves = ['b', 'd', 'e', 'f', 'h']
        while same == True:
            compMove = random.choice(validMoves)
            if compMove not in movesMade:
                same = False
    return compMove


# Prints the board
def printboard():
    print(" A | B | C ")
    print(" {a} | {b} | {c} ".format(a=boxes["a"], b=boxes["b"], c=boxes["c"]))
    print("___|___|___")
    print(" D | E | F ")
    print(" {d} | {e} | {f} ".format(d=boxes['d'], e=boxes['e'], f=boxes['f']))
    print("___|___|___")
    print(" G | H | I ")
    print(" {g} | {h} | {i} ".format(g=boxes['g'], h=boxes['h'], i=boxes['i']))
    print("   |   |   ")

# Checks if someone has won
def findwinner():
    global oWin, xWin, winner
    if ((boxes['a'] == 'X' and boxes['b'] == 'X' and boxes['c'] == 'X') or
        (boxes['d'] == 'X' and boxes['e'] == 'X' and boxes['f'] == 'X') or
        (boxes['g'] == 'X' and boxes['h'] == 'X' and boxes['i'] == 'X') or
        (boxes['a'] == 'X' and boxes['d'] == 'X' and boxes['g'] == 'X') or
        (boxes['b'] == 'X' and boxes['e'] == 'X' and boxes['h'] == 'X') or
        (boxes['c'] == 'X' and boxes['f'] == 'X' and boxes['i'] == 'X') or
        (boxes['a'] == 'X' and boxes['e'] == 'X' and boxes['i'] == 'X') or
        (boxes['c'] == 'X' and boxes['e'] == 'X' and boxes['g'] == 'X')):
        xWin = True
    if ((boxes['a'] == 'O' and boxes['b'] == 'O' and boxes['c'] == 'O') or
        (boxes['d'] == 'O' and boxes['e'] == 'O' and boxes['f'] == 'O') or
        (boxes['g'] == 'O' and boxes['h'] == 'O' and boxes['i'] == 'O') or
        (boxes['a'] == 'O' and boxes['d'] == 'O' and boxes['g'] == 'O') or
        (boxes['b'] == 'O' and boxes['e'] == 'O' and boxes['h'] == 'O') or
        (boxes['c'] == 'O' and boxes['f'] == 'O' and boxes['i'] == 'O') or
        (boxes['a'] == 'O' and boxes['e'] == 'O' and boxes['i'] == 'O') or
        (boxes['c'] == 'O' and boxes['e'] == 'O' and boxes['g'] == 'O')):
        yWin = True
    if oWin == True or xWin == True:
        winner = True
    if counter > 9 and (oWin == False and xWin == False):
        winner = True


# Closing time
def gameover():
    global again, xWin, winner
    os.system('clear')
    printboard()
    if winner == True and (xWin == True or oWin == True):
        if xWin == True and playerNames[0] != 'Computer':
            print("{name} is the winner".format(name=playerNames[0]))
        elif oWin == True and playerNames[1] != 'Computer':
            print("{name} is the winner".format(name=playerNames[1]))
        elif xWin == True and playerNames[0] == 'Computer':
            print("The computer beaten the human!r".format(name=playerNames[0]))
            print("BOW BEFORE THE SUPERIOR INTELECT")
        elif oWin == True and playerNames[1] == 'Computer':
            print("The computer beaten the human!r".format(name=playerNames[0]))
            print("BOW BEFORE THE SUPERIOR INTELECT")
    else:
        print("\nThe game has ended in a tie.")
        print('I guess, "THE ONLY WINNING MOVE IS NOT TO PLAY"\n\n')
    again = input("Do you want to play again (y/n)? ")
    if again == 'n':
        print("Ciao!")
        exit()


# MAIN
while again == 'y':
    initialize()
    intro()
    while winner == False:
        gameplay()
    gameover()