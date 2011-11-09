######################################
import random

from random import randint
######################################

dice_history = []

# dice protocol loop
while True:

	# declaration of status var
	status = raw_input('Do you want to roll the dice? y/n ')
	
	# conditions in which the loop continues
	if status == 'Y' or status == 'y' :
		print 'Okay!'
		
	else:
		break
		
	# declaration of dice and dice_value vars
	dice = int(input('What dice do you want to roll? '))
	dice_value = randint(1, dice)
	
	# invalid dice choice
	if dice <= 0:
		print 'Dice value not valid, exiting....'
		break
		
	# dice rolling and value storage protocol
	print 'You chose d' + str(dice)
	print dice_value
	dice_history.append(dice_value)
	
# declaration of what_do var	
what_do = raw_input('Would you like to check your dice rolling history? y/n ')
	
# display of dice_history var
if what_do == "y" or what_do == "Y":
	print dice_history

