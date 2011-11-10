######################################
import random
import sys

from random import randint
######################################

# dictionary for dice_value history storage
dice_history = {}


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
	
	
# declaration of dice_history_choice
dice_history_choice = raw_input('Would you like to check your dice rolling history? y/n ')

# display of dice_history, sorted by dice_choice
if dice_history_choice == 'y':
	
	for dice_choice in sorted(dice_history.keys()):
		dice_record = "{0}: {1}".format(dice_choice, dice_history[dice_choice])
		print dice_record

# declaration of dice_info_choice
dice_info_choice = raw_input('Would you like some additional information about your dice-rolling statistics? y/n ')

# display of dice_info, only includes average dice_value for each dice_choice for now
if dice_info_choice == 'y':
	for dice_choice in sorted(dice_history.keys()):
		dice_average = sum(dice_history[dice_choice]) /  float(len(dice_history[dice_choice]))
		dice_average_output = "{0}: {1}".format(dice_choice, dice_average)
		print dice_average_output

# end of script
else:
	print "Goodbye!"
	sys.exit(0)
