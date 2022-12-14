Line plot
=====

**Line plot** displays n-grams as a series of data points connected by straight line segments.

Graph displays unigram (single words) and bigram frequencies over a monthly or yearly period, reflecting the time-series structure of the dataset.

-------------------------------------

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
    data.head(2)


The data subset looks like this:

+--------------------------------------------------------------------------------------------------------+------------+
| headline                                                                                               | date       |
+========================================================================================================+============+
|aba decides against community broadcasting licence                                                      | 2003-2-19  |
+--------------------------------------------------------------------------------------------------------+------------+
| act fire witnesses must be aware of defamation                                                         | 2003-2-19  |
+--------------------------------------------------------------------------------------------------------+------------+

The headlines are first made lowercase so that capital letters don't affect n-gram calculations (e.g., "Tree" is not
treated differently from "tree"). Next, the data is cleaned from punctuation, numbers, English stop words, and
additional strings ('zz top', 'donald trump'). Finally, n-gram frequencies for each headline are calculated,
aggregated by monthly frequency, and displayed in a line plot.

.. code-block:: python
   :linenos:

   cappuccino(text = data['headline'],
              time = data['date'],
              plot = 'line',
              ngram = 1,                        # N-gram size, 1 = unigram, 2 = bigram
              time_freq = 'M',                  # Aggregation period, 'M' = monthly, 'Y' = yearly
              max_words = 8,                    # Displays 8 most frequent unigrams for each period
              stopwords = ['english'],          # Remove English stopwords
              skip = ['zz top','donald trump'], # Remove additional strings
              numbers = True,                   # Remove numbers
              lower_case = True,                # Lowercase text before cleaning and frequency analysis
              punct = True)                     # Remove punctuation


Here is the output:



.. image:: line_plot_2.png
   :height: 450 px
   :width: 835 px
   :alt: alternate text
   :align: left


-----

Download the jupyter notebook with the code
and the data `here <https://github.com/PetrKorab/Arabica/blob/main/docs/examples/cappuccino.ipynb>`_.
