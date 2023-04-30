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

    data = pd.read_csv('abcnews_data.csv', encoding='utf8')

The data looks liks this:

.. csv-table::
   :header: "headline", "date"
   :widths: 90, 10
   :align: left

   "aba decides against community broadcasting licence", 2003-2-19
   "act fire witnesses must be aware of defamation", 2003-2-19


It procceeds in this way:

* **additional unwanted strings** removal, if ``skip is not None``

* **stop words** removal, if ``stopwords is not None``

* **punctuation** cleaning - performs automatically

* **digits** removal, , if ``numbers = True``

* **lowercasing**: reviews are made lowercase so that capital letters don't affect n-gram calculations (e.g., "Tree" is not treated differently from "tree"), if ``lower_case = True``

* n-gram frequencies for each headline are calculated, summed, and displayed in a word cloud.


.. code-block:: python
   :linenos:

   cappuccino(text = data['headline'],
              time = data['date'],
              date_format = 'us',                 # Uses US-style date format to parse dates
              plot = 'wordcloud',
              ngram = 2,                          # N-gram size, 1 = unigram, 2 = bigram, 3 = trigram
              time_freq = 'ungroup',              # No period aggregation
              max_words = 150,                    # Displays 150 most frequent bigrams
              stopwords = ['english'],            # Remove English stopwords
              skip = ['covid','great day today'], # Remove additional unwanted strings
              numbers = True,                     # Remove numbers
              lower_case = True)                  # Lowercase text 

Here is the output:



.. image:: word_cloud_4.png
   :height: 500 px
   :width: 800 px
   :alt: alternate text
   :align: left

-----

Download the jupyter notebook with the code
and the data `here <https://github.com/PetrKorab/Arabica/blob/main/docs/examples/cappuccino_examples.ipynb>`_.
