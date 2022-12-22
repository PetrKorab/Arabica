Word cloud
=====

**Word cloud** is a visual representation of n-grams that give greater importance to words that appear more
frequently in a source text. The bigger and bolder the n-gram appears, the more frequently it appears in the text.


Graph display unigrams (single words), bigrams, and trigrams for the source text.

---------------------------------------

**Coding example:**

**Use case:** Essential topics in newspaper headlines

**Data**: Million News Headlines dataset, source: `Australian Broadcasting Corporation <https://www.kaggle.com/datasets/therohk/million-headlines?resource=download>`_,
data licence: `CC0 1.0: Public Domain <https://creativecommons.org/publicdomain/zero/1.0/>`_.


Coding:

.. code-block:: python
   :linenos:

   import pandas as pd
   from arabica import cappuccino

.. code-block:: python
   :linenos:

    data = pd.read_csv('headlines.csv', encoding='utf8')
    data.head(5)


The data subset looks liks this:

+--------------------------------------------------------------------------------------------------------+------------+
| headline                                                                                               | date       |
+========================================================================================================+============+
|aba decides against community broadcasting licence                                                      | 2003-2-19  |
+--------------------------------------------------------------------------------------------------------+------------+
| act fire witnesses must be aware of defamation                                                         | 2003-2-19  |
+--------------------------------------------------------------------------------------------------------+------------+


The headlines are first made lowercase so that capital letters don't affect n-gram calculations (e.g., "Tree" is not
treated differently from "tree"). Next, the data is cleaned from punctuation, numbers, English stop words,
and additional strings ('zz top', 'donald trump'). Finally, n-gram frequencies for each headline are calculated,
summed, and displayed in a word cloud.


.. code-block:: python
   :linenos:

   cappuccino(text = data['headline'],
              time = data['date'],
              plot = 'wordcloud',
              ngram = 2,                        # N-gram size, 1 = unigram, 2 = bigram, 3 = trigram
              time_freq = 'ungroup',            # No period aggregation
              max_words = 150,                  # Displays 150 most frequent bigrams
              stopwords = ['english'],          # Remove English stopwords
              skip = ['zz top','donald trump'], # Remove additional strings
              numbers = True,                   # Remove numbers
              lower_case = True,                # Lowercase text before cleaning and frequency analysis
              punct = True)                     # Remove punctuation


Here is the output:



.. image:: word_cloud.png
   :height: 500 px
   :width: 800 px
   :alt: alternate text
   :align: left

-----

Download the jupyter notebook with the code
and the data `here <https://github.com/PetrKorab/Arabica/blob/main/docs/examples/cappuccino.ipynb>`_.