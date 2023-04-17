# Arabica
**Python package for exploratory text data analysis**

Text data is often recorded as a time series with significant variability over time. Some examples of time-series text data include Twitter tweets, research article metadata, product reviews, and newspaper headlines. Arabica makes exploratory analysis of these time-series text datasets simple by providing:

* **Descriptive n-gram analysis**: n-gram frequencies
* **Time-series n-gram analysis**: n-gram frequencies over a period
* **Text visualization**: n-gram heatmap, line plot, word cloud
* **Sentiment analysis**: VADER sentiment classifier
* **Structural breaks identification**: Jenks Optimization Method

It automatically cleans data from punctuation on input. It can also apply all or a selected combination of the following cleaning operations:

* Remove digits from the text
* Remove the standard list(s) of stopwords
* Remove an additional list of specific strings

Arabica works with **texts** of languages based on the Latin alphabet, uses `cleantext` for punctuation cleaning, and enables stop words removal for languages in the `NLTK` corpus of stopwords.

It reads dates in:

* **US-style**: *MM/DD/YYYY* (2013-12-31, Feb-09-2009, 2013-12-31 11:46:17, etc.)
* **European-style**: *DD/MM/YYYY* (2013-31-12, 09-Feb-2009, 2013-31-12 11:46:17, etc.) date and datetime formats.


## Installation

Arabica requires [Python 3.8 - 3.10](https://www.python.org/downloads/), [NLTK](http://www.nltk.org) - stop words removal,
[cleantext](https://pypi.org/project/cleantext/#description) - text cleaning, [wordcloud](https://pypi.org/project/wordcloud) - word cloud visualization,
[plotnine](https://pypi.org/project/plotnine) - heatmaps and line graphs, [matplotlib](https://pypi.org/project/matplotlib/) - word clouds and graphical operations,
[vaderSentiment](https://pypi.org/project/vaderSentiment) - sentiment analysis, and [jenskpy](https://pypi.org/project/jenkspy/) for breakpoint identification.

To install using pip, use:

`pip install arabica`



## Usage

* **Import the library**:


``` python
from arabica import arabica_freq
from arabica import cappuccino
from arabica import coffee_break 
```



* **Choose a method:**

**arabica_freq** enables a specific set of cleaning operations (lower casing, numbers, stop words, and additional strings 
removal) and returns a dataframe with aggregated unigrams, bigrams, and trigrams frequencies over a period.



``` python
def arabica_freq(text: str,                # Text
                 time: str,                # Time
                 date_format: str,         # Date format: 'eur' - European, 'us' - American
                 time_freq: str = '',      # Aggregation period: 'Y'/'M'/'D', if no aggregation: 'ungroup'
                 max_words: int = '',      # Maximum of most frequent n-grams displayed for each period
                 stopwords: [],            # Languages for stop words
                 skip: [],                 # Remove additional strings
                 numbers: bool = False,    # Remove all digits
                 lower_case: bool = False  # Lowercase text
) 
```

**cappuccino**  enables cleaning operations (lower casing, numbers, stop words, and additional strings
removal) and provides plots for descriptive (word cloud) and time-series (heatmap, line plot) visualization.

``` python
def cappuccino(text: str,                # Text
               time: str,                # Time
               date_format: str,         # Date format: 'eur' - European, 'us' - American
               plot: str = '',           # Chart type: 'wordcloud'/'heatmap'/'line'
               ngram: int = '',          # N-gram size, 1 = unigram, 2 = bigram, 3 = trigram
               time_freq: str = '',      # Aggregation period: 'Y'/'M', if no aggregation: 'ungroup'
               max_words int = '',       # Maximum of most frequent n-grams displayed for each period
               stopwords: [],            # Languages for stop words
               skip: [] ,                # Remove additional strings
               numbers: bool = False,    # Remove numbers
               lower_case: bool = False  # Lowercase text
```

**coffee_break**  provides sentiment analysis and breakpoint identification in aggregated time series of sentiment. 

* The implemented model is **VADER** (Valence Aware Dictionary and sEntiment Reasoner), a lexicon and rule-based sentiment classifier attuned explicitly to sentiments expressed in social media. See: *Hutto, & Gilbert, 2014. VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.* Available from [here](https://ojs.aaai.org/index.php/ICWSM/article/view/14550).

* Structural breaks in the time series are identified with the **Fisher-Jenks algorithm** (Jenks, 1977. Optimal data classification for choropleth maps).


``` python
def coffee_break(text: str,                 # Text
                 time: str,                 # Time
                 date_format: str,          # Date format: 'eur' - European, 'us' - American
                 skip: [] ,                 # Remove additional strings
                 preprocess: bool = False,  # Clean data from numbers and punctuation
                 time_freq: str ='',        # Aggregation period: 'Y'/'M'
                 n_breaks: int =''          # Number of breaks: min. 2
)
```

## Documentation, examples and tutorials

* Read the [documentation](https://arabica.readthedocs.io/en/latest/index.html)

For more examples of coding, read these  tutorials:

**General use:**

* Sentiment Analysis and Structural Breaks in Time-Series Text Data [here](https://medium.com/towards-data-science/sentiment-analysis-and-structural-breaks-in-time-series-text-data-8109c712ca2)                        
* Visualization Module in Arabica Speeds Up Text Data Exploration [here](https://medium.com/towards-data-science/visualization-module-in-arabica-speeds-up-text-data-exploration-47114ad646ce)                                                                                                                          
* Text as Time Series: Arabica 1.0 Brings New Features for Exploratory Text Data Analysis [here](https://towardsdatascience.com/text-as-time-series-arabica-1-0-brings-new-features-for-exploratory-text-data-analysis-88eaabb84deb?sk=229ec0602d0b8514f25bce501ed9ecb9)   

**Applications:**

* **Business Intelligence:** Customer Satisfaction Measurement with N-gram and Sentiment Analysis [here](https://towardsdatascience.com/customer-satisfaction-measurement-with-n-gram-and-sentiment-analysis-547e291c13a6)                       
* **Meta-data description:** TBA

---

Please visit [here](https://github.com/PetrKorab/arabica/issues) for any questions, issues, bugs, and suggestions.
