
# Sentiment analysis and structural breaks identification module

import jenkspy
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd
import sys


from .preprocess import *
from .group import *
from .sentiment import sentiment_vader


def coffee_break(text: str,                  # Text column
                 time: str,                  # Time column
                 date_format: str,           # Date format: 'eur' - European, 'us' - American
                 skip: [ ],                  # Remove additional strings
                 preprocess: bool = False,   # Clean data from numbers and punctuation
                 time_freq: int = '',        # Aggregation period: 'Y'/'M'
                 n_breaks: int = ''):        # Number of breaks: min. 2


    if n_breaks is not None:
        if n_breaks < 2:
            sys.exit("N_breaks parameter is too low. Increase it!")

        else:
            pass

    data=pd.DataFrame()
    data['text']=text
    data['period']=time

    data=data.set_index(data['period'])
    data.replace("", float("NaN"), inplace=True)
    data.dropna(subset = ["text"], inplace=True)


    if skip is not None:
        data['text'] = data.text.str.replace('|'.join(skip), '.', regex=True).str.strip()

    if preprocess is True:
        data['text'] = np.vectorize(preprocess_sentiment)(data['text'])


    if time_freq == 'M':
        if date_format == 'eur':
            data['period']=data['period'].astype(str)
            data['period'] = pd.to_datetime(data['period'], dayfirst=True)

        elif date_format == 'us':
            data['period']=data['period'].astype(str)
            data['period'] = pd.to_datetime(data['period'], dayfirst=False)

        data['sentiment'] = np.vectorize(sentiment_vader)(data['text'])
        sentiment_ts = grouper_sentiment(data = data,time_freq='1M')
        sentiment_ts['period'] = pd.to_datetime(sentiment_ts['period'])
        sentiment_ts.set_index(sentiment_ts['period'], inplace = True)
        sentiment_ts.columns = ['period', 'sentiment']


        if n_breaks is None:
            ts = sentiment_ts['sentiment']
            ts = pd.DataFrame(ts)

            ts.index = pd.to_datetime(ts.index, format = '%Y-%m')
            sentiment_ts.reset_index(drop = True, inplace = True)

            sentiment_ts['period'] = pd.to_datetime(sentiment_ts['period'].astype('str'))
            sentiment_ts['period'] = sentiment_ts['period'].dt.strftime('%Y-%m')
            sentiment_ts.set_index('period', inplace = True)

            figure(figsize=(12, 8), dpi=800)
            plt.plot(ts, label='sentiment')
            plt.grid(linewidth=0.5)
            plt.xlabel('Period', size = 13, labelpad = 6)
            plt.ylabel('Sentiment', size = 13, labelpad = 6)
            plt.legend(loc = 'best', fontsize = 13)
            picture = plt.show()

        else:
            sentiment_ts.reset_index(drop = True, inplace = True)
            sentiment_ts['period'] = pd.to_datetime(sentiment_ts['period'].astype('str'))
            sentiment_ts['period'] = sentiment_ts['period'].dt.strftime('%Y-%m')

            ts = sentiment_ts
            ts.set_index('period', inplace = True)
            ts.index = pd.to_datetime(ts.index, format='%Y-%m').to_period("m")

            ts_series = ts.squeeze()

            y = np.array(ts_series.tolist())
            breaks = jenkspy.jenks_breaks(y, n_classes=n_breaks-1)

            breaks_jkp = []

            for v in breaks:
                idx = ts_series.index[ts_series == v]
                breaks_jkp.append(idx)

            figure(figsize=(12, 8), dpi=800)
            ts_series.plot(label='sentiment')
            print_legend = True

            for i in breaks_jkp:
                if print_legend:
                    plt.axvline(i, color='red',linestyle='dashed', label='breaks')
                    print_legend = False
                else:
                    plt.axvline(i, color='red',linestyle='dashed')

            plt.grid(linewidth=0.5)
            plt.xlabel('Period', size = 13, labelpad = 6)
            plt.ylabel('Sentiment', size = 13, labelpad = 6)
            plt.legend(loc = 'best', fontsize = 13)
            picture = plt.show()


    elif time_freq == 'Y':
        if date_format == 'eur':
            data['period']=data['period'].astype(str)
            data['period'] = pd.to_datetime(data['period'], dayfirst=True)

        elif date_format == 'us':
            data['period']=data['period'].astype(str)
            data['period'] = pd.to_datetime(data['period'], dayfirst=False)

        data['sentiment'] = np.vectorize(sentiment_vader)(data['text'])
        sentiment_ts = grouper_sentiment(data = data,time_freq='1Y')
        sentiment_ts['period'] = pd.to_datetime(sentiment_ts['period'])
        sentiment_ts.set_index(sentiment_ts['period'], inplace = True)
        sentiment_ts.columns = ['period', 'sentiment']

        if n_breaks is None:
            ts = sentiment_ts['sentiment']
            ts = pd.DataFrame(ts)

            ts.index = pd.to_datetime(ts.index, format = '%Y').year
            sentiment_ts.reset_index(drop = True, inplace = True)

            sentiment_ts['period'] = pd.to_datetime(sentiment_ts['period'].astype('str'))
            sentiment_ts['period'] = sentiment_ts['period'].dt.strftime('%Y')
            sentiment_ts.set_index('period', inplace = True)

            figure(figsize=(12, 8), dpi=800)
            plt.plot(ts, label='sentiment')
            plt.grid(linewidth=0.5)
            plt.xlabel('Period', size = 13, labelpad = 8)
            plt.xticks(ts.index, rotation = 45)
            plt.ylabel('Sentiment', size = 13, labelpad = 6)
            plt.legend(loc = 'best', fontsize = 13)
            picture = plt.show()

        else:
            sentiment_ts.reset_index(drop = True, inplace = True)
            sentiment_ts['period'] = pd.to_datetime(sentiment_ts['period'].astype('str'))
            sentiment_ts['period'] = sentiment_ts['period'].dt.strftime('%Y')

            ts = sentiment_ts
            ts.set_index('period', inplace = True)
            ts.index = pd.to_datetime(ts.index, format='%Y').year
            ts_series = ts.squeeze()

            y = np.array(ts_series.tolist())
            breaks = jenkspy.jenks_breaks(y, n_classes=n_breaks-1)

            breaks_jkp = []

            for v in breaks:
                idx = ts_series.index[ts_series == v]
                breaks_jkp.append(idx)

            figure(figsize=(12, 8), dpi=800)
            plt.plot(ts_series, label='sentiment')
            print_legend = True

            for i in breaks_jkp:
                if print_legend:
                    plt.axvline(i, color='red',linestyle='dashed', label='breaks')
                    print_legend = False
                else:
                    plt.axvline(i, color='red',linestyle='dashed')

            plt.grid(linewidth=0.5)
            plt.xlabel('Period', size = 13, labelpad = 6)
            plt.xticks(ts_series.index, rotation = 45)
            plt.ylabel('Sentiment', size = 13, labelpad = 6)
            plt.legend(loc = 'best', fontsize = 13)
            picture = plt.show()

    return sentiment_ts