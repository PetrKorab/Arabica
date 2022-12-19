"""
    preprocess - cleans text from punctuation and removes extra white spaces
    lower_casing - converts text to lowercase
"""

from cleantext import clean


def preprocess(text):
    input = clean(str(text), punct=True, extra_spaces=True)
    output = input.replace('“', '')
    output_out = output.replace('”', '')
    return output_out


def lower_casing(text):
    output = clean(str(text),lowercase = True)

    return output

