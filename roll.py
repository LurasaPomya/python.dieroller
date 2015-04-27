from random import randint

sides = 6
count = 1

while True:
    print "Dec's Dice Roller! Enter 0 as sides to exit!"
    sides = raw_input("Enter the Number of Sides:")
    sides = int(sides)
    #Checks to see if we should break and stop asking
    if int(sides) == 0:
        break
    count = raw_input("How many to roll:")
    count = int(count)
    
    n = 0
    total = 0
    while n < count:
        roll = randint(1,sides)
        print "Roll {} was {}".format(n + 1,roll)
        total += roll
        n += 1
    print total;

