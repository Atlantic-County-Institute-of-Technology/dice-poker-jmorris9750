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


class Dice:

    def __init__(self):
        self.max_dice = 5
        self.dice = []
        self.keep = []
        self.kept_display = []
        self.make_die_list()
        # self.show()
        # self.check_dice()
        # self.roll()

    def make_die_list(self):
        for die in range(self.max_dice):
            self.dice.append(Die())
            self.keep.append(True)
            self.kept_display.append(f"{self.dice[die]}: Not Kept")
        return self.dice, self.keep, self.kept_display

    def get_die_list(self):
        self.dice = self.dice
        return self.dice

    def get_keep_list(self):
        self.keep = self.keep
        return self.keep

    def get_kept_display(self):
        self.kept_display = self.kept_display
        return self.kept_display

    # def show(self):
    #     out_string = ""
    #     for die in range(len(self.dice)):
    #         out_string += f"Die #{die + 1}: {self.dice[die]}\n"
    #     out_string += f"Kept dice:{self.kept_display}"
    #     return out_string

    # def __str__(self):
    #     self.show()
    #     return self.show()


class DieHandler:

    def __init__(self):
        self.keep_ans = ""
        self.keep = Dice.get_keep_list(Dice())
        self.kept_display = Dice.get_kept_display(Dice())
        self.dice = Dice.get_die_list(Dice())

    def check_dice(self, keep_ans):
        self.keep_ans = keep_ans
        if self.keep[int(self.keep_ans) - 1] is False:
            self.keep[int(self.keep_ans) - 1] = True
            self.kept_display[int(self.keep_ans) - 1] = f"{self.dice[int(self.keep_ans) - 1]} Not Kept"
        else:
            self.keep[int(self.keep_ans) - 1] = False
            self.kept_display[int(self.keep_ans) - 1] = f"{self.dice[int(self.keep_ans) - 1]} Kept"
        return self.keep, self.kept_display

    def roll(self):
        for die in range(len(self.dice)):
            if self.keep[die] is True:
                self.dice[die].roll()

    def show(self):
        out_string = ""
        for die in range(len(self.dice)):
            out_string += f"Die #{die + 1}: {self.dice[die]}\n"
        out_string += f"Kept dice:{self.kept_display}"
        return out_string

    def __str__(self):
        out_string = f"{self.show()}"
        return out_string
