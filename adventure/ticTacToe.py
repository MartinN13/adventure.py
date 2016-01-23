#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A game of tic-tac-toe, set on the highest difficulty possible.
"""

filename = 'tictactoe.txt'

def createMatrix(y, x, filler):
    """
    Create a two-dimensional array and return it. 
    """
    return [[filler for _ in range(x)] for _ in range(y)]

def printMatrix(matrix):
    """
    Print the content of the matrix. 
    """
    print(" _ _ _")
    for row in matrix:
        print("|" + "|".join(row) + "|")

def saveMatrix(matrix):
    """
    Saves the game into a file.
    """
    with open(filename, 'w') as f:
        for row in matrix:
            f.write("".join(row) + '\n')

    print("Saved the state to the file {}".format(filename))

def loadMatrix(matrix):
    """
    Loads a game from a file.
    """
    with open(filename, 'r') as f:
        content = f.read().splitlines()
        for y in range(0, len(matrix)):
            matrix[y] = list(content[y])

    print("Loaded the state from the file {}".format(filename))

def main():
    """
    Main function.
    """
    print("""\nMarvin says: 'Before we start I will explain the rules of the game.
You get to start, and you play as 'o' while I'm 'x'.
The game works in that you select which row and column you want to place your marker on.""")

    input("\nPress enter to continue...")

    print("""\nThe game-board is divided like this:

   0 1 2
   _ _ _
0 |_|_|_|
1 |_|_|_|
2 |_|_|_|""")

    input("\nPress enter to continue...")

    print("""\nFor example, if you were to select row 0, column 0, and the next turn row 1, column 1, you would get:

 _ _ _
|o|_|_|
|_|o|_|
|_|_|_|""")

    input("\nPress enter to continue...")

    print("""\nYou can save your game any time by writing 's' as your choice on either the row or column choice.
To load the last saved game write 'l' instead.

