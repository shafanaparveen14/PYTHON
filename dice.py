import random

def roll():
    return random.randint(1,6)
dice_roll=roll()
print("You Rolled dice",dice_roll)
for i in range(5):
    print("roll",i+1,":",roll())
