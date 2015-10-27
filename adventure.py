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
	print("Game description here.")

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
	print("My name is Martin.")

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

def fram(room, inventory):
	"""
	Move forward one room.
	"""
	if room == 0 and key0 in inventory:
		currentRoom = room + 1
	elif room == 1 and key1 in inventory:
		currentRoom = room + 1
	elif room == 2 and key2 in inventory:
		currentRoom = room + 1
	elif room == 3 and key3 in inventory:
		currentRoom = room + 1
	elif room == 4 and key4 in inventory:
		currentRoom = room + 1
	elif room == 5 and key5 in inventory:
		currentRoom = room + 1
	elif room == 6 and key6 in inventory:
		currentRoom = room + 1
	else:
		print("You haven't unlocked the next room yet!")

def bak(room):
	"""
	Go back one room.
	"""
	if room == 0:
		print("You are already in the first room!")
	else:
		currentRoom = room + 1

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
		print("In this room there is a table, with a note on it.")
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
	if objectName == note:
		print("This is a note")
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

	
def oppna(objectName):
	"""
	Opens an object, if possible.
	"""
	if objectName == 'someObject':
		print("Open result here")
	elif objectName == 'someObject':
		print("Open result here")
	else:
		print("This object can't be opened.")
	
def sparka(objectName):
	"""
	Kicks an object, if possible, and breaks it.
	"""
	if objectName == 'someObject':
		print("Kick result here")
	elif objectName == 'someObject':
		print("Kick result here")
	else:
		print("This object can't be kicked.")
	
def flytta(objectName):
	"""
	Moves an object, if possible.
	"""
	if objectName == 'someObject':
		print("Move result here")
	elif objectName == 'someObject':
		print("Move result here")
	else:
		print("This object can't be moved.")

def inventoryList():
	"""
	Prints the players inventory.
	"""

def ta(objectName):
	"""
	Adds an object to inventory.
	"""

def slapp(objectName):
	"""
	Drops an item from inventory.
	"""

def anvand(objectName):
	"""
	Uses an item from inventory.
	"""

def mainGame():
	"""
	The main function of the game.
	"""
	currentRoom = 0

	print("""
		  You and your best friend Marvin suddenly woke up in a cold damp room with no way out but a big
		  wooden door. In an attempt to escape you notice the door is locked. Marvin happens to notice
		  a note laying on the table in the lower-left corner of the room. Maybe the note has some clues as to
		  where you are and how you can escape? To read the note tell Marvin 'titta note'.
		  """)

	input("\nPress enter to continue...")

	print("""
		   __________==__________
		  |						 |
		  |						 |
		  |						 |
		  |						 |
		  |	 _					 |
		  |	|_|					 |
		  |______________________|

		  """)

	while True:
		command = input("\nTell Marvin what you want to do: ")

		# Room commands
		if 'i' in command:
			roomInfo()
		elif 'info' in command:
			roomInfo()
		elif 'h' in command:
			hjalp()
		elif 'hjalp' in command:
			hjalp()
		elif 'fr' in command:
			fram()
		elif 'fram' in command:
			fram()
		elif 'ba' in command:
			bak()
		elif 'bak' in command:
			bak()
		elif 'se' in command:
			se()
		elif 'l' in command:
			ledtrad()
		elif 'ledtråd' in command:
			ledtrad()
		# Item commands
		elif 'o' in command:
			objects(command[2:len(command)])
		elif 'objekt' in command:
			objects(command[7:len(sparka)])
		elif 't' in command:
			titta(command[2:len(command)])
		elif 'titta' in command:
			titta(command[6:len(command)])
		elif 'ö' in command:
			oppna(command[2:len(command)])
		elif 'öppna' in command:
			oppna(command[6:len(command)])
		elif 's' in command:
			sparka(command[2:len(command)])
		elif 'sparka' in command:
			sparka(command[7:len(sparka)])
		elif 'f' in command:
			flytta(command[2:len(command)])
		elif 'flytta' in command:
			flytta(command[7:len(sparka)])
		elif 'inv' in command:
			inventoryList()
		elif 'inventarier' in command:
			inventoryList()
		elif 'ta' in command:
			ta(command[3:len(command)])
		elif 'sl' in command:
			slapp(command[3:len(command)])
		elif 'släpp' in command:
			slapp(command[6:len(command)])
		elif 'a' in command:
			anvand(command[2:len(command)])
		elif 'använd' in command:
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
