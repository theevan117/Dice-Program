######################################
import random

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
	
	
# declaration of what_do and  var	
what_do = raw_input('Would you like to check your dice rolling history? y/n ')


# display of dice_record
for dice_choice in sorted(dice_history.keys()):
	dice_record = "{0}: {1}".format(dice_choice, dice_history[dice_choice])
	print dice_record
