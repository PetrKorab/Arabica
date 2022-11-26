Data structure and requirements
=====

**Arabica** accepts **text** and **time** collumns as inputs:

- **Text** is a written record (speech, review, title, article, ..).

Latin alphabet languages (English, French, Swedish, etc.) are supported. Arabica also enables stopword removal for languages in the `NLTK <https://docs.python.org/3.8/library/datetime.html>`_ corpus of stop words.

- **Time** is a time specification for the recorded text.

Arabica reads dates in standard `date and datetime formats <https://docs.python.org/3.8/library/datetime.html>`_.
These aggregation combinations are provided:

* input time in **second frequency** - aggregated daily, monthly, yearly output
* input time in **daily frequency** - aggregated monthly, yearly output
* input time in **monthly frequency** - aggregated yearly output
* input time in **yearly frequency** - aggregated yearly output

It is recommended to use the US-style dates (MM/DD/YYYY) rather than the European style (DD/MM/YYYY) since Arabica might make a mismatch between months and days in small and incomplete datasets.

For descriptive analysis (:doc:`Descriptive n-gram analysis`), we don't aggregate data over time and make exploratory data analysis of the whole text corpus.










