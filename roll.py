from random import randint

sides = 6
count = 1

while sides != 0:
    print "Dec's Dice Roller! Enter 0 as sides to exit!"
    sides = raw_input("Enter the Number of Sides:")
    count = raw_input("How many to roll:")
    sides = int(sides)
    n = 0
    total = 0
    while n < sides:
        roll = randint(1,sides)
        print "Roll {} was {}".format(n,roll)
        total += roll
        n += 1
    print total;

