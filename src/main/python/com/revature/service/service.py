#!/usr/bin/env python3
#sys.path.append('error')
#from error import *
import numbers
import sys
sys.path.append('io')
from InputOutput import *
sys.path.append('error')
from error import *
import logging
#USERNAMES = []
#PASSWORDS = []
#BALANCES = []
LOG_FORMAT = '%(name)s - %(levelname)s - %(asctime)s - %(message)s'
logging.basicConfig(filename='logging/example.log',level=logging.DEBUG,
format = LOG_FORMAT,filemode = 'w')
logger = logging.getLogger('MyLogger')
#logger.debug('hello again')
def startUp():
	indicator = 0
	loginWord = 'login' 
	registerWord = 'register'
	leaveWord = 'quit'
	match = input()
	#while indicator == 0:
	if match.upper() == registerWord.upper():
		indicator = 1
	elif match.upper() == loginWord.upper():
		indicator = 2
	elif match.upper() == leaveWord.upper():
		indicator = 3
	else:
		print('Invalid input, try again')
	return indicator

def register():
	username = input('Username:' )
	#userValidation = 0
	#checkUser(username,userValidation)
	checkUser(username)
	#print('before while')
	#while userChecker == 1:
	while checkUser(username) == 1:
		try:
			print('Username taken, try again')
			raise usernameError
		except usernameError:
			username = input('Username:' )
			logger.warning('Entered a Taken Username(usernameError')
		#x = checkUser(username)
			if checkUser(username) == 0:
				break
	#print('after while')
	password = input('Password:' )
	addUser(username,password)
	#readLists()
	print('\nYou have created a new account!\nType Return to get started')
	returnWord = 'return'
	matchReturn = input()
	while matchReturn.upper() != returnWord.upper():
		print('Invalid input, try again')
		matchReturn = input()
		if matchReturn.upper() == returnWord.upper():
			break

def login():
	username = input('Username:' )
	password = input('Password:' )
	x = checkIndex(username,password)
	while x == 0:
		logger.warning('User/Pass Failed')
		print('Incorrect username or password, try again')
		username = input('Username:' )
		password = input('Password:' )
		x = checkIndex(username,password)
		if x == 1:
			break
	#USERNAME = username
def logout():
	indicator = 0
	logoutWord = 'logout'
	logout = input()
	if logout.upper() == logoutWord.upper():
		indicator = 1
	else:
		logger.info('User Logged Out')
		print('Invalid input, try again')
	return indicator

def balance():
	x = grabUserBalance()
	formatted = '${:,.2f}'.format(x)
	print('Account Balance: ' + formatted)

def money():
	indicator = 0
	backWord = 'back'
	depositWord = 'deposit'
	withdrawWord = 'withdraw'
	balanceInput = input()
	if backWord.upper() == balanceInput.upper():
		indicator = 1
	elif depositWord.upper() == balanceInput.upper():
		indicator = 2
		#deposit = 'I deposited money'
		#transaction(deposit)
	elif withdrawWord.upper() == balanceInput.upper():
		indicator = 3
		#withdraw = 'I withdrew money'
		#transaction(withdraw)
	else:
		print('Invalid input, try again')
	return indicator

def back():
	backWord = 'back'
	backInput = input()
	while backWord.upper() != backInput.upper():
		print('Invalid input, try again')
		backInput = input()
		#if backWord.upper() == backInput.upper():
			#break
	
def menuOptions():
	indicator = 0
	logoutWord  = 'logout' 
	balanceWord = 'balance'
	transactionWord = 'transactions'
	match = input()
	#while indicator == 0:
	if match.upper() == balanceWord.upper():
		indicator = 1
	elif match.upper() == transactionWord.upper():
		indicator = 2
	elif match.upper() == logoutWord.upper():
		indicator = 3
	else:
		print('Invalid input, try again')
	return indicator

def deposit():
	notNumber = True
	#amount = input('Deposit Amount:' )
	#amount = float(amount)
	while notNumber == True:
		amount = input('Deposit Amount:' )
		try:	
			amount = float(amount)
			notNumber = False
			#raise nonNumberError
		except ValueError:
			logger.debug('User Did Not Use Numbers For Transactions')
			print('Not a number, try again') 
	#amount = float(amount)
	print('Type Back to continue')
	transAmount = '${:,.2f}'.format(amount)
	newBalance = depositCalc(amount)
	#formatted = '${:,.2f}'.format(newBalance)
	#print(formatted)
	depositTransactions(transAmount)
def withdraw():
	#amount = input('Withdraw Amount:' )
	#amount = float(amount)
	notNumber = True
	#amount = input('Deposit Amount:' )
	#amount = float(amount)
	while notNumber == True:
		amount = input('Withdraw Amount:' )
		try:	
			amount = float(amount)
			notNumber = False
		except ValueError:
			logger.debug('User Did Not Enter Numbers For Transactions')
			print('Not a number, try again') 
	#amount = float(amount)
	checkBal(amount)
	while checkBal(amount) == 1:
		logger.warning('Not Enough Funds For Withdraw Request(NoMoneyError')
		amount = input('Not enough funds, try again\nWithdraw Amount:' )
		amount = float(amount)
		checkBal(amount)
	print('Type Back to continue')
	newBalance = withdrawCalc(amount)
	#formatted = '${:,.2f}'.format(newBalance)
	#transactions(formatted)
	amount = '${:,.2f}'.format(amount)
	withdrawTransactions(amount)
def depositTransactions(status):
	x = 'Deposit made: ' + str(status)
	transactionsAdd(x)		

def withdrawTransactions(status):
	x = 'Withdraw made: ' + str(status)
	transactionsMinus(x)
	#print('after function')

def transactions():
	printTransactions()	
