from random import randint

def roll(sides,count):
    sides = int(sides)
    count = int(count)
    n = 0
    total = 0

    results = []
    while n < count:
        roll = randint(1,sides)
        results.append(roll)
        total += roll
        n += 1
    return (results,total)
def skillCheck(modifier,prof):
    modifier = int(modifier)
    prof = int(prof)
    if prof != 0:
        modifier += prof
    
    roll = randint(1,20)
    modroll = roll + modifier
    return (roll, modroll)
