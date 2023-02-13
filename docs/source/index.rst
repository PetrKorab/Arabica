.. Arabica documentation master file, created by
   sphinx-quickstart on Sat Nov 19 22:00:38 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Arabica's documentation!
===================================
**Arabica** is a Python library for exploratory data analysis specifically designed for time-series text data.
It reflects the reality that many text datasets are currently collected as repeated observations over time (product reviews, communication on social media, article headlines, etc.).

Arabica makes exploratory analysis of these datasets simple by providing:

- **Descriptive n-gram analysis**: n-gram frequencies
- **Time-series n-gram analysis**: n-gram frequencies over a period

*N-grams* are continuous sequences of words in a document. In technical terms, they are the neighboring sequences of items in a text.
Some examples include:

* **unigram**: "dog", **bigram**: "dog, goes", **trigram**: "dog, goes, home"
* **unigram**: "flower", **bigram**: "flower, grows", **trigram**: "flower, grows, here"


Contents
--------

.. toctree::

   Installation
   Backend model
   Descriptive n-gram analysis
   Time-series n-gram analysis
   Time-series text visualization
   Word cloud
   Heatmap
   Line plot two
