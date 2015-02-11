# -*- coding: utf-8-*-
import feedparser
import re
import time

WORDS = ["MOVIES"]

def handle(text, mic, profile):

	moviefeed = feedparser.parse('http://www.fandango.com/rss/top10boxoffice.rss')

	mic.say('The movies currently in theaters are.')
	for entry in moviefeed.entries[0:-1]:
		title = entry.title
		splitmovie = title.split(' ')
		movie = splitmovie[1:-1]
		fixed_name = ' '.join(movie)
		mic.say(fixed_name)

def isValid(text):
	"""
		Returns True if the input is related to movies.

		Arguments:
		text -- user-input, typically transcribed speech
	"""
	return bool(re.search(r'\bmovies\b', text, re.IGNORECASE))

