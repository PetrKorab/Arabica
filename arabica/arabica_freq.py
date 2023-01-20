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
                 date_format: str,
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

    if date_format == 'eur':
        data['time']=data['time'].astype(str)
        data['time'] = pd.to_datetime(data['time'], dayfirst=True)

    elif date_format == 'us':
        data['time']=data['time'].astype(str)
        data['time'] = pd.to_datetime(data['time'], dayfirst=False)

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
        unigram_ungr = pd.DataFrame.from_dict(unigram_ungr,orient='index')
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

        df['bigrams'] = df['bigrams'].astype(str)
        df['bigrams']= df['bigrams'].str.replace(")"," ")
        df['bigrams']= df['bigrams'].str.replace("(",' ')
        df['bigrams']= df['bigrams'].str.replace("""', '""","+")
        df['bigrams']= df['bigrams'].str.replace("["," ")
        df['bigrams']= df['bigrams'].str.replace("]"," ")
        df['bigrams']= df['bigrams'].str.replace("'",'')
        df['bigrams']= df['bigrams'].str.replace(" ,  ",' ')
        df['bigrams']= df['bigrams'].str.replace("  ",'')
        bigrams_str = ' '.join(df['bigrams'])
        tokens_ungr_bi= str(bigrams_str).split()
        bigram_frequency_ungr = nltk.ngrams(tokens_ungr_bi,1)
        bigram_ungr = nltk.FreqDist(bigram_frequency_ungr)
        bigram_ungr=pd.DataFrame.from_dict(bigram_ungr,orient='index')
        bigram_ungr['bigram'] = bigram_ungr.index
        bigram_ungr['bigram_freq'] = bigram_ungr.iloc[:,[0]]
        bigram_ungr = bigram_ungr.sort_values(by='bigram_freq', ascending=False)
        bigram_ungr['bigram'] = bigram_ungr['bigram'].astype(str) + ": " + bigram_ungr['bigram_freq'].astype(str)
        bigram_ungr['bigram'] = bigram_ungr['bigram'].str.replace(',', '')
        bigram_ungr = bigram_ungr['bigram']
        bigram_ungr = bigram_ungr.iloc[:max_words]
        bigram_ungr= bigram_ungr.astype(str)
        bigram_ungr = bigram_ungr.str.replace('(', '')
        bigram_ungr = bigram_ungr.str.replace(')', '')
        bigram_ungr = bigram_ungr.str.replace("""'""", '')
        bigram_ungr = bigram_ungr.str.split(n = 2, pat=':',expand=True)
        bigram_ungr['bigram_freq'] = bigram_ungr.iloc[:,[1]]
        bigram_ungr['bigram'] = bigram_ungr.iloc[:,[0]]
        bigram_ungr['bigram'] = bigram_ungr['bigram'].str.replace(' ', ', ')
        bigram_ungr['bigram'] = bigram_ungr['bigram'].astype(str)
        bigram_ungr = bigram_ungr[['bigram','bigram_freq']]
        bigram_ungr.reset_index(inplace = True)

        bigram_ungr = pd.DataFrame(bigram_ungr)
        bigram_col = bigram_ungr['bigram'].str.replace("+",",")
        bigram_freq = bigram_ungr['bigram_freq']
        bigram_ungr = pd.merge(bigram_col, bigram_freq, left_index=True, right_index=True)


        df['trigrams'] = df['trigrams'].astype(str)
        df['trigrams']= df['trigrams'].str.replace(")"," ")
        df['trigrams']= df['trigrams'].str.replace("(",' ')
        df['trigrams']= df['trigrams'].str.replace("""', '""","+")
        df['trigrams']= df['trigrams'].str.replace("["," ")
        df['trigrams']= df['trigrams'].str.replace("]"," ")
        df['trigrams']= df['trigrams'].str.replace("'",'')
        df['trigrams']= df['trigrams'].str.replace(" ,  ",' ')
        df['trigrams']= df['trigrams'].str.replace("  ",'')
        trigrams_str = ' '.join(df['trigrams'])
        tokens_ungr_tri= str(trigrams_str).split()
        trigrams_frequency_ungr = nltk.ngrams(tokens_ungr_tri,1)
        trigram_ungr = nltk.FreqDist(trigrams_frequency_ungr)
        trigram_ungr=pd.DataFrame.from_dict(trigram_ungr,orient='index')
        trigram_ungr['trigrams'] = trigram_ungr.index
        trigram_ungr['trigrams_freq'] = trigram_ungr.iloc[:,[0]]
        trigram_ungr = trigram_ungr.sort_values(by='trigrams_freq', ascending=False)
        trigram_ungr['trigrams'] = trigram_ungr['trigrams'].astype(str) + ": " + trigram_ungr['trigrams_freq'].astype(str)
        trigram_ungr['trigrams'] = trigram_ungr['trigrams'].str.replace(',', '')
        trigram_ungr = trigram_ungr['trigrams']
        trigram_ungr = trigram_ungr.iloc[:max_words]
        trigram_ungr= trigram_ungr.astype(str)
        trigram_ungr = trigram_ungr.str.replace('(', '')
        trigram_ungr = trigram_ungr.str.replace(')', '')
        trigram_ungr = trigram_ungr.str.replace("""'""", '')
        trigram_ungr = trigram_ungr.str.split(n = 2, pat=':',expand=True)
        trigram_ungr['trigram_freq'] = trigram_ungr.iloc[:,[1]]
        trigram_ungr['trigram'] = trigram_ungr.iloc[:,[0]]
        trigram_ungr['trigram'] = trigram_ungr['trigram'].str.replace(' ', ', ')
        trigram_ungr['trigram_freq'] = trigram_ungr['trigram_freq'].astype(str)
        trigram_ungr = trigram_ungr[['trigram','trigram_freq']]
        trigram_ungr.reset_index(inplace = True)

        trigram_col = trigram_ungr['trigram'].str.replace("+",",")
        trigram_freq = trigram_ungr['trigram_freq']
        trigram_ungr = pd.merge(trigram_col, trigram_freq, left_index=True, right_index=True)

        freq_final = unigram_ungr.merge(bigram_ungr, how='left',left_index=True, right_index=True)
        freq_final = freq_final.merge(trigram_ungr, how='left',left_index=True, right_index=True)
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
    #
    return freq_final