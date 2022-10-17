"""Token pre-processing."""


import re

def token_cleaning(text):

    input = re.sub('[)]', ' ', str(text))
    input = re.sub("]", '', input)
    input = re.sub('[(]', ';',input)
    input = re.sub(' ', '', input)
    input = re.sub(',','+', input)
    input = input.replace('+;', ' ')
    input = input.replace('[;', '')
    input = input.replace('[', '')
    input = input.replace('[]', '')
    output = re.sub("""'""", '', input)

    return output