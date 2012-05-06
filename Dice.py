######################################
#
# Evan W. Muller
# theevan117@gmail.com
#
######################################
import kivy
import random
import sys

from kivy.app import App
from kivy.uix.widget import Widget
from random import randint
######################################

# dictionary for dice_value history storage
dice_history = {}

# list of possible choices for stat_choice var
stat_choice_list = ['average die rolls', 'highest die rolls', 'lowest die rolls']

# dice protocol loop
while True:

        # declaration of status var
        status = raw_input('Do you want to roll the dice? y/n ')

        # conditions in which the loop continues
        if status == 'Y' or status == 'y' :
                print 'Okay!'

        else:
                break

        # declaration of dice_choice and dice_value vars
        dice_choice = int(input('What dice do you want to roll? '))
        dice_value = randint(1, dice_choice)

        # invalid dice choice
        if dice_choice <= 0:
                print 'Dice value not valid, exiting....'
                break

        # dice rolling and value storage protocol
        print 'You chose d' + str(dice_choice)
        print dice_value

        # storage protocol for dice_value
        if not dice_choice in dice_history:
                dice_history[dice_choice] = []

        dice_history[dice_choice].append(dice_value)

# declaration of choice var
choice = raw_input('Would you like to do anything else? y/n ')

# exits program if user is done
if choice == 'n':
        print "Goodbye!"
        sys.exit(0)

# declaration of dice_history_choice
dice_history_choice = raw_input('Would you like to check your dice rolling history? y/n ')

# display of dice_history, sorted by dice_choice
if dice_history_choice == 'y':

        for dice_choice in sorted(dice_history.keys()):
                dice_record = "{0}: {1}".format(dice_choice, dice_history[dice_choice])
                print dice_record

# declaration of dice_info_choice
dice_info_choice = raw_input('Would you like some additional information about your dice-rolling statistics? y/n ')
for option in stat_choice_list:
        print option

# loop for stat analysis

while True:
        stat_choice = raw_input('Which stat would you like to see more information about? ')

        # display of dice_average_output
        if stat_choice == 'average die rolls' or stat_choice == 'average' or stat_choice == 'average rolls':
                for dice_choice in sorted(dice_history.keys()):
                        dice_average = sum(dice_history[dice_choice]) /  float(len(dice_history[dice_choice]))
                        dice_average_output = "{0}: {1}".format(dice_choice, dice_average)
                        print dice_average_output

        # display of dice_highest_output
        if stat_choice == 'highest' or stat_choice == 'highest roll' or stat_choice == 'highest rolls':
                for dice_choice in sorted(dice_history.keys()):
                        dice_highest = max(dice_history[dice_choice])
                        dice_highest_output = "{0}: {1}".format(dice_choice, dice_highest)
                        print dice_highest_output

        # display of dice_lowest_output
        if stat_choice == 'lowest' or stat_choice == 'lowest roll' or stat_choice == 'lowest rolls':
                for dice_choice in sorted(dice_history.keys()):
                        dice_lowest = min(dice_history[dice_choice])
                        dice_lowest_output = "{0}: {1}".format(dice_choice, dice_lowest)
                        print dice_lowest_output

        # loop break condition
        if stat_choice == 'none' or stat_choice == 'n':
                break

# end of script
print "Goodbye!"
