######################################
import random

from random import randint
######################################


# dice protocol loop
while True:

	# declaration of status var
	status = raw_input('Do you want to roll the dice? ')
	
	# conditions in which the loop continues
	if status == 'yes' or status == 'y' or status == 'Yes' or status == 'Yeah' or status == 'yeah':
		print 'Okay!'
		
	else:
		break
		
	# declaration of dice var
	dice = int(input('What dice do you want to roll? '))
	
	# invalid dice choice
	if dice <= 0:
		print 'Dice value not valid, exiting....'
		break
		
	# dice rolling protocol
	print 'You chose d' + str(dice)
	print randint(1, dice)
	
# what_do = raw_input('Would you like to check your dice rolling history? ')

