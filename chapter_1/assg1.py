# Assignment 1: The below program is to Roll the Dice
import random

def roll_dice(number_of_sides: int) -> int:
    return random.randint(1, number_of_sides)

def start_dice_roller():
    dice_sides = 6
    keep_rolling = True

    while keep_rolling:
        user_choice = input("Roll the dice? Press Enter to continue or Q to Quit: ")

        if user_choice.lower() != "q":
            rolled_value = roll_dice(dice_sides)
            print("You rolled:", rolled_value)
        else:
            keep_rolling = False

start_dice_roller()