#!/usr/bin/env python3

import os
import sys
USERNAMES = []
PASSWORDS = []
BALANCES = []
TRANSACTIONS = []
CURRENTUSER = ''
sys.path.append('error')
from error import *
import logging
LOG_FORMAT = '%(name)s - %(levelname)s - %(asctime)s - %(message)s'
logging.basicConfig(filename='logging/example.log',level=logging.DEBUG,
format = LOG_FORMAT,filemode = 'w')
logger = logging.getLogger('MyLogger')
#takeBalance = '0'
def grabUserBalance():
	#print(CURRENTUSER)
	findBalance = '0'
	countUserIndex = 0
	countPasswordIndex = 0
	with open('io/Users.txt','r') as users:
		for line in users:
			countUserIndex += 1
			line = line.strip()
			#print(line)
			if line == CURRENTUSER:
				global grabBalanceLine
				grabBalanceLine = countUserIndex
				#print('starting')
				#line = line.strip()
				newCount = 0
				with open('io/Balances.txt','r') as balances:
					for nextLine in balances:
						#print('working...')
						newCount += 1
						nextLine = nextLine.strip()
						#nextLine = nextLine.strip()
						if newCount == countUserIndex:
							findBalance = float(nextLine)
	global takeBalance
	takeBalance = float(findBalance)
	return findBalance

def addUser(username,password):	 
	users = open('io/Users.txt','a+')
	users.write(username + '\n')
	users.close()
	#USERNAMES.append(username)
	passwd = open('io/Passwords.txt','a+')
	passwd.write(password + '\n')
	passwd.close()
	#PASSWORDS.append(password)
	balance = open('io/Balances.txt','a+')
	balance.write('0' + '\n')
	balance.close()
	if os.path.exists('io/Users.txt') or os.path.exists('io/Passwords.txt') or os.path.exists('Balances.txt'):
		pass
	else:
		logger.critical('A File Does Not Exist')
	#transactions = open('io/Transactions.txt','a+')
	#transactions.write(username + '---->\n')
	#transactions.close()
	#readLists()
	#BALANCES.append(0)
	#print(USERNAMES)
	#print(PASSWORDS)
	#print(BALANCES)

def checkUser(username):	
	userValidation = 0
	with open('io/Users.txt','r') as users:
		for line in users:
			#data = users.read()
			#line = str(line)
			line = line.strip()
			if username == line:
			#print(u)
			#users.close()
				userValidation = 1
	return userValidation

'''def checkPassword(password):
	passValidation = 0
	with open('io/Passwords.txt','r') as passwords:
		for line in passwords:
			line = line == strip()
			if password == line:
				passwordValidation = 1
	return passwordValidation 
'''
def checkIndex(username,password):
	statement = 0
	countUserIndex = 0
	countPasswordIndex = 0
	with open('io/Users.txt','r') as users:
		for line in users:
			countUserIndex += 1
			line = line.strip()
			if username == line:
				global CURRENTUSER
				CURRENTUSER = line
				newCount = 0
				with open('io/Passwords.txt','r') as passwords:
					for nextLine in passwords:
						newCount += 1
						nextLine = nextLine.strip()
						if newCount == countUserIndex:
							if nextLine == password:
								statement = 1
	#print(CURRENTUSER)
	return statement

#def readLists():
#	with open('io/Transactions.txt','r') as users:
#		for line in users:
#			USERNAMES.append(line)	
#	with open('io/Passwords.txt','r') as passwords:
#		for line in passwords:
#			PASSWORDS.append(line)
#
#	with open('io/Balances.txt','r') as balances:
#		for line in balances:
#			BALANCES.append(line)


def depositCalc(amount):
	count = 0
	newBalance  = float(takeBalance) + float(amount)
	with open('io/Balances.txt','r') as balances:
		get_all = balances.readlines()
	with open('io/Balances.txt','w') as balances:
		for i,line in enumerate(get_all,1):
			if i == grabBalanceLine:
				balances.writelines(str(newBalance) + '\n')
			else:
				balances.writelines(line)
	#readLists()
	newBalance = float(newBalance)
	return newBalance

def withdrawCalc(amount):
	count = 0
	newBalance  = float(takeBalance) - float(amount)
	#if newBalance < 0
		#newBalance = 0
	with open('io/Balances.txt','r') as balances:
		get_all = balances.readlines()
	with open('io/Balances.txt','w') as balances:
		for i,line in enumerate(get_all,1):
			if i == grabBalanceLine:
				balances.writelines(str(newBalance) + '\n')
			else:
				balances.writelines(line)
	#readLists()
	newBalance = float(newBalance)
	return newBalance

def transactionsAdd(depositConfirmed):
	with open('io/' + CURRENTUSER + 'Transactions.txt','a+') as trans:
		trans.write(depositConfirmed + '\n')

def transactionsMinus(withdrawConfirmed):
	negitiveAmount = 0
	with open('io/' + CURRENTUSER + 'Transactions.txt','a+') as trans:
			trans.write(withdrawConfirmed + '\n')

def checkBal(amount):
	count = 0
	if amount > takeBalance:
		count = 1
		try:
			raise noMoneyError
		except noMoneyError:
			pass
	return count

def printTransactions():
	print('----These are your transactions----\n')
	readTrans = open('io/' + CURRENTUSER + 'Transactions.txt','r') 
	transFile = readTrans.read()
	print(transFile)
	readTrans.close()
			
	
