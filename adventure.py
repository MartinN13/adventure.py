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

def info(room):
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

def se():
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

def ledtrad():
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

def mainGame():
	"""
	The main function of the game.
	"""
	currentRoom = 0

	print("""
		  You and your best friend Marvin suddenly woke up in a cold damp room with no way out but a big
		  wooden door. In an attempt to escape you notice the door is locked. Marvin happens to notice
		  a note laying on the table in the lower-left corner of the room. Maybe the note has some clues as to
		  where you are and how you can escape?
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
