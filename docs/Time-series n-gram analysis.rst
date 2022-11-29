Time-series n-gram analysis
=====

**Arabica** takes text data as the input, enables standard cleaning operations,
and provides n-gram (unigram, bigram, and trigram) frequencies over a specified period.

**arabica_freq** method calculates unigram, bigram, and trigram frequencies over a period (year, month, day). It can apply all or a selected combination of the following cleaning operations:

* Remove digits from the text
* Remove punctuation from the text (using `cleantext <https://pypi.org/project/cleantext/#description>`_)
* Remove standard list of stop words (using `NLTK <https://www.nltk.org/>`_) corpus of stop words
* Remove an additional specific list of words

^^^^^^
Coding example
^^^^^^

**Use case:** Fake news in newspaper headlines during the Covid-19 pandemic

**Data**: Fake-Real News dataset, period: 2019-12-02: 2020-6-19, source: `Politifact.com <https://www.kaggle.com/datasets/techykajal/fakereal-news>`_,
data licence: `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_.

**Coding**:

.. code-block:: python
   :linenos:

   import pandas as pd
   from arabica import arabica_freq

.. code-block:: python
   :linenos:

    data = pd.read_csv('headlines.csv', encoding='utf8')
    data.head(5)


The data subset looks liks this:

+---------------------------------------------------------------------------------------------------------+--------------+
| headline                                                                                                | date         |
+=========================================================================================================+==============+
|Illinois “got into fiscal problems because of a Republican governor who was governor there”              | May 8, 2020  |
+---------------------------------------------------------------------------------------------------------+--------------+
| Black cats in Vietnam are being killed and consumed as a COVID-19 cure.                                 | May 8, 2020  |
+---------------------------------------------------------------------------------------------------------+--------------+
| Georgia Gov. Brian Kemp “mandates restaurants reopen”                                                   | May 8, 2020  |
+---------------------------------------------------------------------------------------------------------+--------------+
| Central Park hospital tents housed thousands of abused children released from underground captivity.    | May 8, 2020  |
+---------------------------------------------------------------------------------------------------------+--------------+
| “New autopsy reports suggest Jeffrey Epstein most likely died from COVID-19 complications.”             | May 8, 2020  |
+---------------------------------------------------------------------------------------------------------+--------------+

Arabica **cleans the data** from punctuation and numbers and removes the English set of stopwords. In the beginning,
the text is also made lowercase so that capital letters don't affect n-gram calculations (e.g., "Tree" is not
treated differently from "tree"). We also want to remove a specific string as part of data cleaning ('grrrrr').

The headlines are aggregated by monthly frequency, and the table shows the first three most frequent n-grams:

.. code-block:: python
   :linenos:

   arabica_freq(text = data['headline'],
            time = data['date'],
            time_freq = 'M',           # Calculates monthly n-gram frequencies
            max_words = 3,             # Displays only the first three most frequent unigrams, bigrams, and trigrams
            stopwords = ['english'],   # Removes English set of stopwords
            skip = ['grrrrr'],         # Excludes string from n-gram calculation
            numbers = True,            # Removes numbers
            punct = True,              # Removes punctuation
            lower_case = True)         # Makes all text lowercase before n-gram calculation


Here is the output:

+---------+-----------------+--------------------+----------------------------+
| period  |unigram          | bigram             | trigram                    |
+=========+=================+====================+============================+
| 2019-12 |says: 48,        |says,photo: 6,      |says,photo,shows: 5,        |
|         |trump: 12,       |donald,trump: 6,    |president,donald,trump: 4,  |
|         |president: 12    |photo,shows: 5      |dirtier,dirtier,dirtier: 2  |
+---------+-----------------+--------------------+----------------------------+
| 2020-01 |says: 78,        |video,shows: 8,     |says,video,shows: 6,        |
|         |shows: 20,       |says,photo: 7,      |says,photo,shows: 6,        |
|         |us: 17           |kobe,bryant: 7      |iranian,rockets,launched: 4 |
+---------+-----------------+--------------------+----------------------------+
| 2020-02 |says: 77,        |bernie,sanders: 9,  |says,photo,shows: 5,        |
|         |trump: 20,       |photo,shows: 8      |says,bernie,sanders: 4,     |
|         |president: 18    |nancy,pelosi: 8     |works,white,house: 4        |
+---------+-----------------+--------------------+----------------------------+
| 2020-03 |says: 81,        |joe,biden: 17,      |says,joe,biden: 6,          |
|         |coronavirus: 76, |bernie,sanders: 12, |president,donald,trump: 5,  |
|         |people: 29       |donald,trump: 12    |video,shows,joe: 3          |
+---------+-----------------+--------------------+----------------------------+
| 2020-04 |says: 66,        |new,york: 8,        |new,york,city: 4,           |
|         |covid: 39,       |photo,shows: 5,     |says,video,shows: 3,        |
|         |coronavirus: 31  |feb,feb: 5          |feb,feb,feb: 3              |
+---------+-----------------+--------------------+----------------------------+
| 2020-05 |says: 38,        |joe,biden: 8,       |president,donald,trump: 5,  |
|         |covid: 33,       |photo,shows: 8,     |says,president,donald: 4,   |
|         |coronavirus: 21  |donald,trump: 7     |says,gov,tony: 3            |
+---------+-----------------+--------------------+----------------------------+
| 2020-06 |says: 31,        |donald,trump: 11,   |require,years,training: 3,  |
|         |trump: 17,       |last,year: 5,       |training,people,killed: 3,  |
|         |police: 16       |george,soros: 5     |people,killed,since: 3      |
+---------+-----------------+--------------------+----------------------------+

-------

*The n-grams indicate that the key topics discussed in the headlines were the US presidential elections*
*until the break-up of Covid 19 in March 2020. In June 2020, George Soros and George Floyd's case dominated*
*the fake news in public debate.*


Download the jupyter notebook with the code and the data `here <https://github.com/PetrKorab/Arabica/blob/main/docs/examples/examples.ipynb>`_.