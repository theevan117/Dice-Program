######################################
import random

from random import randint
######################################


# repeating loop
while True:

	# status of what user wants to do
	status = raw_input('Do you want to roll the dice? ')
	
	# status condition to leave loop and do something other than roll dice
	if status == 'no':
		break
	else:
		print 'Okay!'
	
	# declaration of dice var
	dice = int(input('What dice do you want to roll? '))
	
	# invalid dice choice
	if dice <= 0:
		print 'Dice value not valid, exiting....'
		break
		
	# dice rolling protocol
	print 'You chose d' + str(dice)
	print randint(1, dice)
	
	

