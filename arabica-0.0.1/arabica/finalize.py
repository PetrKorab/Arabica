"""Cleans returned dataframe from redundant characters."""

import re

def final_cleaning(text):
    input = re.sub('[("[)]', ' ', str(text))
    input = re.sub("[']", ' ', input)
    input = re.sub("]", ' ', input)
    input = re.sub(' ,  ', ',', input)
    input = re.sub(r'''\\''', '', input)
    input = re.sub(' ', '', input)
    input = input.replace('+', ',')
    input = input.replace(':', ': ')
    output = re.sub(',:', ':', input)
    return output