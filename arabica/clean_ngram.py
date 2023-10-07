
"These functions do internal character cleaning during the n-gram analysis"

import re


def ungroup_cleaning(text):

    input = re.sub('[)]', ' ', str(text))
    input = re.sub("]", '', input)
    input = re.sub('[(]', ';',input)
    input = re.sub(';', ' ', input)
    input = re.sub(',','', input)
    input = input.replace('+;', ' ')
    input = input.replace('[;', '')
    input = input.replace('[', '')
    input = input.replace('[]', '')
    output = re.sub("""'""", '', input)

    return output



def bigram_cleaning(text):

    input = str(text).replace('(', '')
    input = input.replace("""'', ''""", '')
    output = input.replace(')', '')

    return output



def trigram_cleaning(text):

    input = str(text).replace('(', '')
    output = input.replace(')', '')

    return output




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