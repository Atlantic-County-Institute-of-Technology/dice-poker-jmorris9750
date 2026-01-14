import random


class Die:
    def __init__(self):
        self.max = 6
        self.roll()
        self.get_value()

    def roll(self):
        self.value = random.randint(1, self.max)
        return self.value

    def get_value(self):
        return self.value

    def __str__(self):
        out_string = f"{self.value}"
        return out_string


class DieHandler:

    def __init__(self):
        self.max_dice = 5
        self.dice =[]
        self.keep =[]

        for die in range(self.max_dice):
            self.dice.append(Die())
            self.keep.append(True)

    # def roll_dice(self):
    #     for die in range(self.max_dice):
    #         self.dice[die].roll()
    #         return self.dice

    def __str__(self):
        out_string = f"{self.dice}"
        return out_string


print(Die(), DieHandler())