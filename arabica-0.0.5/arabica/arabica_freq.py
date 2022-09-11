"""arabica_freq"""


import pandas as pd
import numpy as np
from nltk.util import ngrams
from nltk.util import bigrams as bi
from nltk.util import trigrams as tri


from .preprocess import preprocess
from .clean_numbers import remove_numbers
from .stopwords import remove_stopwords
from .finalize import final_cleaning
from .clean_tokens import token_cleaning
from .group import grouper


def arabica_freq(text: str,
                 time: str,
                 stopwords: str,
                 punct: bool = False,
                 max_words: int='',
                 time_freq: str='',
                 numbers: bool = False) -> str:

    """Given string and time, return df with period, unigram, bigram and trigram frequencies
    :param text: Input string
    :param time: Input time
    :param stopwords: Language for stop words
    :param punct: Remove all punctuations
    :param max_words: Max number for unigrams, bigrams and trigrams displayed
    :param time_freq: Aggregation period, 'Y' - yearly, 'M' - mohtly
    :param numbers: Remove all digits
    :return: df with aggregated n-gram frequencies over period
    """

    data=pd.DataFrame()
    data['time']=time
    data['time']=data['time'].astype(str)
    data['time'] = pd.to_datetime(data['time'])
    data['text']=text
    data=data.set_index(data['time'])
    data.replace("", float("NaN"), inplace=True)
    data.dropna(subset = ["text"], inplace=True)

    if punct is True:
        data['text'] = np.vectorize(preprocess)(data['text'])

    if stopwords is not None:
        data['text'] = data.text.map(lambda x: remove_stopwords(x,stopwords=stopwords))

    if numbers is True:
        data['text'] = np.vectorize(remove_numbers)(data['text'])


    periods = []
    unigrams_freq = []
    bigrams_freq = []
    trigrams_freq = []


    for i, row in data.iterrows():
        period = row[0]
        periods.append(period)
        word = row[1]
        token = str(word).split()
        unigrams = list(ngrams(token, 1))
        bigrams = list(bi(token))
        trigrams = list(tri(token))
        unigrams_freq.append(unigrams)
        bigrams_freq.append(bigrams)
        trigrams_freq.append(trigrams)


    df = pd.DataFrame()
    df['period'] = periods
    df['period'] = df['period'].astype(str)
    df['period'] = pd.to_datetime(df['period'])
    df = df.set_index(df['period'])
    df['unigrams'] = unigrams_freq
    df['bigrams'] = bigrams_freq
    df['trigrams'] = trigrams_freq

    df['unigrams'] = np.vectorize(token_cleaning)(df['unigrams'])
    df['bigrams'] = np.vectorize(token_cleaning)(df['bigrams'])
    df['trigrams'] = np.vectorize(token_cleaning)(df['trigrams'])

    unigrams_df = df['unigrams']
    bigrams_df = df['bigrams']
    trigrams_df = df['trigrams']

    unigrams_aggr = grouper(data = unigrams_df,max_words=max_words,time_freq=time_freq)
    bigrams_aggr = grouper(data = bigrams_df,max_words=max_words,time_freq=time_freq)
    trigrams_aggr = grouper(data = trigrams_df,max_words=max_words,time_freq=time_freq)


    freq_final = unigrams_aggr.merge(bigrams_aggr, how='left',left_index=True, right_index=True)
    freq_final = freq_final.merge(trigrams_aggr, how='left',left_index=True, right_index=True)

    freq_final = freq_final[['period_x','ngram_x','ngram_y','ngram']]
    freq_final.columns=['period','unigram','bigram','trigram']

    freq_final['unigram'] = np.vectorize(final_cleaning)(freq_final['unigram'])
    freq_final['bigram'] = np.vectorize(final_cleaning)(freq_final['bigram'])
    freq_final['trigram'] = np.vectorize(final_cleaning)(freq_final['trigram'])
    freq_final = freq_final[freq_final['unigram']!=': 1']

    if time_freq == 'Y':
        freq_final['period'] = pd.to_datetime(freq_final['period'].astype('str'))
        freq_final['period'] = freq_final['period'].dt.strftime('%Y')

    elif time_freq == 'M':
        freq_final['period'] = pd.to_datetime(freq_final['period'].astype('str'))
        freq_final['period'] = freq_final['period'].dt.strftime('%Y-%m')


    return freq_final