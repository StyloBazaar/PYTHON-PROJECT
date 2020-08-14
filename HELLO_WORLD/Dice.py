import random


class Dice:
    def __init__(self):
        self.dice_roll = 0

    def roll(self):
        self.dice_roll = random.randint(1, 6)
        return self.dice_roll


dice1 = Dice()
# num
roll_1 = dice1.roll()
roll_2 = dice1.roll()
roll_set = (roll_1, roll_2)
print(roll_set)





