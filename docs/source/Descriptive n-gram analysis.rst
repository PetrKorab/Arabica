Descriptive n-gram analysis
=====

**Arabica** takes text data as the input, enables standard cleaning operations,
and provides n-gram (unigram, bigram, and trigram) frequencies for the text dataset.

**arabica_freq** method calculates unigram, bigram, and trigram frequencies. It can apply all or a selected combination of the following cleaning operations:

* Remove digits from the text
* Remove punctuation from the text (using `cleantext <https://pypi.org/project/cleantext/#description>`_)
* Remove standard list of stop words (using `NLTK <https://docs.python.org/3.8/library/datetime.html>`_)
* Remove an additional specific list of words

*Stop words* are generally the most common words in a language with no significant meaning, such as *"is"*, *"am"*, *"the"*, *"this"*, *"are"*, etc.
They are often filtered out because they bring low or zero information value.

^^^^^^
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

    data = pd.read_csv('amazon.csv', encoding='utf8')
    data.head(2)


By randomly picking a product from the reviews, a subset of 25 reviews looks like this:

+---------------------------------------------------------------------------------------------------------+------------+
| review                                                                                                  | time       |
+=========================================================================================================+============+
| You may find yourself trying to decide between comparable crystallized ginger offerings from Reeds and  | 19/08/2010 |
| The Ginger People. Which one should you choose? I have now tried both, and here is how they compare.    |            |
| <br /><br />Reed's has a lovely raw cane sugar flavor, and is sweeter and more mellow than The Ginger   |            |
| People's.<br /><br />If you want something a little less sweet (still sweet though--it is crystallized  |            |
| ginger, after all) and a little spicier, go for The Ginger People.                                      |            |
+---------------------------------------------------------------------------------------------------------+------------+
| On the Reeds website, this same product is available for $16.00.<br /><br />"Reed's Crystallized Ginger | 05/06/2009 |
| Candy 12 - 3.5 oz Bags"                                                                                 |            |
+---------------------------------------------------------------------------------------------------------+------------+

The **arabica_freq** method with *time_freq = 'ungroup'* provides a descriptive analysis by returning unigram, bigram,
and trigram frequencies for the most frequent n-grams specified by the *'max_words'* parameter.

The data subset contains a lot of unnecessary strings. Arabica **cleans the data** from punctuation and numbers and removes
the English set of stopwords. In the beginning, the text is also made lowercase so that capital letters don't affect
n-gram calculations (e.g., "Tree" is not treated differently from "tree"). We also want to remove a specific string as
part of data cleaning ('br'):

.. code-block:: python
   :linenos:

   arabica_freq(text = data['headline'],
            time = data['date'],
            time_freq = 'ungroup',     # Calculates n-grams frequencies without period aggregation
            max_words = 7,             # Displays only the first two most frequent unigrams, bigrams, and trigrams
            stopwords = ['english'],   # Removes English set of stopwords
            skip = ['grrrrr'],         # Excludes string from n-gram calculation
            numbers = True,            # Removes numbers
            punct = True,              # Removes punctuation
            lower_case = True)         # Makes all text lowercase before n-gram calculation


Here is the output:

+-------------+---------------+----------------------+-------------+--------------------------+---------------+
|unigram      | unigram _freq | bigram               | bigram_freq | trigram                  | trigram_freq  |
+=============+===============+======================+=============+==========================+===============+
|ginger       |75             | crystallized, ginger | 9           | health, food, store      | 3             |
+-------------+---------------+----------------------+-------------+--------------------------+---------------+
|one          |15             | ginger, candy        | 8           | charged, credit, card    | 2             |
+-------------+---------------+----------------------+-------------+--------------------------+---------------+
|reeds        | 14            | reeds, ginger        | 5           | ginger, candy, would     | 2             |
+-------------+---------------+----------------------+-------------+--------------------------+---------------+
|would        | 13            | crystalized, ginger  | 5           | ginger, unique, taste    | 2             |
+-------------+---------------+----------------------+-------------+--------------------------+---------------+
|candy        | 11            | much, sugar          | 4           | ginger, peoples, organic | 2             |
+-------------+---------------+----------------------+-------------+--------------------------+---------------+
|love         | 11            | ginger, flavor       | 4           | half, sugar, much        | 1             |
+-------------+---------------+----------------------+-------------+--------------------------+---------------+
|crystallized | 11            | baby, ginger         | 4           | think, product, first    | 1             |
+-------------+---------------+----------------------+-------------+--------------------------+---------------+

**Results interpretation**

The frequency of *"love"* and  *"ginger, unique, taste"* and no n-grams with negative meanings suggest that customers
perceived the product positively. The reasons might be less sugar and overall health effects - *"half, sugar, much"*,
*"health, food, store"*, and *"much, sugar"*. A more detailed inspection should confirm this.

Download the jupyter notebook with the code and the data `here <https://github.com/PetrKorab/Arabica/blob/main/docs/examples/examples.ipynb>`_.