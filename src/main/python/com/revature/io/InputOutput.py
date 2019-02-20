#!/usr/bin/env python3

#James Watson
#Project 0 
#2/19/2019

#imports
import os
import sys
#global variable for logged in user
CURRENTUSER = ''

#more imports
sys.path.append('error')
from error import *
import logging

#create logger
LOG_FORMAT = '%(name)s - %(levelname)s - %(asctime)s - %(message)s'
logging.basicConfig(filename='logging/logging.log',level=logging.DEBUG,
format = LOG_FORMAT,filemode = 'w')
logger = logging.getLogger('MyLogger')

#find the users balance
def grabUserBalance():
	#varaibles
	findBalance = '0'
	#loop variables
	countUserIndex = 0
	countPasswordIndex = 0
	#open users
	with open('io/Users.txt','r') as users:
		#iterate through users
		for line in users:
			countUserIndex += 1
			line = line.strip()
			#if you find the current user
			if line == CURRENTUSER:
				#global variable for balance line number
				global grabBalanceLine
				grabBalanceLine = countUserIndex
				newCount = 0
				#open balances file
				with open('io/Balances.txt','r') as balances:
					#iterate through balances
					for nextLine in balances:
						newCount += 1
						nextLine = nextLine.strip()
						#line of user is equal
						#to the line of balance
						if newCount == countUserIndex:
							findBalance = float(nextLine)
	#take balance for later function in io
	global takeBalance
	takeBalance = float(findBalance)
	#return to function in service
	return findBalance

#add all new users here
def addUser(username,password):
	#opens and adds users in a text file
	users = open('io/Users.txt','a+')
	users.write(username + '\n')
	users.close()
	#opens and adds passwords in a password file
	passwd = open('io/Passwords.txt','a+')
	passwd.write(password + '\n')
	passwd.close()
	#opens and balances to a balance file
	balance = open('io/Balances.txt','a+')
	balance.write('0' + '\n')
	balance.close()
	#if the files don't exist, log a critical
	if os.path.exists('io/Users.txt') or os.path.exists('io/Passwords.txt') or os.path.exists('Balances.txt'):
		pass
	else:
		logger.critical('A File Does Not Exist')

#check if user has been created already
def checkUser(username):	
	userValidation = 0
	#open users file
	with open('io/Users.txt','r') as users:
		#iterate through
		for line in users:
			line = line.strip()
			#if the user exists already, return 1
			if username == line:
				userValidation = 1
	#return is used in service 
	return userValidation

#Check to see if username and password match for login
def checkIndex(username,password):
	statement = 0
	#counting for loops
	countUserIndex = 0
	countPasswordIndex = 0
	#open users
	with open('io/Users.txt','r') as users:
		#iterate through users
		for line in users:
			countUserIndex += 1
			line = line.strip()
			#if we find the user
			if username == line:
				#this user is now in the session for tracking
				global CURRENTUSER
				CURRENTUSER = line
				newCount = 0
				#open passwords to find the same line as user
				with open('io/Passwords.txt','r') as passwords:
					for nextLine in passwords:
						newCount += 1
						nextLine = nextLine.strip()
						#when we get to the line
						if newCount == countUserIndex:
							#we found that users password
							if nextLine == password:
								statement = 1
	#return to service 
	return statement

#calculate deposit
def depositCalc(amount):
	count = 0
	#add balance plus the amount the user wants to add
	newBalance  = float(takeBalance) + float(amount)
	#open balance file
	with open('io/Balances.txt','r') as balances:
		#read the lines 
		get_all = balances.readlines()
	with open('io/Balances.txt','w') as balances:
		#iterate over lines for variable
		for i,line in enumerate(get_all,1):
			#if we have the users balance line
			if i == grabBalanceLine:
				#write their new balance
				balances.writelines(str(newBalance) + '\n')
			else:
				#else, write what they had before
				balances.writelines(line)
	#return the new balance to service
	newBalance = float(newBalance)
	return newBalance

#withdraw money for service
def withdrawCalc(amount):
	count = 0
	#subtract balance minus amount they want to take out
	newBalance  = float(takeBalance) - float(amount)
	#open balance file
	with open('io/Balances.txt','r') as balances:
		#read lines
		get_all = balances.readlines()
	with open('io/Balances.txt','w') as balances:
		#iterate through variable in lines
		for i,line in enumerate(get_all,1):
			#if it is the current users balance
			if i == grabBalanceLine:
				#write new balance
				balances.writelines(str(newBalance) + '\n')
			else:
				#don't change what they had before
				balances.writelines(line)
	newBalance = float(newBalance)
	#return balance to service
	return newBalance

#add deposit trasactions to a file
def transactionsAdd(depositConfirmed):
	with open('io/' + CURRENTUSER + 'Transactions.txt','a+') as trans:
		trans.write(depositConfirmed + '\n')

#add withdraw transactions to the same file
def transactionsMinus(withdrawConfirmed):
	negitiveAmount = 0
	with open('io/' + CURRENTUSER + 'Transactions.txt','a+') as trans:
			trans.write(withdrawConfirmed + '\n')

#check the balance of the user account
def checkBal(amount):
	count = 0
	#if the user takes more than they have
	if amount > takeBalance:
		count = 1
		try:
			#raise my error
			raise noMoneyError
		except noMoneyError:
			pass
	#return this to service for a loop until this is not true
	return count

#print transactions to a file for current user
def printTransactions():
	print('----These are your transactions----\n')
	#make a file for the current user
	readTrans = open('io/' + CURRENTUSER + 'Transactions.txt','r') 
	transFile = readTrans.read()
	print(transFile)
	readTrans.close()
