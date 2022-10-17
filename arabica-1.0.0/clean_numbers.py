"""Cleans text from digits."""

import re

def remove_numbers(text):
    output = re.sub("[0123456789]", ' ', str(text))
    return output