Good luck!""")

    input("\nPress enter to continue...")

    matrix = createMatrix(3, 3, "_")

    counter = 0
    while 1:
        printMatrix(matrix)
        # Winning...
        if matrix[0][0] == matrix[0][1] == matrix[0][2] and \
           matrix[0][0] != "x" and matrix[0][0] != "_" and \
           matrix[0][1] != "x" and matrix[0][1] != "_" and \
           matrix[0][2] != "x" and matrix[0][2] != "_" or \
           matrix[1][0] == matrix[1][1] == matrix[1][2] and \
           matrix[1][0] != "x" and matrix[1][0] != "_" and \
           matrix[1][1] != "x" and matrix[1][1] != "_" and \
           matrix[1][2] != "x" and matrix[1][2] != "_" or \
           matrix[2][0] == matrix[2][1] == matrix[2][2] and \
           matrix[2][0] != "x" and matrix[2][0] != "_" and \
           matrix[2][1] != "x" and matrix[2][1] != "_" and \
           matrix[2][2] != "x" and matrix[2][2] != "_" or \
           matrix[0][0] == matrix[1][0] == matrix[2][0] and \
           matrix[0][0] != "x" and matrix[0][0] != "_" and \
           matrix[1][0] != "x" and matrix[1][0] != "_" and \
           matrix[2][0] != "x" and matrix[2][0] != "_" or \
           matrix[0][1] == matrix[1][1] == matrix[2][1] and \
           matrix[0][1] != "x" and matrix[0][1] != "_" and \
           matrix[1][1] != "x" and matrix[1][1] != "_" and \
           matrix[2][1] != "x" and matrix[2][1] != "_" or \
           matrix[0][2] == matrix[1][2] == matrix[2][2] and \
           matrix[0][2] != "x" and matrix[0][2] != "_" and \
           matrix[1][2] != "x" and matrix[1][2] != "_" and \
           matrix[2][2] != "x" and matrix[2][2] != "_" or \
           matrix[0][0] == matrix[1][1] == matrix[2][2] and \
           matrix[0][0] != "x" and matrix[0][0] != "_" and \
           matrix[1][1] != "x" and matrix[1][1] != "_" and \
           matrix[2][2] != "x" and matrix[2][2] != "_" or \
           matrix[0][2] == matrix[1][1] == matrix[2][0] and \
           matrix[0][2] != "x" and matrix[0][2] != "_" and\
           matrix[1][1] != "x" and matrix[1][1] != "_" and \
           matrix[2][0] != "x" and matrix[2][0] != "_":
            # Won game
            return 1
        # or losing...
        elif matrix[0][0] == matrix[0][1] == matrix[0][2] and \
             matrix[0][0] != "o" and matrix[0][0] != "_" and \
             matrix[0][1] != "o" and matrix[0][1] != "_" and \
             matrix[0][2] != "o" and matrix[0][2] != "_" or \
             matrix[1][0] == matrix[1][1] == matrix[1][2] and \
             matrix[1][0] != "o" and matrix[1][0] != "_" and \
             matrix[1][1] != "o" and matrix[1][1] != "_" and \
             matrix[1][2] != "o" and matrix[1][2] != "_" or \
             matrix[2][0] == matrix[2][1] == matrix[2][2] and \
             matrix[2][0] != "o" and matrix[2][0] != "_" and \
             matrix[2][1] != "o" and matrix[2][1] != "_" and \
             matrix[2][2] != "o" and matrix[2][2] != "_" or \
             matrix[0][0] == matrix[1][0] == matrix[2][0] and \
             matrix[0][0] != "o" and matrix[0][0] != "_" and \
             matrix[1][0] != "o" and matrix[1][0] != "_" and \
             matrix[2][0] != "o" and matrix[2][0] != "_" or \
             matrix[0][1] == matrix[1][1] == matrix[2][1] and \
             matrix[0][1] != "o" and matrix[0][1] != "_" and \
             matrix[1][1] != "o" and matrix[1][1] != "_" and \
             matrix[2][1] != "o" and matrix[2][1] != "_" or \
             matrix[0][2] == matrix[1][2] == matrix[2][2] and \
             matrix[0][2] != "o" and matrix[0][2] != "_" and \
             matrix[1][2] != "o" and matrix[1][2] != "_" and \
             matrix[2][2] != "o" and matrix[2][2] != "_" or \
             matrix[0][0] == matrix[1][1] == matrix[2][2] and \
             matrix[0][0] != "o" and matrix[0][0] != "_" and \
             matrix[1][1] != "o" and matrix[1][1] != "_" and \
             matrix[2][2] != "o" and matrix[2][2] != "_" or \
             matrix[0][2] == matrix[1][1] == matrix[2][0] and \
             matrix[0][2] != "o" and matrix[0][2] != "_" and\
             matrix[1][1] != "o" and matrix[1][1] != "_" and \
             matrix[2][0] != "o" and matrix[2][0] != "_":
            # Lost game
            return 2
        # or draw!
        elif counter >= 9:
            # Draw game
            return 1

        if counter % 2: # Computer's turn
            char = "x"
            # First we block any chance to win
            if matrix[0][0] == matrix[1][0] != "_" and matrix[2][0] != "o" and matrix[2][0] != "x":
                posY = 2
                posX = 0
            elif matrix[0][1] == matrix[1][1] != "_" and matrix[2][1] != "o" and matrix[2][1] != "x":
                posY = 2
                posX = 1
            elif matrix[0][2] == matrix[1][2] != "_" and matrix[2][2] != "o" and matrix[2][2] != "x":
                posY = 2
                posX = 2
            elif matrix[2][0] == matrix[1][0] != "_" and matrix[0][0] != "o" and matrix[0][0] != "x":
                posY = 0
                posX = 0
            elif matrix[2][1] == matrix[1][1] != "_" and matrix[0][1] != "o" and matrix[0][1] != "x":
                posY = 0
                posX = 1
            elif matrix[2][2] == matrix[1][2] != "_" and matrix[0][2] != "o" and matrix[0][2] != "x":
                posY = 0
                posX = 2
            elif matrix[0][0] == matrix[2][0] != "_" and matrix[1][0] != "o" and matrix[1][0] != "x":
                posY = 1
                posX = 0
            elif matrix[0][1] == matrix[2][1] != "_" and matrix[1][1] != "o" and matrix[1][1] != "x":
                posY = 1
                posX = 1
            elif matrix[0][2] == matrix[2][2] != "_" and matrix[1][2] != "o" and matrix[1][2] != "x":
                posY = 1
                posX = 2
            elif matrix[0][0] == matrix[0][1] != "_" and matrix[0][2] != "o" and matrix[0][2] != "x":
                posY = 0
                posX = 2
            elif matrix[1][0] == matrix[1][1] != "_" and matrix[1][2] != "o" and matrix[1][2] != "x":
                posY = 1
                posX = 2
            elif matrix[2][0] == matrix[2][1] != "_" and matrix[2][2] != "o" and matrix[2][2] != "x":
                posY = 2
                posX = 2
            elif matrix[0][2] == matrix[0][1] != "_" and matrix[0][0] != "o" and matrix[0][0] != "x":
                posY = 0
                posX = 0
            elif matrix[1][2] == matrix[1][1] != "_" and matrix[1][0] != "o" and matrix[1][0] != "x":
                posY = 1
                posX = 0
            elif matrix[2][2] == matrix[2][1] != "_" and matrix[2][0] != "o" and matrix[2][0] != "x":
                posY = 2
                posX = 0
            elif matrix[0][0] == matrix[0][2] != "_" and matrix[0][1] != "o" and matrix[0][1] != "x":
                posY = 0
                posX = 1
            elif matrix[1][0] == matrix[1][2] != "_" and matrix[1][1] != "o" and matrix[1][1] != "x":
                posY = 0
                posX = 1
            elif matrix[2][0] == matrix[2][2] != "_" and matrix[2][1] != "o" and matrix[2][1] != "x":
                posY = 0
                posX = 2
            elif matrix[0][0] == matrix[1][1] != "_" and matrix[2][2] != "o" and matrix[2][2] != "x":
                posY = 2
                posX = 2
            elif matrix[2][2] == matrix[1][1] != "_" and matrix[0][0] != "o" and matrix[0][0] != "x":
                posY = 0
                posX = 0
            elif matrix[0][2] == matrix[1][1] != "_" and matrix[2][0] != "o" and matrix[2][0] != "x":
                posY = 2
                posX = 0
            elif matrix[2][0] == matrix[1][1] != "_" and matrix[0][2] != "o" and matrix[0][2] != "x":
                posY = 0
                posX = 2
            elif matrix[0][0] == matrix[2][2] != "_" and matrix[1][1] != "o" and matrix[1][1] != "x":
                posY = 1
                posX = 1
            elif matrix[0][2] == matrix[2][0] != "_" and matrix[1][1] != "o" and matrix[1][1] != "x":
                posY = 1
                posX = 1
            # If oppponent starts on corner
            elif matrix[0][0] == "o" or \
                 matrix[0][2] == "o" or \
                 matrix[2][0] == "o" or \
                 matrix[2][2] == "o":
                 # Take empty center
                if matrix[1][1] == "_" and matrix[1][1] != "o":
                    posY = 1
                    posX = 1
                # Take empty edge
                else:
                    if matrix[0][1] == "_" and matrix[0][1] != "o"  and matrix[0][1] != "x":
                        posY = 0
                        posX = 1
                    elif matrix[1][0] == "_" and matrix[1][0] != "o" and matrix[1][0] != "x":
                        posY = 1
                        posX = 0
                    elif matrix[1][2] == "_" and matrix[1][2] != "o" and matrix[1][2] != "x":
                        posY = 1
                        posX = 2
                    elif matrix[2][1] == "_" and matrix[2][1] != "o" and matrix[2][1] != "x":
                        posY = 2
                    # Take remaining empty slots
                    else:
                        if matrix[0][0] == "_":
                            posY = 0
                            posX = 0
                        elif matrix[0][1] == "_":
                            posY = 0
                            posX = 1
                        elif matrix[0][2] == "_":
                            posY = 0
                            posX = 2
                        elif matrix[1][0] == "_":
                            posY = 1
                            posX = 0
                        elif matrix[1][1] == "_":
                            posY = 1
                            posX = 1
                        elif matrix[1][2] == "_":
                            posY = 1
                            posX = 2
                        elif matrix[2][0] == "_":
                            posY = 2
                            posX = 0
                        elif matrix[2][1] == "_":
                            posY = 2
                            posX = 1
                        elif matrix[2][2] == "_":
                            posY = 2
                            posX = 2
            # If opponent starts on center, take empty corner
            elif matrix[1][1] == "o":
                if matrix[0][0] == "_" and matrix[0][0] != "o"  and matrix[0][0] != "x":
                    posY = 0
                    posX = 0
                elif matrix[0][2] == "_" and matrix[0][2] != "o" and matrix[0][2] != "x":
                    posY = 0
                    posX = 2
                elif matrix[2][0] == "_" and matrix[2][0] != "o" and matrix[2][0] != "x":
                    posY = 2
                    posX = 0
                elif matrix[2][2] == "_" and matrix[2][2] != "o" and matrix[2][2] != "x":
                    posY = 2
                    posX = 2
                # Take remaining empty slots
                else:
                    if matrix[0][0] == "_":
                        posY = 0
                        posX = 0
                    elif matrix[0][1] == "_":
                        posY = 0
                        posX = 1
                    elif matrix[0][2] == "_":
                        posY = 0
                        posX = 2
                    elif matrix[1][0] == "_":
                        posY = 1
                        posX = 0
                    elif matrix[1][1] == "_":
                        posY = 1
                        posX = 1
                    elif matrix[1][2] == "_":
                        posY = 1
                        posX = 2
                    elif matrix[2][0] == "_":
                        posY = 2
                        posX = 0
                    elif matrix[2][1] == "_":
                        posY = 2
                        posX = 1
                    elif matrix[2][2] == "_":
                        posY = 2
                        posX = 2  
            # If opponent starts on edge           
            else:
                # Take empty center
                if matrix[1][1] == "_" and matrix[1][1] != "o":
                    posY = 1
                    posX = 1
                # Take empty corner
                elif matrix[1][1] == "x":
                    if matrix[0][1] == "o" and matrix[2][1] == "o" or \
                       matrix[1][0] == "o" and matrix[1][2] == "o":
                        if matrix[0][0] == "_" and matrix[0][0] != "o"  and matrix[0][0] != "x":
                            posY = 0
                            posX = 0
                        elif matrix[0][2] == "_" and matrix[0][2] != "o" and matrix[0][2] != "x":
                            posY = 0
                            posX = 2
                        elif matrix[2][0] == "_" and matrix[2][0] != "o" and matrix[2][0] != "x":
                            posY = 2
                            posX = 0
                        elif matrix[2][2] == "_" and matrix[2][2] != "o" and matrix[2][2] != "x":
                            posY = 2
                            posX = 2 
        else:
            playerMove = 0

            while playerMove < 1:
                char = "o"
                posY = input("Enter a row: ")
                posX = input("Enter a column (or q for quit): ")
                if matrix[int(posY)][int(posX)] == "x" or matrix[int(posY)][int(posX)] == "o":
                    print("\nThat spot is already taken!\n")
                    playerMove = 0
                else:
                    playerMove = 1



        counter += 1

        if posY == "q" or posX == "q":
            break
        elif posY == "s" or posX == "s":
            saveMatrix(matrix)
            continue
        elif posY == "l" or posX == "l":
            loadMatrix(matrix)
            loadCount = 0
            # Count number of turns taken
            for item in matrix:
                for subitem in item:
                    if "x" in subitem:
                        loadCount = loadCount + 1
                    elif "o" in subitem:
                        loadCount = loadCount + 1

            counter = loadCount
            continue

        matrix[int(posY)][int(posX)] = char
