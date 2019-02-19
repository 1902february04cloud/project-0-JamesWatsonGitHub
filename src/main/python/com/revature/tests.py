#!/usr/bin/env python3
import logging
import sys
sys.path.append('io')
from InputOutput import *
sys.path.append('error')
from error import *
#sys.path.append('../io')
#from InputOutput import checkIndex
def main():
	username = 'test'
	password = 'test'
	x = checkIndex(username,password)
	if x == 0:
		print('failed login')
	elif x == 1:
		print('succesful login')

	#balance is 100 for test
	amount = 99
	grabUserBalance()
	y = checkBal(amount)
	if y == 0:
		print('Good balance')
	elif y == 1:
		print('Can not withdraw that much')
	
	
if __name__ == '__main__':
	main()
