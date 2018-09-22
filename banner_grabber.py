#!/usr/bin/python

# Performs banner grabbing through an interactive text prompt

import urllib2
import sys
import os

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def continue_program():
    next = raw_input("Continue?...[Y/n] ")
    if next.lower() == 'n':
        sys.exit()

# Program Body
clear_screen()
response = raw_input("Would you like to perform a banner grab? [Y/n]  ")
if response.lower() == 'n':
    print("See yah next time...")
    sys.exit()
elif response.lower() == 'y':
    while True:
        clear_screen()
        try:
            # Prompt user to enter the full URL
            url = raw_input("Type the full URL: ")
            url.rstrip()

            # Header is displayed on screen showing teh webserver version
            header = urllib2.urlopen(url).info()

            print("\n" + str(header))
            continue_program()            
        except ValueError, e:
            print("\n* Error: " + str(e))
            print("* Correctly formmated URL: 'http://google.com'.\n")
            continue_program()
           
