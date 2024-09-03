"""
    preprocess - cleans text from punctuation and removes extra white spaces
    lower_casing - converts text to lowercase
"""

from cleantext import clean


def preprocess(text):
    input = clean(str(text), punct=True, extra_spaces=True)
    output = input.replace('“',' ')
    output = output.replace('”',' ')
    output = output.replace('.',' ')
    output = output.replace('-',' ')

    return output


def lower_casing(text):
    output = clean(str(text),lowercase = True)

    return output


def preprocess_sentiment(text):
    output = clean(str(text), punct=True,
                   numbers = True)
    return output
