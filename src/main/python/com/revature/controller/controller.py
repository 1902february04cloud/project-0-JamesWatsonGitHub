#!/usr/bin/env python3

#James Watson
#Project 0 
#2/19/2019

#imports
import sys
sys.path.append('service')
from service import *
from controller.titles import *

#starting function called in main
def startBank():
	welcomeTitle()
	loopStart = True
	#loop over the application
	while loopStart == True:
		#call service function
		x = startUp()
		if x == 1:
			#go to register function
			registerTitle()
			register()
			welcomeTitle()
		elif x == 2:
			#go to login function
			loginTitle()
			login()
			menuTitle()
			loopMenu = True
			#loop menu until the logout
			while loopMenu == True:
				m = menuOptions()
				if m == 1:
					#show balance and options function
					balanceTitle()
					b = balance()
					loopBalance = True
					while loopBalance == True:
						mo = money()
						if mo == 2:
							#deposit money function
							depositTitle()	
							deposit()
							back()
							#back to balance
							balanceTitle()
							balance()
						elif mo == 3:
							#withdraw money function
							withdrawTitle()
							withdraw()
							back()
							#back to balance
							balanceTitle()
							balance()
						elif mo == 1:
							#back to main menu
							loopBalance = False
							menuTitle()
				elif m == 2:
					#print transactions
					transactions()
					print('Type back to return to menu')
					back()
					menuTitle()
				elif m == 3:
					#logout
					loopMenu = False
					welcomeTitle()
		elif x == 3:
			#exit application
			sys.exit()
