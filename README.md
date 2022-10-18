# Arabica
**A Python package for exploratory analysis of text data**

Text data is often recorded as a time series with significant variability over time. Some examples of time-series text data include Twitter tweets, product reviews, and newspaper headlines. Arabica provides functions to make the exploratory analysis of such datasets simple.


Arabica provides these methods:

* **arabica_freq**: calculates unigram, bigram, and trigram frequencies over a period (year, month, day)

It can apply all or a selected combination of the following cleaning operations:

* Remove digits from the text
* Remove punctuation from the text
* Remove standard list of stopwords
* Remove an additional specific list of words

`arabica` uses `clean-text` for punctuation cleaning and `nltk` corpus of stopwords.

Arabica works with **texts** of languages based on the Latin alphabet and enables stopword removal for languages in the ntlk corpus of stopwords. 

It reads **dates** in standard date and datetime formats (e.g., 2013–12–31, 2013/12/31, 09-Feb-2009, 2013–12–31 11:46:17, 09/02/2009 09:26).
It is preferable to use the US-style dates (MM/DD/YYYY) rather than the European-style date format (DD/MM/YYYY) since there might be a mismatch between months and days in small datasets.

## Installation

Arabica requires [Python 3](https://www.python.org/downloads/),
[NLTK](http://www.nltk.org/install.html),
[clean-text](https://pypi.org/project/cleantext/#description),
[numpy](https://pypi.org/project/numpy/), and [ipython](https://pypi.org/project/ipython/) to execute. To install using pip, use:

`pip install arabica`



## Usage

* **Import the library**:


``` python
from arabica import arabica_freq
```



* **Choose a method:**

**arabica_freq** returns a dataframe with aggregated unigrams, bigrams, and trigrams frequencies over a period.
To remove stopwords, select aggregation period, and choose a specific set of cleaning operations:

``` python
def arabica_freq(text: str,                # Text
                 time: str,                # Time
                 stopwords: [],            # Languages for stop words
                 skip: [],                 # Strings to be skipped
                 punct: bool = False,      # Remove all punctuation
                 lower_case: bool = False, # Make all text lowercase before n-gram calculation
                 max_words: int ='',       # Max number for unigrams, bigrams and trigrams displayed
                 time_freq: str ='',       # Aggregation period: 'Y'/'M'/'D', if no aggregation: 'ungroup'
                 numbers: bool = False     # Remove all digits
) 
```

A list of available languages for stopwords is printed with:
``` python
from nltk.corpus import stopwords
print(stopwords.fileids())
```

It is possible to remove more sets of stopwords at once by `stopwords = ['language 1', 'language2','etc..']`

## Examples

### Time-series n-gram analysis

Returns a table with unigram, bigram, and trigram frequencies over a period of time.


``` python
import pandas as pd
from arabica import arabica_freq
```


``` python
data = pd.DataFrame({'text': ['The ordering process was very easy & straight forward. They have great customer service and sorted any issues out very quickly.',
                              'So far seems to be the wrong product for me :-/ grrrrr...',
                              'Excellent, service, thank you really, really, really much!!!'],
                     'time': ['2013-08-8', '2013-09-8','2014-10-8']})
```

``` python
arabica_freq(text = data['text'],
             time = data['time'],
             time_freq = 'M',           # Calculates monthly n-gram frequencies
             max_words = 2,             # Displays only the first two most frequent unigrams, bigrams, and trigrams
             stopwords = ['english'],   # Removes English set of stopwords
             skip = ['grrrrr'],         # Excludes string from n-gram calculation
             numbers = True,            # Removes numbers
             punct = True,              # Removes punctuation
             lower_case = True)         # Makes all text lowercase before n-gram calculation     
``` 

### Descriptive n-gram analysis

Returns unigram, bigram, and trigram frequencies without period aggregation.

``` python
arabica_freq(text = data['text'],
             time = data['time'],
             time_freq = 'ungroup',        # No aggregation made
             max_words = 2,
             stopwords = ['english'],
             skip = ['grrrrr'],       
             numbers = True,
             punct = True
             lower_case = True)
``` 

## Tutorial

For more examples of coding, read these tutorials:

**Text as Time Series: Arabica 1.0.0 Brings New Features for Exploratory Text Data Analysis** (forthcoming)

**Arabica: A Python Package for Exploratory Analysis of Text Data** [here](https://towardsdatascience.com/arabica-a-python-package-for-exploratory-analysis-of-text-data-3bb8d7379bd7?sk=cc91cabb56d44e0f285825d9a666b064)



## License

##### MIT

For any questions, issues, bugs, and suggestions, please visit [here](https://github.com/PetrKorab/arabica/issues).
