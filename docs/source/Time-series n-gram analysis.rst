Time-series n-gram analysis
=====

**Arabica** takes text data as the input, enables standard cleaning operations,
and provides n-gram (unigram, bigram, and trigram) frequencies over a specified period.

**arabica_freq** method calculates unigram, bigram, and trigram frequencies over a period (year, month, day). It can apply all or a selected combination of the following cleaning operations:

* Remove digits from the text
* Remove punctuation from the text (using `cleantext <https://pypi.org/project/cleantext/#description>`_)
* Remove standard list of stop words (using `NLTK <https://docs.python.org/3.8/library/datetime.html>`_) corpus of stop words
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

+---------+-------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------+
|period   | unigram                             |bigram                                           | trigram                                                                   |
+=========+=====================================+=================================================+===========================================================================+
|2019-12  |says: 48,trump: 12,president: 12     |says,photo: 6,donald,trump: 6,photo,shows: 5     | says,photo,shows: 5,president,donald,trump: 4,dirtier,dirtier,dirtier: 2  |
+---------+-------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------+
|2020-01  |says: 78,shows: 20,us: 17            |video,shows: 8,says,photo: 7,kobe,bryant: 7      | says,video,shows: 6,says,photo,shows: 6,iranian,rockets,launched: 4       |
+---------+-------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------+
|2020-02  | says: 77,trump: 19,president: 17    |photo,shows: 8,bernie,sanders: 8,says,photo: 7   | says,photo,shows: 5,works,white,house: 4,says,bernie,sanders: 4           |
+---------+-------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------+
|2020-03  | says: 81,coronavirus: 64,people: 23 |joe,biden: 14,bernie,sanders: 10,donald,trump: 8 | president,donald,trump: 4,says,joe,biden: 4,says,president,donald: 3      |
+---------+-------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------+
|2020-04  | says: 66,covid: 39,coronavirus: 29  |new,york: 8,feb,feb: 5,photo,shows: 5            | new,york,city: 4,says,video,shows: 3,feb,feb,feb: 3                       |
+---------+-------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------+
|2020-05  | says: 38,covid: 32,coronavirus: 20  |joe,biden: 8,photo,shows: 8,donald,trump: 7      | president,donald,trump: 5,says,president,donald: 4,says,gov,tony: 3       |
+---------+-------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------+
|2020-06  | says: 31,police: 16,trump: 13       |donald,trump: 9,people,killed: 4,george,floyd: 4 | require,years,training: 3,training,people,killed: 3,black,lives,matter: 3 |
+---------+-------------------------------------+-------------------------------------------------+---------------------------------------------------------------------------+

------------

*The n-grams indicate that the key topics discussed in the headlines were the US presidential elections until the break-up of*
*covid in March 2020. In June 2020, George Floyd's case dominated the public debate. The topics in the discussion are revealed*
*in more detail in the bigram and trigram columns.*

*To develop the project further, one can pre-process the data and keep only the headlines labeled as fake in the original dataset.*
*In this way, we can identify the evolution of the key topics related to fake news.*


Download the jupyter notebook with the code and the data `here <https://github.com/PetrKorab/Arabica/blob/main/docs/examples/examples.ipynb>`_.