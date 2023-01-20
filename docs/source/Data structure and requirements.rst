Data structure and requirements
=====

**Arabica** accepts text and time columns as inputs:

- **Text** is a written record (speech, review, title, article, ..)

- **Time** is a time specification for the recorded text

Latin alphabet languages (English, French, Swedish, etc.) are supported.

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

It reads dates in the US-style (MM/DD/YYYY, e.g., *2013–12–31, Feb-09-2009, 2013–12–31 11:46:17*) and European-style (DD/MM/YYYY, e.g., *2013–31–12, 09-Feb-2009, 2013–31–12 11:46:17*) date and datetime formats.

These aggregation combinations are provided:

* input time in **second frequency** - aggregated daily, monthly, and yearly output
* input time in **daily frequency** - aggregated monthly, yearly output
* input time in **monthly frequency** - aggregated yearly output
* input time in **yearly frequency** - aggregated yearly output

For :doc:`Descriptive n-gram analysis`, we don't aggregate data over time and make exploratory data analysis of the whole text corpus.
