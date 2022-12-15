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

The data subset contains lots of unnecessary strings. Arabica lowercases the text,
so that capital letters don't affect n-gram calculations (e.g., "Tree" is not treated
differently from "tree"). In the next step, it **cleans the data** from punctuation
and numbers and removes the English set of stopwords. We also remove a specific
string ('grrrrr') as part of data cleaning:

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

.. csv-table::
   :file: results.csv
   :widths: 8, 30, 32, 30
   :header-rows: 1


*The n-grams indicate that the key topics discussed in the headlines were the US presidential elections*
*until the break-up of Covid 19 in March 2020. In June 2020, George Soros and George Floyd's case dominated*
*the fake news in public debate.*


Download the jupyter notebook with the code and the data `here <https://github.com/PetrKorab/Arabica/blob/main/docs/examples/examples.ipynb>`_.