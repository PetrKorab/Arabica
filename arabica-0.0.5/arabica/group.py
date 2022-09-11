"""Grouper function."""


import pandas as pd
import nltk


def grouper(data,max_words,time_freq):

    period = []
    unigrams_aggr = []

    for u,v in data.groupby(pd.Grouper(freq=time_freq)):
        u=u
        v=pd.DataFrame(v)
        v.reset_index(drop=True,inplace=True)
        column=v.iloc[:,[0]]
        column.columns = ['unigram']
        textlist=column['unigram'].tolist()
        textlist = list(filter(None, textlist))
        tokens= str(textlist).split()
        unigram_frequency = nltk.ngrams(tokens,1)
        unigram = nltk.FreqDist(unigram_frequency)
        unigram=pd.DataFrame.from_dict(unigram,orient='index')
        unigram['word'] = unigram.index
        unigram['freq'] = unigram.iloc[:,[0]]
        unigram = unigram.sort_values(by='freq', ascending=False)
        unigram['unigram'] = unigram['word'].astype(str) + ": " + unigram['freq'].astype(str)
        unigram['unigram'] = unigram['unigram'].str.replace(',', '')
        unigram = unigram['unigram']
        unigram = unigram.iloc[:max_words]
        blankIndex_bi=[''] * len(unigram)
        unigram.index=blankIndex_bi
        unigram=unigram.tolist()[0:max_words]

        period.append(u)
        unigrams_aggr.append(unigram)

    freq_df = pd.DataFrame()
    freq_df['period']= period
    freq_df['ngram']= unigrams_aggr

    return freq_df