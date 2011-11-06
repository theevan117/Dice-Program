
import random

from random import randint

# repeating loop
while True:

	dice = int(input('What dice do you want to roll? '))
	
	# break conditions
	if dice < 0:
		print 'Dice value not valid, exiting....'
		break
		
	
	# dice rolling protocol
	print 'You chose d' + str(dice)
	
	print randint(1, dice)
	
	

