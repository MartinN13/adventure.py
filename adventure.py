#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
An adventure game.
"""

import sys
import getopt
import ticTacToe
import requests
import random

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
        print("The third room looks exactly the same as the two before it. There is a door, hopefully "
              "leading further ahead, with a digital lock on it.")
    elif room == 3:
        print("The fourth room has a third of it cut of by a tall glass wall. The wall ends about 40 centimeters "
              "below the ceiling, leaving a gap inbetween. The area within the glass is filled with water and it "
              "seems impossible to climb over the wall as it's too high!")
    elif room == 4:
        print("The fifth room is just as uninviting as the ones before it. No windows, stone walls, it's another "
              "room that could very well be likened to a prison cell. How will you escape?")
    elif room == 5:
        print("The sixth room surprisingly has a tiny window, unfortunately it's too dark outside to see anything. "
              "Maybe it's the middle of the night?")
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

def fram(currentRoom, inventory, item=0, extraItem=0):
    """
    Move forward one room.
    """
    if currentRoom == 0 and item == 1:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    elif currentRoom == 1 and item == 1:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    elif currentRoom == 2 and item == 1:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom, inventory, item, extraItem)
    elif currentRoom == 3 and item == 1:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom, inventory)
    elif currentRoom == 4 and item == 1:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    elif currentRoom == 5 and item == 1:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    elif currentRoom == 6 and 'key7' in inventory:
        currentRoom = currentRoom + 1
        roomSelector(currentRoom)
    else:
        print("You haven't unlocked the next room yet!")

    return(currentRoom)

def bak(currentRoom, inventory, item=[], extraItem=[]):
    """
    Go back one room.
    """ 
    if currentRoom == 0:
        print("You are already in the first room!")
    elif currentRoom == 4 and item == 1:
        currentRoom = currentRoom - 1
        roomSelector(currentRoom, inventory, item, extraItem)
    else:
        currentRoom = currentRoom - 1
        if 'note' in inventory:
            roomSelector(currentRoom, inventory)
        elif 'rope' in inventory:
            roomSelector(currentRoom, inventory)
        elif 'UV-light' in inventory:
            roomSelector(currentRoom, inventory)
        elif 'modern-key' in inventory:
            roomSelector(currentRoom, inventory)
        else:
            roomSelector(currentRoom)
    return(currentRoom)

def roomSelector(currentRoom, inventory=[], item=0, extraItem=0):
    """
    Prints the users current room.
    """
    if currentRoom == 0 and 'note' in inventory:
        print("""
                        Room 1
               ______________________
              |                      |
              |                      |
              |                      |
              |                      |
              |  _                   |
              | | |                  |
              |__________==__________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 0:
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
              |     x               x|
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
    elif currentRoom == 3 and 'wet-key' in inventory or \
         currentRoom == 3 and extraItem == 1:
        print("""
                        Room 4
               __________==__________
              |       |              |
              |       |              |
              |       |              |
              |       |              |
              |       |             _|
              |       |            | |
              |_______|__==__________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 3 and 'rope' in inventory or \
         currentRoom == 3 and 'fishing-tool' in inventory:
        print("""
                        Room 4
               __________==__________
              |       |              |
              |       |              |
              |       |              |
              |    x  |              |
              |       |             _|
              |       |            | |
              |_______|__==__________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 3:
        print("""
                        Room 4
               __________==__________
              |       |              |
              |       |              |
              |       |              |
              |    x  |              |
              |       |             _|
              |       |            |x|
              |_______|__==__________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 4 and 'UV-light' in inventory:
        print("""
                        Room 5
               __________==__________
              |                      |
              |                      |
              |_                    <|
              | |                    |
              |                     <|
              |                      |
              |__________==__________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 4:
        print("""
                        Room 5
               __________==__________
              |                      |
              |                      |
              |_                    <|
              |x|                    |
              |                     <|
              |                      |
              |__________==__________|
              """)
        roomInfo(currentRoom)
    elif currentRoom == 5 and 'modern-key' in inventory:
        print("""
                        Room 6
               __________==__________
              |                      |
              |                      |
              |                      |
              |                      |   
              |                  _   |
              |                 | |  |
              |__________==__________|
              """)
    elif currentRoom == 5:
        print("""
                        Room 6
               __________==__________
              |                      |
              |                      |
              |                      |
              |                      |   
              |                  _   |
              |                 |x|  |
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

def se(room, inventory=[], item=0):
    """
    Look around the room.
    """
    if room == 0:
        if 'note' not in inventory and item == 0:
            print("Trying to escape you realize there's a locked 'padlock' on the door, requiring a four-digit passcode. "
                  "Marvin happens to notice a 'note' laying on the table in the lower-left corner of the room. "
                  "Maybe the 'note' has some clues as to where you are and how you can escape?")
        elif 'note' not in inventory and item == 1:
            print("The 'padlock' is now unlocked and the only thing left in the room is a table with a note.")
        elif 'note' in inventory and item == 0:
            print("The 'padlock' is locked and the only thing left in the room is a table.")
        else:
            print("The 'padlock' is unlocked, you've taken the 'note' and the only thing left in the room is a table.")
    elif room == 1:
        if 'rusty-key' not in inventory and item == 0:
            print("Once again the door is locked. This time there is a lock requiring a key to unlock it. "
                  "There are multiple objects laying around in the room, maybe there is something hidden?")
        elif 'rusty-key' not in inventory and item == 1:
            print("The door is unlocked and there are multiple objects laying around in the room, along with a broken vase.")
        elif 'rusty-key' in inventory and item == 0:
            print("The door is locked and there are multiple objects laying around in the room, along with a broken vase.")
        else:
            print("The door is unlocked and there are multiple objects laying around in the room.")
    elif room == 2:
        if item == 0:
            print("The next door is locked, maybe something in the room can be of help?")
        elif item == 1:
            print("The door has been unlocked and the stereo has been kicked to pieces.")
    elif room == 3:
        if 'rope' not in inventory and item == 0:
            print("The door is locked, there is a 'rope' laying in the lower right corner, and there is a 'wet-key' at the "
                  "bottom of the water on the other side of the glass! If only you could reach it...")
        elif 'rope' in inventory and item == 0:
            print("The door is locked, and there is a 'wet-key' at the bottom of the water on the other side of the glass! "
                  "If only you could each it...")
        elif 'rope' in inventory and item == 1:
            print("The door has been unlocked, and there is nothing else left in the room.")
    elif room == 4:
        if item == 0:
            print("Looking around the room you see two objects hanging on the wall, "
                  "a wooden 'closet', and a door locked with a 'padlock'")
        elif item == 1:
            print("Looking around the room you see two objects hanging on the wall, "
                  "a wooden 'closet', and an unlocked door.")
    elif room == 5:
            print("There is some kind of machine, with a box connected to it. Other than that there is a lock requiring a key.")
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
            print("Try unlocking the 'padlock' by telling Marvin 'ö padlock' or 'öppna padlock'.")
        elif clueCounter == 2:
            print("A new day starts at 00:00.")
        else:
            print("There are no more clues!")
    elif room == 1:
        if clueCounter == 0:
            print("Try looking at, moving, or kicking different objects!")
        elif clueCounter == 1:
            print("Maybe there is a key to unlock the door in one of the objects?")
        else:
            print("There are no more clues!")
    elif room == 2:
        if clueCounter == 0:
            print("Maybe something can be used from any objects laying around?")
        if clueCounter == 1:
            print("Can magnets break electric equipment?!")
        else:
            print("There are no more clues!")
    elif room == 3:
        if clueCounter == 0:
            print("If only there was a way to get the 'wet-key'...")
        elif clueCounter == 1:
            print("Maybe the 'rope' can be used?")
        elif clueCounter == 2:
            print("You need to use something to make the 'wet-key' stick to the 'rope'.")
        else:
            print("There are no more clues!")
    elif room == 4:
        if clueCounter == 0:
            print("Maybe there is something in the closet?")
        elif clueCounter == 1:
            print("Is there anything with a battery in the room?")
        elif clueCounter == 2:
            print("If only there was some note or message you could use the UV-light on...")
    elif room == 5:
        print("Clue 1 for room 6 is...")
    elif room == 6:
        print("Clue 1 for room 7 is...")

    clueCounter = clueCounter + 1
    return(clueCounter)

def objects(room, inventory=[], item=0):
    """
    Prints all items in the room.
    """
    if room == 0:
        if 'note' in inventory and item == 0:
            print("In this room there is now an empty table, along with a 'padlock' keeping the door locked.")
        elif 'note' in inventory and item == 1:
            print("In this room there is now an empty table, along with an unlocked 'padlock'.")
        elif 'note' not in inventory and item == 0:
            print("In this room there is a table with a 'note' on it, along with a 'padlock' keeping the door locked.")
        elif 'note' not in inventory and item == 1:
            print("In this room there is a table with a 'note' on it, along with an unlocked 'padlock'.")
    elif room == 1:
        if 'rusty-key' in inventory or item == 1:
            print("In this room there is a big 'crate', a shattered 'vase', and a longcase 'clock'.")
        else:
            print("In this room there is a big 'crate', a 'vase', and a longcase 'clock'.")
    elif room == 2:
        if 'magnet' in inventory and item == 0:
            print("In this room there is a broken 'stereo' and a digital 'lock' keeping the door shut.")
        elif 'magnet' in inventory and item == 1:
            print("In this room there is a broken 'stereo' and a broken digital 'lock'.")
        else:
            print("In this room there is nothing but a lone 'stereo' laying on the floor, and a digital 'lock' keeping the door shut.")
    elif room == 3:
        if 'wet-key' in inventory and item == 0:
            print("There is nothing left in the room, but the door is still locked.")
        elif 'wet-key' in inventory and item == 1 or \
             'wet-key' not in inventory and item == 1:
            print("There is nothing left in the room and the door is unlocked!")
        elif 'wet-key' not in inventory and item == 0:
            print("In this room there is a 'rope' and a 'wet-key' on the other side of the wall.")
    elif room == 4:
        print("In this room there is a 'lamp' and a 'clock' hanging on the wall, on the opposite side there is a 'closet' "
              "and finally there is a 'padlock'.")
    elif room == 5:
        print("In this room there is a 'cipher-lock' protecting something, and a normal 'lock' on the exit door.")
    elif room == 6:
        print("In room 7 there is...")

def titta(objectName, room, inventory=[], item=0):
    """
    Describes an object.
    """
    if objectName == 'note':
        if room == 0:
            if 'note' not in inventory:
                print("Reading the note it says:\n"
                      "When there is darkness, be the first to shine a light.\n"
                      "When there is injustice, be the first to condemn it.\n"
                      "When something seems difficult, do it anyway.\n"
                      "When life seems to beat you down, fight back.\n"
                      "When a new day begins, open a new door.\n"
                      "\nMaybe there is some hidden message on the note?")
            elif 'note' in inventory:
                print("Reading the note in your inventory it says:\n"
                      "When there is darkness, be the first to shine a light.\n"
                      "When there is injustice, be the first to condemn it.\n"
                      "When something seems difficult, do it anyway.\n"
                      "When life seems to beat you down, fight back.\n"
                      "When a new day begins, open a new door.\n"
                      "\nMaybe there is another hidden message to be found?")
    elif objectName == 'padlock':
        print("This is a padlock, it seems to require four digits.")
    elif objectName == 'vase' and room == 1:
        if 'rusty-key' in inventory or item == 1:
            print("A vase shattered into a million pieces.")
        else:
            print("An old vase with a checkered pattern. Maybe there is something inside it?")
    elif objectName == 'crate' and room == 1:
        print("A big sturdy crate, it doesn't seem as it will break.")
    elif objectName == 'clock' and room == 1:
        print("An old longcase clock, it seems to be broken.")
    elif objectName == 'stereo' and room == 2:
        print("A boombox-style stereo. It doesn't seem to work.")
    elif objectName == 'lock' and room == 2:
        print("A digital lock, which doesn't seem to take either a code nor a key!")
    elif objectName == 'magnet':
        print("A small magnet, taken from a speaker.")
    elif objectName == 'rope' and room == 3:
        print("A sturdy rope, about 6 meters long.")
    elif objectName == 'fishing-tool':
        print("A magnet tied to the end of a rope, effectively becoming a fishing tool.")
    elif objectName == 'wet-key' and room == 3:
        print("A wet key with water dripping from it.")
    elif objectName == 'lamp' and room == 4:
        print("A lamp hanging from the wall, it seems to be battery powered.")
    elif objectName == 'clock' and room == 4:
        print("An out of place, modern, clock is hanging on the wall.")
    elif objectName == 'closet' and room == 4:
        print("A wooden closet, it looks old.")
    elif objectName == 'UV-light':
        print("A UV flashlight, it seeems to take two batteries.")
    elif objectName == 'cipher-lock' and room == 5:
        print("A cipher lock, requiring you to solve a Caesar-cipher.")
    else:
        print("There is no such object!")

    
def oppna(objectName, room, inventory, item=[]):
    """
    Opens an object, if possible.
    """
    if objectName == 'stereo' and room == 2:
        if 'magnet' in inventory or item == 1:
            print("There is nothing else useful found from the 'stereo'")
        else:
            print("You pry open the stereo and take out the 'magnet' from its left speaker.")
            print("\n'magnet' has been added to your inventory.")
            inventory.append('magnet')
    elif objectName == 'closet' and room == 4:
        if 'UV-light' in inventory or item == 1:
            print("There is nothing else in the closet.")
        else:
            print("You open the closet and find a 'UV-light'!")
            print("\n'UV-light' has been added to your inventory.")
            inventory.append('UV-light')
            print("""
                        Room 5
               __________==__________
              |                      |
              |                      |
              |_                    <|
              | |                    |
              |                     <|
              |                      |
              |__________==__________|
              """)
    elif objectName == 'clock' and room == 4:
        if 'clock-battery' in inventory or item == 1:
            print("You open the clock one more time but there is nothing of interest.")
        else:
            print("You look behind the clock and open it up, inside there is one single AA 'clock-battery'!")
            print("\n'clock-battery' has been added to your inventory.")
            inventory.append('clock-battery')
    elif objectName == 'lamp' and room == 4:
        if 'lamp-battery' in inventory or item == 2:
            print("You open the lamp again and find nothing .")
        else:
            print("You lift the lamp off the wall and find one single AA 'lamp-battery'!")
            print("\n'lamp-battery' has been added to your inventory.")
            inventory.append('lamp-battery')
    elif objectName == 'cipher-lock' and room == 5:
        if item == 1:
            print("You check the box once again but there is nothing to be found!")
        else:
            item = decrypt()
            return(decrypt)
    else:
        print("This object doesn't exist or it can't be opened!")
    
def sparka(objectName, room, inventory=[], item=0):
    """
    Kicks an object, if possible, and breaks it.
    """
    if objectName == 'clock' and room == 1:
        print("You kick the clock and it makes a loud 'diiiinng!' noise, but nothing else happens.")
    elif objectName == 'vase' and room == 1:
        if 'rusty-key' in inventory or item == 1:
            print("The vase is already broken into a million pieces!")
        else:
            print("You kick the vase and it shatters into a million pieces! Out comes a 'rusty-key'."
                  "\n'rusty-key' has been added to your inventory.")
        inventory.append("rusty-key")
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
        if 'note' not in inventory:
            inventory.append(objectName)
            print("'%s' was added to your inventory." % objectName)
            print("""
                        Room 1
               ______________________
              |                      |
              |                      |
              |                      |
              |                      |
              |  _                   |
              | | |                  |
              |__________==__________|
              """)
        else:
            print("'note' is already in your inventory!")
    elif objectName == 'rope' and room == 3:
        if 'rope' not in inventory:
            inventory.append(objectName)
            print("'%s' was added to your inventory." % objectName)
            print("""
                        Room 4
               __________==__________
              |       |              |
              |       |              |
              |       |              |
              |    x  |              |
              |       |             _|
              |       |            |_|
              |_______|__==__________|
              """)
        else:
            print("'rope' is already in your inventory!")
    else:
        print("This object doesn't exist or it can't be taken!")

def slapp(objectName, inventory):
    """
    Drops an item from inventory.
    """
    if objectName in inventory:
        inventory.remove(objectName)
        print("'%s' was removed from your inventory." % objectName)
    else:
        print("There is no such item in your inventory!")

def anvand(objectName, inventory, room, item=0):
    """
    Uses an item from inventory.
    """
    if objectName in inventory:
        if objectName == 'rusty-key':
            if room == 1 and item == 0:
                print("You nervously put the 'rusty-key' into the lock, and it works! "
                      "\nDoor 2 has now been unlocked.")
                inventory.remove('rusty-key')
                item = 1
            elif room == 1 and item == 1:
                print("This door has already been unlocked!")
            else:
                print("This key can only be used on the door in room 2!")
        elif objectName == 'magnet':
            if room == 2 and item == 0:
                print("You hold the 'magnet' near the digital 'lock', the display flickers and the lock shuts off! "
                      "\nDoor 3 has now been unlocked.")
                item = 1
            elif room == 3 and item == 0 and 'rope' in inventory:
                print("You tie the 'magnet' onto the end of the 'rope', creating a 'fishing-tool', "
                      "maybe this can be used for something?"
                      "\n'fishing-tool' has been added to your inventory.")
                inventory.remove('magnet')
                inventory.remove('rope')
                inventory.append('fishing-tool')
            else:
                print("You take out the 'magnet', but there doesn't seem to be anything you can do with it.")
        elif objectName == 'rope':
            if room == 3:
                print("You throw the 'rope' over the wall but getting the key seems impossible.")
            else:
                print("You take out the 'rope' but there's nothing you can do with it.")
        elif objectName == 'fishing-tool':
            if room == 3:
                print("You throw your self-made 'fishing-tool' over the wall, the key sticks to it and you slowly "
                      "fish it up over the wall!"
                      "\n'wet-key' has been added to your inventory.")
                inventory.append('wet-key')
                print("""
                        Room 4
               __________==__________
              |       |              |
              |       |              |
              |       |              |
              |       |              |
              |       |             _|
              |       |            |_|
              |_______|__==__________|
              """)
            else:
                print("You swing your 'fishing-tool' around but nothing happens.")
        elif objectName == 'wet-key':
            if room == 3:
                print("You put the 'wet-key' into the lock and the door opens!"
                      "\nDoor 4 has now been unlocked.")
                inventory.remove('wet-key')
                item = 1
            else:
                print("This key can only be used on the door in room 4!")
        elif objectName == 'clock-battery':
            if 'UV-light' in inventory and item == 0:
                print("You put the 'clock-battery' into the 'UV-light'.")
                inventory.remove('clock-battery')
                item = 1
            elif 'UV-light' in inventory and item == 2:
                print("You put the 'clock-battery' into the 'UV-light', making it full.")
                inventory.remove('clock-battery')
                item = 3
            else:
                print("There is nothing to put the clock-battery in!")
        elif objectName == 'lamp-battery':
            if 'UV-light' in inventory and item == 0:
                print("You put the 'lamp-battery' into the UV-light.")
                inventory.remove('lamp-battery')
                item = 2
            elif 'UV-light' in inventory and item == 1:
                print("You put the 'lamp-battery' into the UV-light, making it full.")
                inventory.remove('lamp-battery')
                item = 3
            else:
                print("There is nothing to put the lamp-battery in!")
        elif objectName == 'UV-light':
            if item == 1 or item == 2:
                print("You turn on the 'UV-light' and it flickers for a second, then nothing happens...")
            elif item == 3 and 'note' not in inventory:
                print("The 'UV-light' turns on but there is nothing to use it on!")
            elif item == 3 and 'note' in inventory:
                print("You turn on the 'UV-light' and light it onto the 'note' in your inventory and a secret "
                      "message shows up! It says nothing but: 5987")
            else:
                print("You try to turn on the UV-light but nothing happens because there are no batteries inside of it.")
        else:
            print("This item doesn't do anything.")
    else:
        print("There is no such item in your inventory!")
    if item >= 1:
        return(item)
    else:
        return(0)

def padlock(room, padlockStatus):
    """
    Unlocks a padlock if the user inputs the right digits.
    """
    if room == 0:
        if padlockStatus == 1:
            print("This padlock is already unlocked!")
        else:
            digits = input("Please type a four-number combination: ")
            if digits == '0000':
                print("Door 1 has now been unlocked! To go to the next room type 'fr' or 'fram'.")
                padlockStatus = 1
            else:
                print("The combination didn't work! Maybe there is a clue somewhere?")
                padlockStatus = 0
    elif room == 4:
        if padlockStatus == 1:
            print("This padlock is already unlocked!")
        else:
            digits = input("Please type a four-number combination: ")
            if digits == '5987':
                print("Door 5 has now been unlocked!")
                padlockStatus = 1
            else:
                print("The combination didn't work! Maybe there is a clue somewhere?")
                padlockStatus = 0
    return(padlockStatus)

def decrypt():
    """
    Decrypt a Ceasarscipher the hard way.
    """
    url = 'https://raw.githubusercontent.com/MartinN13/adventure.py/master/words.txt'
    message = requests.get(url)


    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lettersLower = 'abcdefghijklmnopqrstuvwxyz'
    key = 1
    wordList = {}

    while key <= 25:
        translated = ""

        for char in message:
            if char in letters:
                num = letters.find(char)
                num = num + key
    
                if num >= len(letters):
                    num = num - len(letters)
                elif num < 0:
                    num = num + len(letters)
    
                translated = translated + letters[num]
            elif char in lettersLower:
                num = lettersLower.find(char)
                num = num + key
    
                if num >= len(lettersLower):
                    num = num - len(lettersLower)
                elif num < 0:
                    num = num + len(lettersLower)
    
                translated = translated + lettersLower[num]
            else:
                translated = translated + char

        wordList[key] = translated
        print("%s) %s" % (key, translated))
        key = key + 1
    choice = input("Guess the correct number: ")
    if choice == 18:
        print("You guessed right! The lock opens up and inside you find a 'modern-key'")
        inventory.append('modern-key')
        return(1)
    else:
        print("ERROR! WRONG KEY!")
        return(0)


def mainGame():
    """
    The main function of the game.
    """
    currentRoom = 0
    clueCount = 0
    padlock1 = 0
    padlock2 = 0
    rustyKey = 0
    stereoMagnet = 0
    wetKey = 0
    uvLight = 0
    decrypter = 0
    decryptLock = 0
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
            elif currentRoom == 1:
                currentRoom = fram(currentRoom, inventory, rustyKey)
            elif currentRoom == 2:
                currentRoom = fram(currentRoom, inventory, stereoMagnet, wetKey)
            elif currentRoom == 3:
                currentRoom = fram(currentRoom, inventory, wetKey)
            elif currentRoom == 4:
                currentRoom = fram(currentRoom, inventory, padlock2)
            elif currentRoom == 5:
                currentRoom = fram(currentRoom, inventory, decryptLock)
            else:
                currentRoom = fram(currentRoom, inventory)
            clueCount = 0
        elif 'ba' in command.split() or 'bak' in command.split():
            if currentRoom == 4:
                currentRoom = bak(currentRoom, inventory, wetKey, 1)
            else:
                currentRoom = bak(currentRoom, inventory)
            clueCount = 0
        elif 'se' in command.split():
            if currentRoom == 0:
                se(currentRoom, inventory, padlock1)
            elif currentRoom == 1:
                se(currentRoom, inventory, rustyKey)
            elif currentRoom == 2:
                se(currentRoom, inventory, stereoMagnet)
            elif currentRoom == 3:
                se(currentRoom, inventory, wetKey)
            elif currentRoom == 4:
                se(currentRoom, inventory, uvLight)
            else:
                se(currentRoom)
        elif 'l' in command.split() or 'ledtråd' in command.split():
            clueCount = ledtrad(currentRoom, clueCount)
        # Item commands.
        elif 'o' in command.split() or 'objekt' in command.split():
            if currentRoom == 0:
                objects(currentRoom, inventory, padlock1)
            elif currentRoom == 1:
                objects(currentRoom, inventory, rustyKey)
            elif currentRoom == 2:
                objects(currentRoom, inventory, stereoMagnet)
            elif currentRoom == 3:
                objects(currentRoom, inventory, wetKey)
            else:
                objects(currentRoom)
        elif 't ' in command:
            if currentRoom == 0:
                titta(command[2:len(command)], currentRoom, inventory)
            elif currentRoom == 1:
                titta(command[2:len(command)], currentRoom, inventory, rustyKey)
            else:
                titta(command[2:len(command)], currentRoom)
        elif 'titta ' in command:
            if currentRoom == 0:
                titta(command[6:len(command)], currentRoom, inventory)
            elif currentRoom == 1:
                titta(command[6:len(command)], currentRoom, inventory, rustyKey)
            else:
                titta(command[6:len(command)], currentRoom)
        elif 'ö ' in command:
            if 'padlock' in command and currentRoom == 0:
                padlock1 = padlock(currentRoom, padlock1)
            elif 'padlock' in command and currentRoom == 4:
                padlock2 = padlock(currentRoom, padlock2)
            elif 'stereo' in command and currentRoom == 2:
                oppna(command[2:len(command)], currentRoom, inventory, stereoMagnet)
            elif 'closet' in command and currentRoom == 4:
                oppna(command[2:len(command)], currentRoom, inventory, uvLight)
            elif 'UV-light' in command and currentRoom == 4:
                oppna(command[2:len(command)], currentRoom, inventory, uvLight)
            elif 'clock' in command and currentRoom == 4:
                oppna(command[2:len(command)], currentRoom, inventory, uvLight)
            else:
                oppna(command[2:len(command)], currentRoom, inventory)
        elif 'öppna ' in command:
            if 'padlock' in command and currentRoom == 0:
                padlock1 = padlock(currentRoom, padlock1)
            elif 'padlock' in command and currentRoom == 4:
                padlock2 = padlock(currentRoom, padlock2)
            elif 'stereo' in command and currentRoom == 2:
                oppna(command[6:len(command)], currentRoom, inventory, stereoMagnet)
            elif 'closet' in command and currentRoom == 4:
                oppna(command[6:len(command)], currentRoom, inventory, uvLight)
            elif 'UV-light' in command and currentRoom == 4:
                oppna(command[6:len(command)], currentRoom, inventory, uvLight)
            elif 'clock' in command and currentRoom == 4:
                oppna(command[6:len(command)], currentRoom, inventory, uvLight)
            else:
                oppna(command[6:len(command)], currentRoom, inventory)
        elif 's ' in command:
            if 'vase' in command and currentRoom == 1:
                sparka(command[2:len(command)], currentRoom, inventory, rustyKey)
            else:
                sparka(command[2:len(command)], currentRoom)
        elif 'sparka ' in command:
            if 'vase' in command and currentRoom == 1:
                sparka(command[7:len(command)], currentRoom, inventory, rustyKey)
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
            ta(command[3:len(command)], inventory, currentRoom)
        elif 'sl ' in command:
            slapp(command[3:len(command)], inventory)
        elif 'släpp ' in command:
            slapp(command[6:len(command)], inventory)
        elif 'a ' in command:
            if 'rusty-key' in command and currentRoom == 1:
                rustyKey = anvand(command[2:len(command)], inventory, currentRoom, rustyKey)
            elif 'magnet' in command and currentRoom == 2:
                stereoMagnet = anvand(command[2:len(command)], inventory, currentRoom, stereoMagnet)
            elif 'wet-key' in command and currentRoom == 3:
                wetKey = anvand(command[2:len(command)], inventory, currentRoom, wetKey)
            elif 'clock-battery' in command:
                uvLight = anvand(command[2:len(command)], inventory, currentRoom, uvLight)
            elif 'lamp-battery' in command:
                uvLight = anvand(command[2:len(command)], inventory, currentRoom, uvLight)
            elif 'UV-light' in command:
                uvLight = anvand(command[2:len(command)], inventory, currentRoom, uvLight)
            else:
                anvand(command[2:len(command)], inventory, currentRoom)
        elif 'använd ' in command:
            if 'rusty-key' in command and currentRoom == 1:
                rustyKey = anvand(command[7:len(command)], inventory, currentRoom, rustyKey)
            elif 'magnet' in command and currentRoom == 2:
                stereoMagnet = anvand(command[7:len(command)], inventory, currentRoom, stereoMagnet)
            elif 'wet-key' in command and currentRoom == 3:
                wetKey = anvand(command[7:len(command)], inventory, currentRoom, wetKey)
            elif 'clock-battery' in command:
                uvLight = anvand(command[7:len(command)], inventory, currentRoom, uvLight)
            elif 'lamp-battery' in command:
                uvLight = anvand(command[7:len(command)], inventory, currentRoom, uvLight)
            elif 'UV-light' in command:
                uvLight = anvand(command[7:len(command)], inventory, currentRoom, uvLight)
            else:
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
