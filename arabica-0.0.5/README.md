# Arabica
**A Python package for exploratory analysis of text data**

Text data is often recorded as a time series with significant variability over time. Some examples of time-series text data include Twitter tweets, product reviews, and newspaper headlines. Arabica provides functions to make the exploratory analysis of such datasets simple.


Arabica provides these methods:

* **arabica_freq**: calculates unigram, bigram, and trigram frequencies over a period (year, month)

It can apply all or a selected combination of the following cleaning operations:

* Remove digits from the text
* Remove punctuation from the text
* Remove standard list of stopwords

`arabica` uses `clean-text` for punctuation cleaning and `nltk` corpus of stopwords.



## Installation

Arabica requires [Python 3](https://www.python.org/downloads/), 
[NLTK](http://www.nltk.org/install.html), and
[clean-text](https://pypi.org/project/cleantext/#description), to execute. To install using pip, use:

`pip install arabica`



## Usage

* **Import the library**:


``` python
from arabica import arabica_freq

```



* **Choose a method:**

Arabica returns a dataframe with aggregated unigrams, bigrams, and trigrams frequencies over a period.
To remove stopwords, select aggregation period, and choose a specific set of cleaning operations:

``` python
def arabica_freq(text: str, # Text
                 time: str, # Time
                 stopwords: str, # Language for stop words
                 punct: bool = False, # Remove all punctuation
                 max_words: int='', # Max number for unigrams, bigrams and trigrams displayed
                 time_freq: str='', # Aggregation period, 'Y'/'M'
                 numbers: bool = False # Remove all digits
) 
```

## Example


``` python
import pandas as pd
from arabica import arabica_freq
```


``` python
data = pd.DataFrame({'text': ['The ordering process was very easy & straight forward. They have great customer service and sorted any issues out very quickly.',
                              'So far seems to be the wrong product for me :-/',
                              'Excellent, service, thank you really, really, really much!!!'],
                     'time': ['2013-08-8', '2013-09-8','2014-10-8']})



```

``` python
arabica_freq(text= data['text'],time=data['time'],time_freq='M',max_words=2,stopwords='english', numbers = True, punct=True)
``` 

## Tutorial

For more examples of coding, read a tutorial here.



## License

##### MIT

For any questions, issues, bugs, and suggestions, please visit [here](https://github.com/PetrKorab/arabica/issues)
