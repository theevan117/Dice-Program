
import random

from random import randint

dice = 1

# repeating loop
while True:

	dice = int(input('What dice do you want to roll? '))
	
	# break conditions
	if dice < 0:
		print 'blarp'
		break
		
	
	# dice rolling protocol
	print 'You chose d' + str(dice)
	
	print randint(1, dice)
	
	

