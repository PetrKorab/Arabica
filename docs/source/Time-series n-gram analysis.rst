Time-series n-gram analysis
=====

**arabica_freq**  method takes text data, enables standard cleaning operations, and provides n-gram (unigram, bigram, and trigram) frequencies over a year, month, or day. 

It automatically cleans data from punctuation (using `cleantext <https://pypi.org/project/cleantext/#description>`_) on input. It can also apply all or a selected combination of the following cleaning operations:

* Remove digits from the text
* Remove standard list(s) of stop words (using `NLTK <https://www.nltk.org/>`_)
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

    stopwords = ['english', 'french','etc..']
    
    
--------


**Coding example**


**Use case:** Fake news in newspaper headlines during the Covid-19 pandemic

**Data**: Fake-Real News dataset, period: 2019-12-02: 2020-6-19, source: `Politifact.com <https://www.kaggle.com/datasets/techykajal/fakereal-news>`_,
data licence: `CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0/>`_.

**Coding**:

.. code-block:: python
   :linenos:

   import pandas as pd
   from arabica import arabica_freq

.. code-block:: python
   :linenos:

    data = pd.read_csv('headlines.csv', encoding='utf8')

The data looks like this:

.. csv-table::
   :header: "headline", "date"
   :widths: 88, 12
   :align: left

   "Illinois “got into fiscal problems because of a Republican governor who was governor there", "May 8, 2020"
   "Black cats in Vietnam are being killed and consumed as a COVID-19 cure ", "May 8, 2020"
   "Georgia Gov. Brian Kemp “mandates restaurants reopen", "May 8, 2020"
   "Central Park hospital tents housed thousands of abused children released from underground captivity", "May 8, 2020"
   "New autopsy reports suggest Jeffrey Epstein most likely died from COVID-19 complications", "May 8, 2020"

It procceeds in this way:

* **additional stop words** cleaning, if ``skip is not None``

* **stop words** removal, if ``stopwords is not None``

* **punctuation** cleaning - performs automatically

* **digits** removal, , if ``numbers = True``

* **lowercasing**: reviews are made lowercase so that capital letters don't affect n-gram calculations (e.g., "Tree" is not treated differently from "tree"), if ``lower_case = True``

* n-gram frequencies for each headline are calculated, summed, and aggregated by a specified frequency.


.. code-block:: python
   :linenos:

   arabica_freq(text = data['headline'],
                time = data['date'],
                date_format = 'us',          # Uses US-style date format to parse dates
                time_freq = 'M',             # Aggregation period: 'D' = daily, 'M' = monthly, 'Y' = yearly
                max_words = 3,               # Displays thee most n-grams for each period
                stopwords = ['english'],     # Remove English set of stopwords
                skip = ['<br />'],           # Remove additional stop words
                numbers = True,              # Remove numbers
                lower_case = True)           # Lowercase text


The output is a dataframe with n-grams in monthly frequency:

.. csv-table::
   :header: "period",	"unigram",	"bigram",	"trigram"
   :widths: 10, 20, 30, 45
   :align: left

   "2019-12", "says: 48,trump: 12,president: 12",	"says,photo: 6,donald,trump: 6,photo,shows: 5",	"says,photo,shows: 5,president,donald,trump: 4,dirtier,dirtier,dirtier: 2"
   "2020-01",	"says: 78,shows: 20,us: 17",	"video,shows: 8,says,photo: 7,kobe,bryant: 7",	"says,video,shows: 6,says,photo,shows: 6,iranian,rockets,launched: 4"
   "2020-02",	"says: 77,trump: 20,president: 18",	"bernie,sanders: 9,photo,shows: 8,nancy,pelosi: 8",	"says,photo,shows: 5,says,bernie,sanders: 4,works,white,house: 4"
   "2020-03",	"says: 81,coronavirus: 76,people: 29",	"joe,biden: 17,bernie,sanders: 12,donald,trump: 12",	"says,joe,biden: 6,president,donald,trump: 5,video,shows,joe: 3"
   "2020-04",	"says: 66,covid: 39,coronavirus: 31",	"new,york: 8,photo,shows: 5,feb,feb: 5",	"new,york,city: 4,says,video,shows: 3,feb,feb,feb: 3"
   "2020-05",	"says: 38,covid: 33,coronavirus: 21",	"joe,biden: 8,photo,shows: 8,donald,trump: 7",	"president,donald,trump: 5,says,president,donald: 4,says,gov,tony: 3"
   "2020-06",	"says: 31,trump: 17,police: 16",	"donald,trump: 11,last,year: 5,george,soros: 5",	"require,years,training: 3,training,people,killed: 3,people,killed,since: 3"




*The n-grams indicate that the key topics discussed in the headlines were the US presidential elections*
*until the break-up of Covid 19 in March 2020. In June 2020, George Soros and George Floyd's case dominated*
*the fake news in public debate.*


Download the jupyter notebook with the code and the data `here <https://github.com/PetrKorab/Arabica/blob/main/docs/examples/arabica_freq_examples.ipynb>`_.
