# -*- coding: utf-8-*-

from yahoo_finance import Share
import re

WORDS = ["STOCKS"]

def handle(text, mic, profile):

	positions = open('/home/pi/.jasper/config.txt', 'r')

	total_change = 0

	for position in positions.readlines():
		if '#' in position:
			pass
		else:
			x = position.split(':')
			stock = Share(str(x[0]))
			change = float(stock.get_change().strip('+'))
			shares = float(x[1])
			#print x[0] + ' ' + str(change) + ' ' + str(shares) + ' ' + str(change * shares)
	
			total_change += (change * shares)
	
	#print("$%.2f" % round(total_change, 2))
	change = ("%.2f" % round(total_change, 2))
	
	if change[0] == '-':
		updown = 'down'
	else:
		updown = 'up'

	change = change[1:len(change)]
	change = change.split('.')

	tens = str(change[0])
	ones = str(change[1])

	#print 'Your stocks are ' + updown + ' ' + tens + ' dollars and ' + ones + ' cents on the day.'
	sentence = 'Your stocks are ' + updown + ' ' + tens + ' dollars and ' + ones + ' cents on the day.'
	mic.say(sentence)
		

def isValid(text):
	return bool(re.search(r'\bstocks\b', text, re.IGNORECASE))
