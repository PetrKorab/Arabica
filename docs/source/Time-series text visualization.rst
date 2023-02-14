Time-series text visualization
=====

**Arabica** provides n-gram visualization methods to describe the dataset
and discover variability over time.

**cappuccino** method enables standard cleaning operations (stop words, numbers, and punctuation removal),
and provides plots for descriptive (word cloud) and time-series (heatmap, line plot) text data visualization.

It can apply all or a selected combination of the following cleaning operations:

* Remove digits from the text
* Remove punctuation from the text (using `cleantext <https://pypi.org/project/cleantext/#description>`_)
* Remove standard list of stop words (using `NLTK <https://www.nltk.org/>`_)
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

    stopwords = ['language 1', 'language2','etc..']

-----------------------------------------


:doc:`Word cloud` is a graphical representation of word importance (typically frequencies) that give
greater prominence to words that appear more frequently in a source text.


:doc:`Heatmap` allows us to visualize n-grams through time. It divides the data into discrete categories
(boxes) by time and assigns a color to each category based on the value of the n-gram.


:doc:`Line plot` displays n-grams as a series of data points called 'markers' connected
by straight line segments. It is a basic type of chart common in many fields.
