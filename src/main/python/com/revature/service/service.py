#!/usr/bin/env python3

#James Watson
#Project 0 
#2/19/2019

#Imports needed functions and scripts
import numbers
from getpass import getpass
import sys
sys.path.append('io')
from InputOutput import *
sys.path.append('error')
from error import *

#Creating a logger
import logging
LOG_FORMAT = '%(name)s - %(levelname)s - %(asctime)s - %(message)s'
logging.basicConfig(filename='logging/logging.log',level=logging.DEBUG,
format = LOG_FORMAT,filemode = 'w')
logger = logging.getLogger('MyLogger')

#Called at the start of program
def startUp():
	#variables
	indicator = 0
	loginWord = 'login' 
	registerWord = 'register'
	leaveWord = 'quit'
	match = input()
	#match variables to input then bring to controller
	if match.upper() == registerWord.upper():
		indicator = 1
	elif match.upper() == loginWord.upper():
		indicator = 2
	elif match.upper() == leaveWord.upper():
		indicator = 3
	else:
		print('Invalid input, try again')
	return indicator

#register a new user
def register():
	#input user and make sure the name is avalible and not blank
	boolean = 0
	username = input('Username:' )
	#iterate through username
	for char in username:
		#find if it is empty
		if char != '':
			boolean = 1
			break
	#if user has an empty username, loop
	if boolean == 0:
		print('Username can not be blank, try again')
		#log debug
		logger.debug('Username Can Not Be Blank')
		#recall function
		register()
	checkUser(username)
	#if not avalible, then keep asking for a new username
	while checkUser(username) == 1:
		try:
			print('Username taken, try again')
			#raising my own error
			raise usernameError
		except usernameError:
			username = input('Username:' )
			#logging warning
			logger.warning('Entered a Taken Username(usernameError')
			if checkUser(username) == 0:
				break
	#make a password and then add the user
	password = getpass('Password:' )
	addUser(username,password)
	print('\nYou have created a new account!\nType Return to get started')
	returnWord = 'return'
	matchReturn = input()
	#loop until the user enters return to go back to the home screen
	while matchReturn.upper() != returnWord.upper():
		print('Invalid input, try again')
		matchReturn = input()
		if matchReturn.upper() == returnWord.upper():
			break
#login function
def login():
	username = input('Username:' )
	password = getpass('Password:' )
	#check to see if username and password match for the user
	x = checkIndex(username,password)
	#if they don't, keep trying
	while x == 0:
		#log warning
		logger.warning('User/Pass Failed')
		print('Incorrect username or password, try again')
		username = input('Username:' )
		password = getpass('Password:' )
		x = checkIndex(username,password)
		if x == 1:
			break

#logout function
def logout():
	indicator = 0
	logoutWord = 'logout'
	logout = input()
	#if user enters logout then they go back to main menu
	if logout.upper() == logoutWord.upper():
		indicator = 1
		#logging info, user logout
		logger.info('User Logged Out')
	else:
		#try again to logout
		print('Invalid input, try again')
	return indicator

#balance of account
def balance():
	#grab balance and format it correctly, then print
	x = grabUserBalance()
	formatted = '${:,.2f}'.format(x)
	print('Account Balance: ' + formatted)

#balance menu movements
def money():
	#varaibles
	indicator = 0
	backWord = 'back'
	depositWord = 'deposit'
	withdrawWord = 'withdraw'
	balanceInput = input()
	#if one of these words is typed, take it to the controller
	if backWord.upper() == balanceInput.upper():
		indicator = 1
	elif depositWord.upper() == balanceInput.upper():
		indicator = 2
	elif withdrawWord.upper() == balanceInput.upper():
		indicator = 3
	else:
		print('Invalid input, try again')
	return indicator

#back function to make user back up a step
def back():
	backWord = 'back'
	backInput = input()
	while backWord.upper() != backInput.upper():
		print('Invalid input, try again')
		backInput = input()

#menu options for user	
def menuOptions():
	#variables
	indicator = 0
	logoutWord  = 'logout' 
	balanceWord = 'balance'
	transactionWord = 'transactions'
	match = input()
	#if the user enters these words, report to the controller
	if match.upper() == balanceWord.upper():
		indicator = 1
	elif match.upper() == transactionWord.upper():
		indicator = 2
	elif match.upper() == logoutWord.upper():
		indicator = 3
	else:
		print('Invalid input, try again')
	return indicator

#deposit money
def deposit():
	notNumber = True
	#while user did not enter a number, keep trying
	while notNumber == True:
		amount = input('Deposit Amount:' )
		try:	
			#if it can not become a float, value error
			amount = float(amount)
			notNumber = False
		except ValueError:
			#logging degug
			logger.debug('User Did Not Use Numbers For Transactions')
			print('Not a number, try again')
	#type back and format money
	print('Type Back to continue')
	transAmount = '${:,.2f}'.format(amount)
	#calculate new balance for user
	newBalance = depositCalc(amount)
	#add this to transactions file
	depositTransactions(transAmount)

#withdraw money
def withdraw():
	notNumber = True
	#if user does not enter a number, keep trying
	while notNumber == True:
		amount = input('Withdraw Amount:' )
		try:	
			amount = float(amount)
			notNumber = False
		except ValueError:
			#log debug
			logger.debug('User Did Not Enter Numbers For Transactions')
			print('Not a number, try again')
	#check balance to make sure it is positive
	checkBal(amount)
	#if it is not positive, keep looping
	while checkBal(amount) == 1:
		#log the attempts
		logger.warning('Not Enough Funds For Withdraw Request(NoMoneyError')
		amount = input('Not enough funds, try again\nWithdraw Amount:' )
		amount = float(amount)
		checkBal(amount)
	#type back and calculate the withdraw
	print('Type Back to continue')
	newBalance = withdrawCalc(amount)
	#format money
	amount = '${:,.2f}'.format(amount)
	#add this to the transactions file
	withdrawTransactions(amount)

#transactions for deposits
def depositTransactions(status):
	#add transactions in io
	x = 'Deposit made: ' + str(status)
	transactionsAdd(x)		

#transactions for withdraw
def withdrawTransactions(status):
	#add withdraws in io
	x = 'Withdraw made: ' + str(status)
	transactionsMinus(x)

#print the transactions for the user if they ask
def transactions():
	printTransactions()
