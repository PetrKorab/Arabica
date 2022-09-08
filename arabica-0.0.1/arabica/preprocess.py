"""Cleans text from punctuation, removes extra white spaces and converts to lowercase."""

from cleantext import clean

def preprocess(text):
    output = clean(str(text),punct = True, lowercase=True, extra_spaces=True)
    return output
