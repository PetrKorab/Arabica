Time-series n-gram analysis
=====

**Arabica** takes text data as the input, enables standard cleaning operations,
and provides n-gram (unigram, bigram, and trigram) frequencies over a specified period.

**arabica_freq** method calculates n-gram frequencies over a year, month, or day. It can apply all
or a selected combination of the following cleaning operations:

* Remove digits from the text
* Remove punctuation from the text (using `cleantext <https://pypi.org/project/cleantext/#description>`_)
* Remove standard list of stop words (using `NLTK <https://www.nltk.org/>`_) corpus of stop words
* Remove an additional specific list of words


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

The data looks like this:

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

It procceeds in this way:

* **lowercasing**: headlines are made lowercase - capital letters don't affect n-gram calculations (e.g., "Tree" is not treated differently from "tree")

* **punctuation** cleaning

* **digits** removal

* **stop words** removal

* **additional unnnecessary strings** removal

* n-gram frequencies for each headline are calculated, summed, and aggregated by a specified frequency.


.. code-block:: python
   :linenos:

   arabica_freq(text = data['headline'],
            time = data['date'],
            date_format = 'us',       # Uses US-style date format to parse dates
            time_freq = 'M',          # Calculates monthly n-gram frequencies
            max_words = 3,            # Displays  three most frequent unigrams, bigrams, and trigrams
            stopwords = ['english'],  # Removes English set of stopwords
            skip = ['grrrrr'],        # Removes additional string
            numbers = True,           # Removes numbers
            punct = True,             # Removes punctuation
            lower_case = True)        # Lowercase text before cleaning and frequency analysis


The output is a dataframe with trigrams in monthly frequency:

.. csv-table::
   :file: results.csv
   :widths: 10, 30, 30, 30
   :header-rows: 1


*The n-grams indicate that the key topics discussed in the headlines were the US presidential elections*
*until the break-up of Covid 19 in March 2020. In June 2020, George Soros and George Floyd's case dominated*
*the fake news in public debate.*


Download the jupyter notebook with the code and the data `here <https://github.com/PetrKorab/Arabica/blob/main/docs/examples/arabica_freq_examples.ipynb>`_.
