## Test for visualization method: cappuccino
## It relies on the n-gram frequency matrix from arabica_freq
## n-gram frequencies are visualised with Matplotlib or Plotnine


import unittest
import pandas as pd
from arabica import cappuccino

class TestCappuccinoFunction(unittest.TestCase):

    data = pd.DataFrame({
        'text': ["You may find yourself trying to decide between comparable crystallized ginger offerings from Reeds",
                 "Reed’s has a lovely raw cane sugar flavor, and is sweeter and more mellow than The Ginger People’s."],
        'time': ["2016-08-30", "2016-08-31"]})


def test_cappuccino_wordcloud(self):
    # Provide test input
    date_format = "us"
    stopwords = []
    skip = []
    plot_type = "wordcloud"
    ngram = 1
    time_freq = "ungroup"
    max_words = 10
    numbers = True
    lower_case = True

    # Call the cappuccino function
    result = cappuccino(self.data['text'], self.data['time'], date_format, stopwords, skip, plot_type,
                        ngram, time_freq, max_words, numbers, lower_case)

    # Perform assertions based on the expected behavior
    self.assertIsNone(result)  # Assuming picture is None when using wordcloud

def test_cappuccino_line(self):
    # Provide test input
    text = "Some example text for testing."
    time = "date_column"
    date_format = "us"
    stopwords = []
    skip = []
    plot_type = "line"
    ngram = 1
    time_freq = "M"
    max_words = 10
    numbers = True
    lower_case = True

    # Call the cappuccino function
    result = cappuccino(text, time, date_format, stopwords, skip, plot_type,
                        ngram, time_freq, max_words, numbers, lower_case)


def test_cappuccino_heatmap(self):
    # Provide test input
    text = "Some example text for testing."
    time = "date_column"
    date_format = "us"
    stopwords = []
    skip = []
    plot_type = "heatmap"
    ngram = 1
    time_freq = "M"
    max_words = 10
    numbers = True
    lower_case = True

    # Call the cappuccino function
    result = cappuccino(text, time, date_format, stopwords, skip, plot_type,
                        ngram, time_freq, max_words, numbers, lower_case)



    # Perform assertions based on the expected behavior
    self.assertIsNone(result)  # Assuming picture is None when using line plot for monthly frequency

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
