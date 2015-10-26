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
            print('You won!')
            break
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
            print('You lost!')
            break
        # or draw!
        elif counter >= 9:
            print("It's a draw!")
            break

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
            char = "o"
            posY = input("Enter a row: ")
            posX = input("Enter a column (or q for quit): ")

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
