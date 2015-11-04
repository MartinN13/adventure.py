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
          "Marvin waking up in a mysterious castle and having to solve various problems to escape this cold, damp place.\n")

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
          "currently studying web-programming. I hope you'll enjoy this game!\n")

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
        print("A cold, stone-tiled room looking as if it belongs to an old medieval castle presents itself in front of you. "
              "There are no windows and there seems to be no other way to escape but through the main door.")
    elif room == 1:
        print("Another stone-tiled room. There are no windows and a single door leading further ahead. "
              "Hopefully you can find something useful! Maybe looking around the room could help...")
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
a [object], använd [object] - Uses [object], if possible.""")

def fram(currentRoom, inventory, padlock=0):
    """
    Move forward one room.
    """
    if currentRoom == 0 and padlock == 1:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    elif currentRoom == 1 and 'rusty key' in inventory:
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
        print("You haven't unlocked the next room yet!")

    return(currentRoom)

def bak(currentRoom):
    """
    Go back one room.
    """ 
    if currentRoom == 0:
        print("You are already in the first room!")
    else:
        currentRoom = currentRoom - 1
        roomSelector(currentRoom)
    return(currentRoom)

def se(room):
    """
    Look around the room.
    """
    if room == 0:
        print("Trying to escape you realize there's a locked padlock on the door, requiring a four-digit passcode. "
              "Marvin happens to notice a note laying on the table in the lower-left corner of the room. "
              "Maybe the note has some clues as to where you are and how you can escape?")
    elif room == 1:
        print("Once again the door is locked. This time there is a lock requiring a key to unlock it. "
              "There are multiple objects laying around in the room, maybe there is something hidden?")
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
            print("To take a look around the room tell Marvin 'se'.")
        elif clueCounter == 1:
            print("Try unlocking the padlock by telling Marvin 'ö padlock' or 'öppna padlock'.")
        elif clueCounter == 2:
            print("A new day starts at 00:00.")
        else:
            print("There are no more clues!")
    elif room == 1:
        if clueCounter == 0:
            print("Try looking at, moving, or kicking different objects!")
        elif clueCounter == 1:
            print("Maybe there is a key to unlock the door somewhere?")
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
        print("In this room there is a table with a 'note' on it, along with a 'padlock' keeping the door locked.")
    elif room == 1:
        print("In this room there is a big 'crate', a 'vase', and a longcase 'clock'.")
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

def titta(objectName, room):
    """
    Describes an object.
    """
    if objectName == 'note' and room == 0:
        print("Reading the note it says:\n"
              "When there is darkness, be the first to shine a light.\n"
              "When there is injustice, be the first to condemn it.\n"
              "When something seems difficult, do it anyway.\n"
              "When life seems to beat you down, fight back.\n"
              "When a new day begins, open a new door.")
    elif objectName == 'padlock' and room == 0:
        print("This is a padlock, it seems to require four digits.")
    elif objectName == 'vase' and room == 1:
        print("An old vase with a checkered pattern. Maybe there is something inside it?")
    elif objectName == 'crate' and room == 1:
        print("A big study crate, it doesn't seem as it will break.")
    elif objectName == 'clock' and room == 1:
        print("An old longcase clock, it seems to be broken.")
    elif objectName == 'someObject':
        print("This is...")
    elif objectName == 'someObject':
        print("This is...")
    else:
        print("There is no such object!")

    
def oppna(objectName, room):
    """
    Opens an object, if possible.
    """
    if objectName == 'someObject' and room == 0:
        print("Open result here")
    elif objectName == 'someObject' and room == 0:
        print("Open result here")
    else:
        print("This object doesn't exist or it can't be opened!")
    
def sparka(objectName, room, inventory=[]):
    """
    Kicks an object, if possible, and breaks it.
    """
    if objectName == 'clock' and room == 1:
        print("You kick the clock and it makes a loud 'diiiinng!' noise, but nothing else happens.")
    elif objectName == 'vase' and room == 1:
        if 'rusty key' in inventory:
            print("You kick the vase again but nothing happens!")
        else:
            print("You kick the vase and it shatters into a million pieces! Out comes a 'rusty key'."
              "\n'rusty key' has been added to your inventory.")
        inventory.append("rusty key")
    else:
        print("This object doesn't exist or it can't be kicked!")
    
def flytta(objectName, room):
    """
    Moves an object, if possible.
    """
    if objectName == 'crate' and room == 1:
        print("You move the crate, but there is nothing under it!")
    elif objectName == 'someObject' and room == 0:
        print("Move result here")
    else:
        print("This object doesn't exist or it can't be moved!")

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
            inventoryNames = inventoryNames + item + " "
        print("Your inventory contains: \n%s" % inventoryNames)

def ta(objectName, inventory, room):
    """
    Adds an object to inventory.
    """
    if objectName == 'note' and room == 0:
        inventory.append(objectName)
        print("%s was added to your inventory." % objectName)
    else:
        print("This object doesn't exist or it can't be taken!")

def slapp(objectName, inventory):
    """
    Drops an item from inventory.
    """
    if objectName in inventory:
        inventory.remove(objectName)
        print("%s was removed from your inventory." % objectName)
    else:
        print("There is no such item in your inventory!")

def anvand(objectName, inventory, room, rustyKey=0):
    """
    Uses an item from inventory.
    """
    if objectName in inventory:
        if objectName == 'rusty key':
            if room == 1 and rustyKey == 0:
                print("You nervously put the 'myserious key' into the lock, and it works! "
                      "Open the door by telling Marvin 'fr' or 'fram'.")
                inventory.remove('rusty key')
                rustyKey = 1
            elif room == 1 and rustyKey == 1:
                print("This door has already been unlocked!")
            else:
                print("This key can only be used on the door in room 2!")
        elif objectName == 'someItem':
            print("Item reaction here")
        else:
            print("This item doesn't do anything.")
    else:
        print("There is no such item in your inventory!")
    if rustyKey == 1:
        return(rustyKey)

def padlock(room, padlockStatus):
    """
    Unlocks a padlock if the user inputs the right digits.
    """
    if padlockStatus == 1:
        print("This padlock is already unlocked!")
    elif room == 0:
        digits = input("Please type a four-number combination: ")
        if digits == '0000':
            print("The door has been unlocked! To go to the next room type 'fr' or 'fram'.")
            padlockStatus = 1
        else:
            print("The combination didn't work! Maybe there is a clue somewhere?")
            padlockStatus = 0

    return(padlockStatus)

def roomSelector(currentRoom):
    """
    Prints the users current room.
    """
    if currentRoom == 0:
        print("""
                        Room 1
               ______________________
              |                      |
              |                      |
              |                      |
              |                      |
              |  _                   |
              | |x|                  |
              |__________==__________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 1:
        print("""
                        Room 2
               __________==__________
              |                      |
              |   x                  |
              |                      |
              |                      |
              |     x           x    |
              |                      |
              |__________==__________|
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
              |  x                   |
              |                      |
              |__________==__________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 3:
        print("""
                        Room 4
               __________==__________
              |       |              |
              |       |              |
              |       |      fishing |
              |    x  |              |
              |       |             _|
              |       |            |_|
              |_______|__==__________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 4:
        print("""
                        Room 5
               __________==__________
              |                      |
              |                      |
              |_                    <|
              |_|     UV-Light       |
              |                     <|
              |                      |
              |__________==__________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 5:
        print("""
                        Room 6
               __________==__________
              |                      |
              |                      |
              |                      |
              |  Schiffer            |   
              |                  _   |
              |                 |_|  |
              |__________==__________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 6:
        print("""
                        Room 7
               __________==__________
              |                      |
              |     _                |
              |    | |               |
              |    |x|    ticTacToe  |
              |    |_|               |
              |                      |
              |_________====_________|
              """)
        roomInfo(currentRoom)


def mainGame():
    """
    The main function of the game.
    """
    currentRoom = 0
    clueCount = 0
    padlock1 = 0
    padlock5 = 0
    rustyKey = 0
    inventory = []

    print("\nWelcome to this mysterious adventure! Tell Marvin 'h' or 'hjälp' to get a list of all available commands. "
          "Whenever you get into a new room it might be useful to use the 'se' command to look around. If you get stuck "
          "don't forget you can always get a hint with 'l' or 'ledtråd'."
          "\n\nYou and a stranger named Marvin suddenly wake up in a cold, damp room. "
          "Where are you and how will you escape? Maybe there is something in the room you can use?")

    input("\nPress enter to continue...")

    roomSelector(currentRoom)

    while True:
        command = input("\nTell Marvin what you want to do: ")
        print("\n")
        # Room commands.
        if 'i' in command.split() or 'info' in command.split():
            roomInfo(currentRoom)
        elif 'h' in command.split() or 'hjälp' in command.split():
            hjalp()
        elif 'fr' in command.split() or 'fram' in command.split():
            if currentRoom == 0:
                currentRoom = fram(currentRoom, inventory, padlock1)
            else:
                currentRoom = fram(currentRoom, inventory)
            clueCount = 0
        elif 'ba' in command.split() or 'bak' in command.split():
            currentRoom = bak(currentRoom)
            clueCount = 0
        elif 'se' in command.split():
            se(currentRoom)
        elif 'l' in command.split() or 'ledtråd' in command.split():
            clueCount = ledtrad(currentRoom, clueCount)
        # Item commands.
        elif 'o' in command.split() or 'objekt' in command.split():
            objects(currentRoom)
        elif 't ' in command:
            titta(command[2:len(command)], currentRoom)
        elif 'titta ' in command:
            titta(command[6:len(command)], currentRoom)
        elif 'ö ' in command:
            if 'padlock' in command and currentRoom == 0:
                padlock1 = padlock(currentRoom, padlock1)
            elif 'padlock' in command and currentRoom == 4:
                padlock5 = padlock(currentRoom, padlock5)
            else:
                oppna(command[2:len(command)], currentRoom)
        elif 'öppna ' in command:
            if 'padlock' in command and currentRoom == 0:
                padlock1 = padlock(currentRoom, padlock1)
            elif 'padlock' in command and currentRoom == 4:
                padlock5 = padlock(currentRoom, padlock5)
            else:
                oppna(command[6:len(command)], currentRoom)
        elif 's ' in command:
            if 'vase' in command and currentRoom == 1:
                sparka(command[2:len(command)], currentRoom, inventory)
            else:
                sparka(command[2:len(command)], currentRoom)
        elif 'sparka ' in command:
            if 'vase' in command and currentRoom == 1:
                sparka(command[7:len(command)], currentRoom, inventory)
            else:
                sparka(command[7:len(command)], currentRoom)
        elif 'f ' in command:
            flytta(command[2:len(command)], currentRoom)
        elif 'flytta ' in command:
            flytta(command[7:len(command)], currentRoom)
        # Inventory commands.
        elif 'inv' in command.split() or 'inventarier' in command.split():
            inventoryList(inventory)
        elif 'ta ' in command:
            ta(command[3:len(command)], currentRoom)
        elif 'sl ' in command:
            slapp(command[3:len(command)])
        elif 'släpp ' in command:
            slapp(command[6:len(command)])
        elif 'a ' in command:
            if 'rusty key' in command and currentRoom == 1:
                rustyKey = anvand(command[2:len(command)], inventory, currentRoom, rustyKey)
            else:
                anvand(command[2:len(command)], inventory, currentRoom)
            if 'rusty key' in command and currentRoom == 1:
                rustyKey = anvand(command[2:len(command)], inventory, currentRoom, rustyKey)
            else:
                anvand(command[2:len(command)], inventory, currentRoom)
        elif 'använd ' in command:
            anvand(command[7:len(command)], inventory, currentRoom)
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
