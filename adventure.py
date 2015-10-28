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
    print("""adventure.py. By Martin Nabhan. Version 1.0.
 
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
    print("Explanation of game")

def version():
    """
    Prints the version number.
    """
    print("1.0")

def about():
    """
    Prints info about the creator.
    """
    print("""My name is Martin Nabhan, I'm a student at Blekinge Institute of Technology 
currently studying web-programming. I hope you'll enjoy this game!
""")

def cheat():
    """
    Prints instructions how to beat the game quickly.
    """
    print("To cheat...")

def roomInfo(room):
    """
    Describes the current room.
    """
    if room == 0:
        print("This is room 1.")
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
    print("""The available commands in this game are:

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

def fram(room, inventory):
    """
    Move forward one room.
    """
    if room == 0 and key0 in inventory:
        currentRoom = room + 1
        roomSelector(currentRoom)
    elif room == 1 and key1 in inventory:
        currentRoom = room + 1
        roomSelector(currentRoom)
    elif room == 2 and key2 in inventory:
        currentRoom = room + 1
        roomSelector(currentRoom)
    elif room == 3 and key3 in inventory:
        currentRoom = room + 1
        roomSelector(currentRoom)
    elif room == 4 and key4 in inventory:
        currentRoom = room + 1
        roomSelector(currentRoom)
    elif room == 5 and key5 in inventory:
        currentRoom = room + 1
        roomSelector(currentRoom)
    elif room == 6 and key6 in inventory:
        currentRoom = room + 1
        roomSelector(currentRoom)
    else:
        print("You haven't unlocked the next room yet!")

def bak(room):
    """
    Go back one room.
    """
    if room == 0:
        print("You are already in the first room!")
    else:
        currentRoom = room - 1
        roomSelector(currentRoom)

def se(room):
    """
    Look around the room.
    """
    if room == 0:
        print("In this room there is...")
    elif room == 1:
        print("In this room there is...")
    elif room == 2:
        print("In this room there is...")
    elif room == 3:
        print("In this room there is...")
    elif room == 4:
        print("In this room there is...")
    elif room == 5:
        print("In this room there is...")
    elif room == 6:
        print("In this room there is...")

def ledtrad(room):
    """
    Gives a clue.
    """
    if room == 0:
        print("Clue 1 for this room is...")
    elif room == 1:
        print("Clue 1 for this room is...")
    elif room == 2:
        print("Clue 1 for this room is...")
    elif room == 3:
        print("Clue 1 for this room is...")
    elif room == 4:
        print("Clue 1 for this room is...")
    elif room == 5:
        print("Clue 1 for this room is...")
    elif room == 6:
        print("Clue 1 for this room is...")

def objects(room):
    """
    Prints all items in the room.
    """
    if room == 0:
        print("In this room there is a table with a note on it.")
    elif room == 1:
        print("In this room there is...")
    elif room == 2:
        print("In this room there is...")
    elif room == 3:
        print("In this room there is...")
    elif room == 4:
        print("In this room there is...")
    elif room == 5:
        print("In this room there is...")
    elif room == 6:
        print("In this room there is...")

def titta(objectName):
    """
    Describes an object.
    """
    if objectName == 'note':
        print("Welcome to this mysterious adventure! Tell Marvin 'h' or 'hjälp' to get a list of available commands.")
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
        print("There is no such object!")

    
def oppna(objectName):
    """
    Opens an object, if possible.
    """
    if objectName == 'someObject':
        print("Open result here")
    elif objectName == 'someObject':
        print("Open result here")
    else:
        print("This object can't be opened!")
    
def sparka(objectName):
    """
    Kicks an object, if possible, and breaks it.
    """
    if objectName == 'someObject':
        print("Kick result here")
    elif objectName == 'someObject':
        print("Kick result here")
    else:
        print("This object can't be kicked!")
    
def flytta(objectName):
    """
    Moves an object, if possible.
    """
    if objectName == 'someObject':
        print("Move result here")
    elif objectName == 'someObject':
        print("Move result here")
    else:
        print("This object can't be moved!")

def inventoryList(inventory):
    """
    Prints the players inventory.
    """
    inventoryCount = 0
    inventoryNames = ""
    if not inventory:
        print("Your inventory is empty!")
    else:
        for item in inventory:
            inventoryNames = item + " "
        print("You have %sin your inventory." % inventoryNames)

def ta(objectName):
    """
    Adds an object to inventory.
    """
    if objectName == 'takeable item':
        # Append item to inventory list.
        print("%s was added to your inventory." % objectName.capitalize())
    else:
        print("This object can't be taken!")

def slapp(objectName):
    """
    Drops an item from inventory.
    """
    if objectName in inventory:
        # Remove item from inventory list.
    else:
        print("There is no such item in your inventory!")

def anvand(objectName):
    """
    Uses an item from inventory.
    """
    if objectName in inventory:
        if objectName == 'key0':
            print("You unlocked the door to room 2!")
        elif objectName == 'someItem':
            print("Item reaction here")
    else:
        print("There is no such item in your inventory!")

def roomSelector(room):
    """
    Prints the users current room.
    """
    if room == 0:
        print("""
                        Room 1
               __________==__________
              |                      |
              |                      |
              |                      |
              |                      |
              |  _                   |
              | |_|                  |
              |______________________|
              """)
    elif room == 1:
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
    elif room == 2:
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
    elif room == 3:
        print("""
                        Room 4
               __________==__________
              |                      |
              |                      |
              |                      |
              |                      |
              |  _                   |
              | |_|                  |
              |______________________|
              """)
    elif room == 4:
        print("""
                        Room 5
               __________==__________
              |                      |
              |                      |
              |                      |
              |                      |
              |  _                   |
              | |_|                  |
              |______________________|
              """)
    elif room == 5:
        print("""
                        Room 6
               __________==__________
              |                      |
              |                      |
              |                      |
              |                      |
              |  _                   |
              | |_|                  |
              |______________________|
              """)
    elif room == 6:
        print("""
                        Room 7
               __________==__________
              |                      |
              |                      |
              |                      |
              |                      |
              |  _                   |
              | |_|                  |
              |______________________|
              """)


def mainGame():
    """
    The main function of the game.
    """
    currentRoom = 0
    inventory = ["flower, note, umbrella"]

    print("You and your best friend Marvin suddenly woke up in a cold damp room with no way out but a big "
          "wooden door. In an attempt to escape you notice the door is locked. Marvin happens to notice "
          "a note laying on the table in the lower-left corner of the room. Maybe the note has some clues as to "
          "where you are and how you can escape? \n\nTo read the note tell Marvin 't note' or 'titta note'.")

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
            fram(currentRoom, inventory)
        elif 'fram' in command.split():
            fram(currentRoom, inventory)
        elif 'ba' in command.split():
            bak(currentRoom)
        elif 'bak' in command.split():
            bak(currentRoom)
        elif 'se' in command.split():
            se(currentRoom)
        elif 'l' in command.split():
            ledtrad(currentRoom)
        elif 'ledtråd' in command.split():
            ledtrad(currentRoom)
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
            sparka(command[7:len(sparka)])
        elif 'f ' in command:
            flytta(command[2:len(command)])
        elif 'flytta ' in command:
            flytta(command[7:len(sparka)])
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
            anvand(command[7:len(sparka)])
        else:
            print("Marvin doesn't understand you!")
    
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
