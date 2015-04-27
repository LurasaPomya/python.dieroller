import os
import diefunctions

def wfi():
    raw_input("Press Enter to Continue...")
    return

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
        results = diefunctions.roll(s,c)
        rolls = results[0]
        total = results[1]
        c = 1
        for roll in rolls:
            print "Roll {} was {}".format(c,roll)
            c += 1
        print "Total was: {}".format(total)
        wfi()
    elif selection == 2:
        m = raw_input("Modofier to roll(w/o Prof): ")
        p = raw_input("Prof. Modifier: ")
        results = diefunctions.skillCheck(m,p)
        if results[0] == 20:
            print "Critical Success!"
        elif results[0] == 1:
            print "Critical Failure!"
        else:
            print "You rolled {}! Modded to {}".format(results[0],results[1])
            wfi()
    else:
        print "Invalid Selection!"


