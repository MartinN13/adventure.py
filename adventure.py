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

def mainGame():
	"""
	The main function of the game.
	"""
	print("Game started")
	
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
