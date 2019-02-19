#!/usr/bin/env python3

'''
This is your main script, this should call several other scripts within your packages.
'''
from controller.controller import startBank

def main():
	#LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
	#logging.basicConfig(filename='example.log',level=logging.DEBUG,
	#format = LOG_FORMAT)
	#logger = logging.getLogger('MyLogger')
	#logger.debug('hello again')

	#register()
	startBank()

if __name__ == '__main__':
	main()
