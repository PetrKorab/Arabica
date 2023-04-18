Descriptive n-gram analysis
=====

**arabica_freq** method takes text data, enables standard cleaning operations, and with *time_freq = 'ungroup'* provides descriptive analysis for the most frequent words, bigrams, and trigrams.

It automatically cleans data from punctuation (using `cleantext <https://pypi.org/project/cleantext/#description>`_) on input. It can also apply all or a selected combination of the following cleaning operations:

* Remove digits from the text
* Remove standard list(s) of stop words (using `NLTK <https://www.nltk.org/>`_)
* Remove an additional specific list of words


**Stop words** are generally the most common words in a language with no significant meaning, such as *"is"*, *"am"*, *"the"*, *"this"*, *"are"*, etc.
They are often filtered out because they bring low or zero information value. Arabica enables stopword removal for languages in the
`NLTK <https://www.nltk.org/>`_ corpus.

To print all available languages:

.. code-block:: python
   :linenos:

    from nltk.corpus import stopwords
    print(stopwords.fileids())


It is possible to remove more sets of stopwords at once by:

.. code-block:: python
   :linenos:

    stopwords = ['english', 'french','etc..']


Coding example
^^^^^^

**Use case:** Customer perception of Amazon products

**Data**: Amazon Product Reviews dataset, source: `Amazon.com <https://www.kaggle.com/datasets/arhamrumi/amazon-product-reviews>`_,
data licence: `CC0: Public Domain <https://creativecommons.org/publicdomain/zero/1.0/>`_.

**Coding**:

.. code-block:: python
   :linenos:

   import pandas as pd
   from arabica import arabica_freq

.. code-block:: python
   :linenos:

    data = pd.read_csv('reviews_subset.csv',encoding='utf8')

By randomly picking a product from the reviews, a subset of 25 reviews looks like this:

.. csv-table::
   :file: subset.csv
   :widths: 5, 95
   :header-rows: 1
   :align: left

It procceeds in this way:

* **additional unwanted strings** removal, if ``skip is not None``

* **stop words** removal, if ``stopwords is not None``

* **lowercasing**: reviews are made lowercase so that capital letters don't affect n-gram calculations (e.g., "Tree" is not treated differently from "tree"), if ``lower_case = True``

* **punctuation** cleaning - performs automatically

* **digits** removal, , if ``numbers = True``

* n-gram frequencies for each headline are calculated and summed for the whole dataset.

.. code-block:: python
   :linenos:

   arabica_freq(text = data['review'],
                 time = data['time'],
                 date_format = 'us',         # Uses US-style date format to parse dates
                 time_freq = 'ungroup',      # Calculate n-grams frequencies without period aggregation
                 max_words = 10,             # Display 10 most frequent unigrams, bigrams, and trigrams
                 stopwords = ['english'],    # Remove English set of stopwords
                 skip = ['grrrrr', 'ZZ Top]  # Remove additional strings
                 numbers = True,             # Remove numbers
                 lower_case = True)          # Lowercase text

The output is a dataframe with n-gram frequencies:

.. csv-table::
   :file: descriptive_results_GOOD_2.csv
   :widths: 17, 17, 20, 17, 20, 17
   :header-rows: 1

*The frequency of "love" and  "ginger, unique, taste" and no n-grams with negative meanings suggest that customers*
*perceived the product positively. The reasons might be less sugar and overall health effects - "health,food",*
*"much,sugar", and "good,without,much". A more detailed inspection should confirm this.*

Download the jupyter notebook with the code and the data `here <https://github.com/PetrKorab/Arabica/blob/main/docs/examples/arabica_freq_examples.ipynb>`_.
