"""
    preprocess - cleans text from punctuation and removes extra white spaces
    lower_casing - converts text to lowercase
"""

from cleantext import clean


def preprocess(text):
    output = clean(str(text), punct=True, extra_spaces=True)
    return output


def lower_casing(text):
    output = clean(str(text),lowercase = True)

    return output

