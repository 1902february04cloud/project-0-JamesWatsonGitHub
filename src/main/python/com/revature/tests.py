#!/usr/bin/env python3

#James Watson
#Project 0 
#2/19/2019

#imports
import sys
sys.path.append('io')
from InputOutput import *
sys.path.append('error')
from error import *

#main to check a few test cases
def main():
	#user login test function
	username = 'test'
	password = 'test'
	x = checkIndex(username,password)
	#if login fails
	if x == 0:
		print('Login: Failed Login')
	#if login is sussessful
	elif x == 1:
		print('Login: Successful Login')

	#balance is 100 for test user but take 99
	amount = 99
	#grab new balance in io
	grabUserBalance()
	#check balance
	y = checkBal(amount)
	#if balance is positive
	if y == 0:
		print('Balance Amount: Good balance(Passed)')
	#if balance is negitive
	elif y == 1:
		print('Balance Amount: Bad balance(Failed)')
	
	
if __name__ == '__main__':
	main()
