Library architecture
=====

**Arabica** accepts text and time columns as inputs:

- **Text** is a written record (speech, review, title, article, ..)

- **Time** is a time specification for the recorded text

It reads dates in:

- **US-style**: MM/DD/YYYY (2013-12-31, Feb-09-2009, 2013-12-31 11:46:17, etc.)
- **European-style**: DD/MM/YYYY (2013-31-12, 09-Feb-2009, 2013-31-12 11:46:17, etc.) date and datetime formats.

Latin alphabet languages (English, French, Swedish, etc.) are supported.

These aggregation combinations are provided:

* input time in **second frequency** - aggregated daily, monthly, and yearly output
* input time in **daily frequency** - aggregated monthly, yearly output
* input time in **monthly frequency** - aggregated yearly output
* input time in **yearly frequency** - aggregated yearly output

In :doc:`Descriptive n-gram analysis`, we don't aggregate data over time and make exploratory analysis of the whole dataset.

.

.. image:: arabica_backend_FULL.png
   :height: 450 px
   :width: 800 px
   :alt: alternate text
   :align: center
