# -*- coding: utf-8-*-
import re

WORDS = ["FUCK"]


def handle(text, mic, profile):

    mic.say("Fuck you right back you heap of crap.")


def isValid(text):
    """
        Returns True if input is related to the time.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\bfuck\b', text, re.IGNORECASE))
