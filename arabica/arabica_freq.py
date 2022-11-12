"""arabica_freq method"""


import pandas as pd
import numpy as np
import nltk
from nltk.util import ngrams
from nltk.util import bigrams as bi
from nltk.util import trigrams as tri


from .preprocess import *
from .clean_numbers import remove_numbers
from .stopwords import remove_stopwords
from .group import grouper
from .clean_ngram import *



def arabica_freq(text: str,
                 time: str,
                 stopwords: [],
                 skip: [],
                 max_words: int='',
                 punct: bool = False,
                 lower_case: bool = False,
                 time_freq: str='',
                 numbers: bool = False) -> str:

    data=pd.DataFrame()
    data['text']=text

    if time_freq != 'ungroup':
        data['time']=time
    else:
        data['time']='2016-08-30'

    data['time']=data['time'].astype(str)
    data['time'] = pd.to_datetime(data['time'])
    data=data.set_index(data['time'])
    data.replace("", float("NaN"), inplace=True)
    data.dropna(subset = ["text"], inplace=True)

    if lower_case is True:
        data['text'] = np.vectorize(lower_casing)(data['text'])

    if punct is True:
        data['text'] = np.vectorize(preprocess)(data['text'])

    if stopwords is not None:
        data['text'] = data.text.map(lambda x: remove_stopwords(x,stopwords=[stopwords]))

    if numbers is True:
        data['text'] = np.vectorize(remove_numbers)(data['text'])

    periods = []
    unigrams_freq = []
    bigrams_freq = []
    trigrams_freq = []

    for i, row in data.iterrows():
        period = row[1]
        periods.append(period)
        word = row[0]
        token = str(word).split()
        if skip is not None:
            tokens_clean = [x for x in token if x not in skip]
        else: tokens_clean = token
        unigrams = list(ngrams(tokens_clean, 1))
        bigrams = list(bi(tokens_clean))
        trigrams = list(tri(tokens_clean))
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

    if time_freq == 'ungroup':

        df['unigrams'] = np.vectorize(ungroup_cleaning)(df['unigrams'])
        unigrams_str = ' '.join(df['unigrams'])
        tokens_ungr= str(unigrams_str).split()
        unigram_frequency_ungr = nltk.ngrams(tokens_ungr,1)
        unigram_ungr = nltk.FreqDist(unigram_frequency_ungr)
        unigram_ungr=pd.DataFrame.from_dict(unigram_ungr,orient='index')
        unigram_ungr['word'] = unigram_ungr.index
        unigram_ungr['freq'] = unigram_ungr.iloc[:,[0]]
        unigram_ungr = unigram_ungr.sort_values(by='freq', ascending=False)
        unigram_ungr['unigram'] = unigram_ungr['word'].astype(str) + ": " + unigram_ungr['freq'].astype(str)
        unigram_ungr['unigram'] = unigram_ungr['unigram'].str.replace(',', '')
        unigram_ungr = unigram_ungr['unigram']
        unigram_ungr = unigram_ungr.iloc[:max_words]
        unigram_ungr= unigram_ungr.astype(str)
        unigram_ungr = unigram_ungr.str.replace('(', '')
        unigram_ungr = unigram_ungr.str.replace(')', '')
        unigram_ungr = unigram_ungr.str.replace("""'""", '')
        unigram_ungr = unigram_ungr.str.split(n = 2, pat=':',expand=True)
        unigram_ungr['unigram_freq'] = unigram_ungr.iloc[:,[1]]
        unigram_ungr['unigram'] = unigram_ungr.iloc[:,[0]]
        unigram_ungr = unigram_ungr[['unigram','unigram_freq']]
        unigram_ungr.reset_index(inplace = True)

        bigrams_frequency_ungr = nltk.bigrams(tokens_ungr)
        bigrams_ungr = nltk.FreqDist(bigrams_frequency_ungr)
        bigrams_ungr=pd.DataFrame.from_dict(bigrams_ungr,orient='index')
        bigrams_ungr['bigram'] = bigrams_ungr.index
        bigrams_ungr['bigram_freq'] = bigrams_ungr.iloc[:,[0]]
        bigrams_ungr = bigrams_ungr.sort_values(by='bigram_freq', ascending=False)
        bigrams_ungr['bigram'] = bigrams_ungr['bigram'].astype(str) + ": " + bigrams_ungr['bigram_freq'].astype(str)
        bigrams_ungr['bigram'] = bigrams_ungr['bigram'].str.replace(',', '')
        bigrams_ungr = bigrams_ungr['bigram']
        bigrams_ungr = bigrams_ungr.iloc[:max_words]
        bigrams_ungr= bigrams_ungr.astype(str)
        bigrams_ungr = bigrams_ungr.str.replace('(', '')
        bigrams_ungr = bigrams_ungr.str.replace(')', '')
        bigrams_ungr = bigrams_ungr.str.replace("""'""", '')
        bigrams_ungr = bigrams_ungr.str.split(n = 2, pat=':',expand=True)
        bigrams_ungr['bigram_freq'] = bigrams_ungr.iloc[:,[1]]
        bigrams_ungr['bigram'] = bigrams_ungr.iloc[:,[0]]
        bigrams_ungr['bigram'] = bigrams_ungr['bigram'].str.replace(' ', ', ')
        bigrams_ungr['bigram'] = bigrams_ungr['bigram'].astype(str)
        bigrams_ungr = bigrams_ungr[['bigram','bigram_freq']]
        bigrams_ungr.reset_index(inplace = True)

        trigram_frequency_ungr = nltk.trigrams(tokens_ungr)
        trigrams_ungr = nltk.FreqDist(trigram_frequency_ungr)
        trigrams_ungr=pd.DataFrame.from_dict(trigrams_ungr,orient='index')
        trigrams_ungr['trigram'] = trigrams_ungr.index
        trigrams_ungr['trigram_freq'] = trigrams_ungr.iloc[:,[0]]
        trigrams_ungr = trigrams_ungr.sort_values(by='trigram_freq', ascending=False)
        trigrams_ungr['trigram'] = trigrams_ungr['trigram'].astype(str) + ": " + trigrams_ungr['trigram_freq'].astype(str)
        trigrams_ungr['trigram'] = trigrams_ungr['trigram'].str.replace(',', '')
        trigrams_ungr = trigrams_ungr['trigram']
        trigrams_ungr = trigrams_ungr.iloc[:max_words]
        trigrams_ungr= trigrams_ungr.astype(str)
        trigrams_ungr = trigrams_ungr.str.replace('(', '')
        trigrams_ungr = trigrams_ungr.str.replace(')', '')
        trigrams_ungr = trigrams_ungr.str.replace("""'""", '')
        trigrams_ungr = trigrams_ungr.str.split(n = 2, pat=':',expand=True)
        trigrams_ungr['trigram_freq'] = trigrams_ungr.iloc[:,[1]]
        trigrams_ungr['trigram'] = trigrams_ungr.iloc[:,[0]]
        trigrams_ungr['trigram'] = trigrams_ungr['trigram'].str.replace(' ', ', ')
        trigrams_ungr['trigram'] = trigrams_ungr['trigram'].astype(str)
        trigrams_ungr = trigrams_ungr[['trigram','trigram_freq']]
        trigrams_ungr.reset_index(inplace = True)

        freq_final = unigram_ungr.merge(bigrams_ungr, how='left',left_index=True, right_index=True)
        freq_final = freq_final.merge(trigrams_ungr, how='left',left_index=True, right_index=True)
        freq_final = freq_final[['unigram','unigram_freq','bigram','bigram_freq','trigram','trigram_freq']]
        freq_final = pd.DataFrame(freq_final)

    else:

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
        freq_final = freq_final[freq_final['bigram']!=': 1']
        freq_final = freq_final[freq_final['trigram']!=': 1']

        if time_freq == 'Y':
            freq_final['period'] = pd.to_datetime(freq_final['period'].astype('str'))
            freq_final['period'] = freq_final['period'].dt.strftime('%Y')

        elif time_freq == 'M':
            freq_final['period'] = pd.to_datetime(freq_final['period'].astype('str'))
            freq_final['period'] = freq_final['period'].dt.strftime('%Y-%m')

        elif time_freq == 'D':
            freq_final['period'] = pd.to_datetime(freq_final['period'].astype('str'))
            freq_final['period'] = freq_final['period'].dt.strftime('%Y-%m-%d')

    return freq_final