#coding=utf-8
__author__ = 'ron975'
"""
This file is part of Snowflake.Core
"""

import colorama.initialise
import ctypes

def main():
    ctypes.windll.kernel32.SetConsoleTitleA("Testing 1 2 3")
    print "Welcome to Snowflake"
    print "Mode 1 or 2"
    mode = raw_input()
    if mode is "1":
        print "Getting Consoles"
        print "Consoles:"
        print "- SNES"
        print "- NES"
        print "Select Console"
        console = raw_input()
        print "You selected", console
        print "Games for this console"
        if console == "SNES":
            print "Super Mario World"
            print "Super Mario Kart"
            print "Super Mario Crush Saga"
        elif console == "NES":
            print "Battletoads"
            print "More Battletoads"
            print "Ninja Gaiden"
        else:
            print "Invalid Choice"
            return
    elif mode is "2":
        print "Getting Consoles"
        print "Consoles are SNES and NES"
        print "Games:"
        print "SNES"
        print "===="
        print "Super Mario World"
        print "Super Mario Kart"
        print "Super Mario Crush Saga"
        print "NES"
        print "==="
        print "Battletoads"
        print "More Battletoads"
        print "Ninja Gaiden"

if __name__ == "__main__":
    main()