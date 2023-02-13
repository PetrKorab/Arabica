Descriptive n-gram analysis
=====

**Arabica** takes text data as the input, enables standard cleaning operations,
and provides n-gram (unigram, bigram, and trigram) frequencies for the text dataset.

**arabica_freq** method with *time_freq = 'ungroup'* provides descriptive analysis for the most frequent n-grams.

It can apply all or a selected combination of the following cleaning operations:

* Remove digits from the text
* Remove punctuation from the text (using `cleantext <https://pypi.org/project/cleantext/#description>`_)
* Remove standard list of stop words (using `NLTK <https://www.nltk.org/>`_)
* Remove an additional specific list of words


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

* **lowercasing**: reviews are made lowercase - capital letters don't affect n-gram calculations (e.g., "Ginger" is not treated differently from "ginger")

* **punctuation** cleaning

* **digits** removal

* **stop words** removal

* **additional unnnecessary strings** removal

* n-gram frequencies for each headline are calculated and summed.

.. code-block:: python
   :linenos:

   arabica_freq(text = data['review'],
            time = data['time'],
            date_format = 'us',        # Uses US-style date format to parse dates
            time_freq = 'ungroup',     # Calculates n-grams frequencies without period aggregation
            max_words = 7,             # Displays 7 most frequent unigrams, bigrams, and trigrams
            stopwords = ['english'],   # Removes English set of stopwords
            skip = ['br'],             # Removes additional string
            numbers = True,            # Removes numbers
            punct = True,              # Removes punctuation
            lower_case = True)         # Lowercase text before cleaning and frequency analysis


The output is a dataframe with n-gram frequencies:

.. table::
   :align: left

+-----------------+---------------+-------------------------+---------------+-----------------------------+--------------+
| unigram         | unigram _freq | bigram                  | bigram_freq   | trigram                     | trigram_freq |
+=================+===============+==========================+===============+============================+==============+
| ginger          | 75            | crystallized,ginger     | 9             | health,food,store           | 3            |
+-----------------+---------------+----------------------------+------------+------------------------------+-------------+
| one             | 15            | ginger,candy            | 8             | charged,credit,card         | 2            |
+-----------------+---------------+-------------------------+---------------+-----------------------------+--------------+
| reeds           | 14            | reeds,ginger            | 5             | ginger,candy,would          | 2            |
+-----------------+---------------+-------------------------+---------------+-----------------------------+--------------+
| would           | 13            | crystalized,ginger      | 5             | ginger,unique,taste         | 2            |
+-----------------+---------------+-------------------------+---------------+-----------------------------+--------------+
| candy           | 11            | much,sugar              | 4             | ginger,peoples,organic      | 2            |
+-----------------+---------------+-------------------------+---------------+-----------------------------+--------------+
| love            | 11            | ginger,flavor           | 4             | half,sugar,much             | 1            |
+-----------------+---------------+-------------------------+---------------+-----------------------------+--------------+
| crystallized    | 11            | baby,ginger             | 4             | think,product,first         | 1            |
+-----------------+---------------+-------------------------+---------------+-----------------------------+--------------+


*The frequency of "love" and  "ginger, unique, taste" and no n-grams with negative meanings suggest that customers*
*perceived the product positively. The reasons might be less sugar and overall health effects - "half, sugar, much",*
*"health, food, store", and "much, sugar". A more detailed inspection should confirm this.*

Download the jupyter notebook with the code and the data `here <https://github.com/PetrKorab/Arabica/blob/main/docs/examples/arabica_freq_examples.ipynb>`_.
