#!/usr/bin/env python3
import sys
sys.path.append('service')
from service import *
from controller.titles import *

#maybe make global variables??

def startBank():
	#or variables in here for the session the user is currently in so we can show transactions and balance, etc.
	welcomeTitle()
	loopStart = True
	while loopStart == True:
		x = startUp()
		if x == 1:
			registerTitle()
			register()
			welcomeTitle()
		elif x == 2:
			loginTitle()
			login()
			menuTitle()
			loopMenu = True
			while loopMenu == True:
				m = menuOptions()
				if m == 1:
					balanceTitle()
					b = balance()
					loopBalance = True
					while loopBalance == True:
						mo = money()
						if mo == 2:
							depositTitle()	
							deposit()
							#transaction()
							back()
							balanceTitle()
							balance()
						elif mo == 3:
							withdrawTitle()
							withdraw()
							
							#transaction()
							back()
							balanceTitle()
							balance()
						elif mo == 1:
							loopBalance = False
							menuTitle()
				elif m == 2:
					transactions()
					print('Type back to return to menu')
					back()
					menuTitle()
				elif m == 3:
					loopMenu = False
					welcomeTitle()
		elif x == 3:
			sys.exit()
