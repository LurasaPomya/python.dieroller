import os
import diefunctions

while True:
    os.system('clear')
    print "Dec's Dice Roller! Please choose:"
    print "1. Enter sides and count manually."
    print "2. Roll Skill Check."
    print "===================================="
    print "0. Exit App"

    selection = raw_input("Select: ")
    selection = int(selection)

    if selection == 0:
        break
    elif selection == 1:
        s = raw_input("How many sides: ")
        c = raw_input("How many to roll: ")
        diefunctions.roll(s,c)
    elif selection == 2:
        m = raw_input("Modofier to roll(w/o Prof): ")
        p = raw_input("Prof. Modifier: ")
        diefunctions.skillCheck(m,p)
    else:
        print "Invalid Selection!"


