from random import randint
import os

def roll(sides,count):
    sides = int(sides)
    count = int(count)
    n = 0
    total = 0

    while n < count:
        roll = randint(1,sides)
        print "Roll {} was {}".format(n + 1,roll)
        total += roll
        n += 1
    print "Total: {}".format(total)
    raw_input("Press Enter to return to menu...")
    return

def skillCheck(modifier,prof):
    modifier = int(modifier)
    prof = int(prof)

    if prof != 0:
        modifier += prof

    roll = randint(1,20)
    if roll == 20:
        print "Critical Success! Modified Roll: {}".format(roll + modifier)
    elif roll == 1:
        print "Critical Failure! Modified Roll: {}".format(roll + modifier)
    else:
        print "Rolled {}, Modified to {}".format(roll,roll + modifier)
    raw_input("Press Enter to return to the menu...")
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
        roll(s,c)
    elif selection == 2:
        m = raw_input("Modofier to roll(w/o Prof): ")
        p = raw_input("Prof. Modifier: ")
        skillCheck(m,p)
    else:
        print "Invalid Selection!"


