.. Arabica documentation master file, created by
   sphinx-quickstart on Sat Nov 19 22:00:38 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Arabica's documentation!
===================================
**Arabica** is a python library for exploratory data analysis specifically designed for time-series text data.
It reflects the reality that many text datasets are now collected as repeated observations over time (social media conversations, 
research metadata, product reviews, newspaper headlines, central bankers' communication, etc.).

* **Descriptive n-gram analysis**: n-gram frequencies
* **Time-series n-gram analysis**: n-gram frequencies over a period
* **Text visualization**: n-gram heatmap, line plot, word cloud
* **Sentiment analysis**: VADER sentiment classifier
* **Financial sentiment analysis**: with FinVADER
* **Structural breaks identification**: Jenks Optimisation Method

*N-grams* are continuous sequences of words in a document. Technically, they are the neighboring sequences of items in a text.
Some examples include:

* **unigram**: "dog", **bigram**: "dog, goes", **trigram**: "dog, goes, home"
* **unigram**: "flower", **bigram**: "flower, grows", **trigram**: "flower, grows, here"


Contents
--------

.. toctree::

   Installation
   Library architecture
   Descriptive n-gram analysis
   Time-series n-gram analysis
   Time-series text visualization
   Word cloud
   Heatmap
   Line plot
   Sentiment analysis
   Structural break analysis
   Breakpoint identification
   Use cases and tutorials
   
------


I have created this project in my free time, and I hope Arabica will save you some time. You can `invite me for coffe <https://www.buymeacoffee.com/PetrKorab>`_ if Arabica helps you with your project, thesis, or research paper.
