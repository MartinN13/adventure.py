#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An adventure game.
"""

import sys
import getopt

def usage():
    """
    Prints possible options.
    """
    print("""\nadventure.py. By Martin Nabhan. Version 1.0.
 
Options:
  -h --help        Display this help message.
  -i --info        Prints a description of the game and the idea behind it.
  -v --version     Prints version number.
  -a --about       Prints a short introduction of the game's creator.
  -c --cheat       Tells how to solve the game, and how to load a finished save-game.
 """)

def info():
    """
    Prints a description of the game.
    """
    print("\nThe idea for this game came from having played a lot of escape-games as "
          "a child. Especially 'Mysteriet på greveholm' (an escape-game based on a Swedish TV-series "
          "of the same name) brings back fond memories. The basic premise is of you and a stranger named "
          "Marvin waking up in a mysterious castle and having to solve various problems to escape this cold, damp place.")

def version():
    """
    Prints the version number.
    """
    print("1.0")

def about():
    """
    Prints info about the creator.
    """
    print("\nMy name is Martin Nabhan, I'm a student at Blekinge Institute of Technology "
          "currently studying web-programming. I hope you'll enjoy this game!")

def cheat():
    """
    Prints instructions how to beat the game quickly.
    """
    print("\nTo cheat...\n")

def roomInfo(room):
    """
    Describes the current room.
    """
    if room == 0:
        print("\nA cold, stone-tiled room looking as if it belongs to an old medieval castle presents itself in front of you. "
              "There are no windows and there seems to be no other way to escape but through the main door.")
    elif room == 1:
        print("This is room 2.")
    elif room == 2:
        print("This is room 3.")
    elif room == 3:
        print("This is room 4.")
    elif room == 4:
        print("This is room 5.")
    elif room == 5:
        print("This is room 6.")
    elif room == 6:
        print("This is room 7.")

def hjalp():
    """
    Lists available commands.
    """
    print("""\nThe available commands in this game are:

i, info - Tells you about the current room.
h, hjälp - Shows you all available commands.
fr, fram - Moves to the next room, if unlocked.
ba, bak - Moves to the previous room.
se - Look around the room for anything suspicious.
l, ledtråd - Gives a hint.

o, object - Tells you what items are in the room.
t [object], titta [object] - Describes [object].
ö [object], öppna [object] - Opens [object], if possible.
s [object], sparka [object] - Kicks [object], if possible.
f [object], flytta [object] - Moves [object], if p

