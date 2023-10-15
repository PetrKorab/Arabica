## Test replicates graphs in the paper submitted to JOSS - bigram word cloud, bigram heatmap, bigram line plot, 
## and line plot for financial sentiment analysis
## Graphs to be saved manually as .jpg/.png


import pandas as pd

data = pd.read_csv('data.csv', encoding = 'utf8')

# N-gram analysis: descriptive visualization
# Word cloud

from arabica import cappuccino

cappuccino(text = data['title'],
           time = data['publicationYear'],
           date_format = 'us',                # Uses US-style date format to parse dates
           plot = 'wordcloud',
           ngram = 2,                         # N-gram size, 1 = unigram, 2 = bigram, 3 = trigram
           time_freq = 'ungroup',             # No time aggregation
           max_words = 150,                   # Displays 150 most frequent bigrams
           stopwords = ['english'],           # Remove English stopwords
           skip = None,                       # Remove additional stop words
           numbers = True,                    # Remove numbers
           lower_case = True)                 # Lowercase text


print("word cloud generated, save manually as .jpg/.png")


# N-gram analysis: time-series visualization
# Heatmap
from arabica import cappuccino

cappuccino(text = data['title'],
           time = data['publicationYear'],
           date_format = 'us',                # Uses US-style date format to parse dates
           plot = 'heatmap',
           ngram = 2,                         # N-gram size, 1 = unigram, 2 = bigram
           time_freq = 'Y',                   # Aggregation period, 'M' = monthly, 'Y' = yearly
           max_words = 6,                     # Displays 6 most frequent bigrams for each period
           stopwords = ['english'],           # Remove English stopwords
           skip = None,                       # Remove additional stopwords
           numbers = True,                    # Remove numbers
           lower_case = True)                 # Lowercase text


print("heatmap generated, save manually as .jpg/.png")

# N-gram analysis: time-series visualization
# Line plot
from arabica import cappuccino

cappuccino(text = data['title'],
           time = data['publicationYear'],
           date_format = 'us',                # Uses US-style date format to parse dates
           plot = 'line',
           ngram = 1,                         # N-gram size, 1 = unigram, 2 = bigram
           time_freq = 'Y',                   # Aggregation period, 'M' = monthly, 'Y' = yearly
           max_words = 6,                     # Displays 6 most frequent bigrams for each period
           stopwords = ['english'],           # Remove English stopwords
           skip = None,                       # Remove additional stopwords
           numbers = True,                    # Remove numbers
           lower_case = True)                 # Lowercase text


print("lineplot generated, save manually as .jpg/.png")


# Financial sentiment and structural break analysis
# Line plot with two breakpoints

from arabica import coffee_break

coffee_break(text = data['title'],
             time = data['publicationYear'],
             date_format = 'us',               # Read dates in US format
             model = 'finvader',               # Use FinVADER sentiment classifier
             time_freq = 'Y',                  # Yearly aggregation
             preprocess = True,                # Clean data - digits and punctuation
             skip = None,                      # Remove additional stop words
             n_breaks = 2)                     # Find 2 breakpoints

print("lineplot with sentiment and breakpoint analysis results generated, save manually as .jpg/.png")
