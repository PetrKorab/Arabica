from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from finvader import finvader

def sentiment_vader(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    compound = sentiment_dict['compound']

    return compound



def fin_vader(sentence):
    compound = finvader(sentence,
                        use_sentibignomics = True,
                        use_henry = True,
                        indicator = 'compound')

    return compound