inv, inventarier - Tells you what's in your inventory.
ta [object] - Adds [object] to inventory, if possible.
sl [object], släpp [object] - Drops [object], if in inventory.
a [object], använd [object] - Uses [object], if possible.
""")

def fram(currentRoom, inventory):
    """
    Move forward one room.
    """
    if currentRoom == 0 and 'key1' in inventory:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    elif currentRoom == 1 and 'key2' in inventory:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    elif currentRoom == 2 and 'key3' in inventory:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    elif currentRoom == 3 and 'key4' in inventory:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    elif currentRoom == 4 and 'key5' in inventory:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    elif currentRoom == 5 and 'key6' in inventory:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    elif currentRoom == 6 and 'key7' in inventory:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    else:
        print("\nYou haven't unlocked the next room yet!")
    return(currentRoom)

def bak(currentRoom):
    """
    Go back one room.
    """
    if currentRoom == 0:
        print("\nYou are already in the first room!")
    else:
        currentRoom = currentRoom - 1
        roomSelector(currentRoom)
    return(currentRoom)

def se(room):
    """
    Look around the room.
    """
    if room == 0:
        print("\nTrying to escape you realize there's a locked padlock on the door, requiring a four-digit passcode. "
              "Marvin happens to notice a note laying on the table in the lower-left corner of the room. "
              "Maybe the note has some clues as to where you are and how you can escape?"
              "\n\nTo read the note tell Marvin 't note' or 'titta note'.")
    elif room == 1:
        print("In room 2 there is...")
    elif room == 2:
        print("In room 3 there is...")
    elif room == 3:
        print("In room 4 there is...")
    elif room == 4:
        print("In room 5 there is...")
    elif room == 5:
        print("In room 6 there is...")
    elif room == 6:
        print("In room 7 there is...")

def ledtrad(room, clueCounter):
    """
    Gives a clue.
    """
    if room == 0:
        if clueCounter == 0:
            print("\nTo take a look around the room tell Marvin 'se'.")
        elif clueCounter == 1:
            print("\nA new day starts at 00:00.")
        else:
            print("\nThere are no more clues!")
    elif room == 1:
        print("Clue 1 for room 2 is...")
    elif room == 2:
        print("Clue 1 for room 3 is...")
    elif room == 3:
        print("Clue 1 for room 4 is...")
    elif room == 4:
        print("Clue 1 for room 5 is...")
    elif room == 5:
        print("Clue 1 for room 6 is...")
    elif room == 6:
        print("Clue 1 for room 7 is...")

    clueCounter = clueCounter + 1
    return(clueCounter)

def objects(room):
    """
    Prints all items in the room.
    """
    if room == 0:
        print("\nIn this room there is a table with a note on it.")
    elif room == 1:
        print("In room 2 there is...")
    elif room == 2:
        print("In room 3 there is...")
    elif room == 3:
        print("In room 4 there is...")
    elif room == 4:
        print("In room 5 there is...")
    elif room == 5:
        print("In room 6 there is...")
    elif room == 6:
        print("In room 7 there is...")

def titta(objectName):
    """
    Describes an object.
    """
    if objectName == 'note':
        print("\nWhen there is darkness, be the first to shine a light."
              "When there is injustice, be the first to condemn it."
              "When something seems difficult, do it anyway."
              "When life seems to beat you down, fight back."
              "When a new day begins, open a new door.")
    elif objectName == 'someObject':
        print("This is...")
    elif objectName == 'someObject':
        print("This is...")
    elif objectName == 'someObject':
        print("This is...")
    elif objectName == 'someObject':
        print("This is...")
    elif objectName == 'someObject':
        print("This is...")
    elif objectName == 'someObject':
        print("This is...")
    else:
        print("\nThere is no such object!")

    
def oppna(objectName):
    """
    Opens an object, if possible.
    """
    if objectName == 'someObject':
        print("Open result here")
    elif objectName == 'someObject':
        print("Open result here")
    else:
        print("\nThis object can't be opened!")
    
def sparka(objectName):
    """
    Kicks an object, if possible, and breaks it.
    """
    if objectName == 'someObject':
        print("Kick result here")
    elif objectName == 'someObject':
        print("Kick result here")
    else:
        print("\nThis object can't be kicked!")
    
def flytta(objectName):
    """
    Moves an object, if possible.
    """
    if objectName == 'someObject':
        print("Move result here")
    elif objectName == 'someObject':
        print("Move result here")
    else:
        print("\nThis object can't be moved!")

def inventoryList(inventory):
    """
    Prints the players inventory.
    """
    inventoryCount = 0
    inventoryNames = ""
    if not inventory:
        print("\nYour inventory is empty!")
    else:
        for item in inventory:
            inventoryNames = inventoryNames + item + " "
        print("\nYour inventory contains: \n%s" % inventoryNames)

def ta(objectName, inventory):
    """
    Adds an object to inventory.
    """
    if objectName == 'takeable item':
        inventory.append(objectName)
        print("\n%s was added to your inventory." % objectName.capitalize())
    else:
        print("\nThis object can't be taken!")

def slapp(objectName, inventory):
    """
    Drops an item from inventory.
    """
    if objectName in inventory:
        inventory.remove(objectName)
        print("\n%s was remoed from your inventory." % objectName.capitalize())
    else:
        print("\nThere is no such item in your inventory!")

def anvand(objectName, inventory):
    """
    Uses an item from inventory.
    """
    if objectName in inventory:
        if objectName == 'key0':
            print("\nYou unlocked the door to room 2!"
                  "Open the door by telling Marvin 'fr' or 'fram'.")
        elif objectName == 'someItem':
            print("Item reaction here")
        else:
            print("\nThis item doesn't do anything.")
    else:
        print("\nThere is no such item in your inventory!")

def roomSelector(currentRoom):
    """
    Prints the users current room.
    """
    if currentRoom == 0:
        print("""
                        Room 1
               __________==__________
              |                      |
              |   Welcome note       |
              |                      |
              |                      |
              |  _                   |
              | |_|                  |
              |______________________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 1:
        print("""
                        Room 2
               __________==__________
              |                      |
              |                      |
              |                      |
              |                      |
              |  _                   |
              | |_|                  |
              |______________________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 2:
        print("""
                        Room 3
               __________==__________
              |                      |
              |                      |
              |                      |
              |                      |
              |  _                   |
              | |_|                  |
              |______________________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 3:
        print("""
                        Room 4
               __________==__________
              |                      |
              |                      |
              |  Rope-magnet-fishing |
              |                      |
              |  _                   |
              | |_|                  |
              |______________________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 4:
        print("""
                        Room 5
               __________==__________
              |                      |
              |                      |
              |                      |
              |       UV-Light       |
              |  _                   |
              | |_|                  |
              |______________________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 5:
        print("""
                        Room 6
               __________==__________
              |                      |
              |                      |
              |                      |
              |  Schiffer-decrypt    |
              |  _                   |
              | |_|                  |
              |______________________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 6:
        print("""
                        Room 7
               __________==__________
              |                      |
              |                      |
              |                      |
              |      TicTacToe       |
              |  _                   |
              | |_|                  |
              |______________________|
              """)
        roomInfo(currentRoom)


def mainGame():
    """
    The main function of the game.
    """
    currentRoom = 0
    clueCount = 0
    padlock1 = 0
    inventory = ["key1", "key2"]

    print("\nWelcome to this mysterious adventure! Tell Marvin 'h' or 'hjälp' to get a list of all available commands. "
          "Whenever you get into a new room it might be useful to use the 'se' command to look around. If you get stuck "
          "don't forget you can always get a hint with 'l' or 'ledtråd'."
          "\n\nYou and a stranger named Marvin suddenly wake up in a cold, damp room. "
          "Where are you and how will you escape? Maybe there is something in the room you can use?")

    input("\nPress enter to continue...")

    roomSelector(currentRoom)

    while True:
        command = input("\nTell Marvin what you want to do: ")

        # Room commands.
        if 'i' in command.split():
            roomInfo(currentRoom)
        elif 'info' in command.split():
            roomInfo(currentRoom)
        elif 'h' in command.split():
            hjalp()
        elif 'hjälp' in command.split():
            hjalp()
        elif 'fr' in command.split():
            currentRoom = fram(currentRoom, inventory)
        elif 'fram' in command.split():
            currentRoom = fram(currentRoom, inventory)
        elif 'ba' in command.split():
            currentRoom = bak(currentRoom)
        elif 'bak' in command.split():
            currentRoom = bak(currentRoom)
        elif 'se' in command.split():
            se(currentRoom)
        elif 'l' in command.split():
            clueCount = ledtrad(currentRoom, clueCount)
        elif 'ledtråd' in command.split():
            clueCount = ledtrad(currentRoom, clueCount)
        # Item commands.
        elif 'o' in command.split():
            objects(currentRoom)
        elif 'objekt' in command.split():
            objects(currentRoom)
        elif 't ' in command:
            titta(command[2:len(command)])
        elif 'titta ' in command:
            titta(command[6:len(command)])
        elif 'ö ' in command:
            oppna(command[2:len(command)])
        elif 'öppna ' in command:
            oppna(command[6:len(command)])
        elif 's ' in command:
            sparka(command[2:len(command)])
        elif 'sparka ' in command:
            sparka(command[7:len(command)])
        elif 'f ' in command:
            flytta(command[2:len(command)])
        elif 'flytta ' in command:
            flytta(command[7:len(command)])
        # Inventory commands.
        elif 'inv' in command.split():
            inventoryList(inventory)
        elif 'inventarier' in command.split():
            inventoryList(inventory)
        elif 'ta ' in command:
            ta(command[3:len(command)])
        elif 'sl ' in command:
            slapp(command[3:len(command)])
        elif 'släpp ' in command:
            slapp(command[6:len(command)])
        elif 'a ' in command:
            anvand(command[2:len(command)])
        elif 'använd ' in command:
            anvand(command[7:len(command)])
        else:
            print("\nMarvin doesn't understand you!")
    
def main():    
    """
    The main function of the program, which looks for options and launches the game.
    """          
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hivac", ["help", "info", "version", "about", "cheat"])
    except getopt.GetoptError:          
        usage()                        
        sys.exit(1)                     
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()                     
            sys.exit(0) 
        elif opt in ("-i", "--info"):
            info()
            sys.exit(0)   
        elif opt in ("-v", "--version"):
            version()
            sys.exit(0)
        elif opt in ("-a", "--about"):
            about()
            sys.exit(0)
        elif opt in ("-c", "--cheat"):
            cheat()
            sys.exit(0)
    mainGame()

if __name__ == "__main__":
    main()
