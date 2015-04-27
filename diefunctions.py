from random import randint

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
