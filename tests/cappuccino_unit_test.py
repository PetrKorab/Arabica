## Test for visualization method: cappuccino
## It relies on the n-gram frequency matrix from arabica_freq
## n-gram frequencies are visualised with Matplotlib or Plotnine


import unittest
import pandas as pd
from arabica import cappuccino

class TestCappuccinoFunction(unittest.TestCase):
    # test data
    data = pd.DataFrame({
        'text': ["You may find yourself trying to decide between comparable crystallized ginger offerings from Reeds",
                 "Reed’s has a lovely raw cane sugar flavor, and is sweeter and more mellow than The Ginger People’s."],
        'time': ["2016-08-30", "2016-08-31"]})


def test_cappuccino_wordcloud(self):
        date_format = "us"
        stopwords = ['english']
        skip = None,
        plot = "wordcloud"
        ngram = 1
        time_freq = "ungroup"
        max_words = 10
        numbers = True
        lower_case = True

        # Call the cappuccino function
        result_wordcloud = cappuccino(text=self.data['text'],
                                      time=self.data['time'],
                                      date_format = date_format, 
                                      stopwords = stopwords, 
                                      skip = skip, 
                                      plot = plot,
                                      ngram = ngram, 
                                      time_freq = time_freq, 
                                      max_words = max_words,
                                      numbers = numbers, 
                                      lower_case = lower_case)

        # Perform assertions based on the expected behavior
        self.assertIsNotNone(result_wordcloud)  # Returns a wordcloud picture, assuming picture is not None when using wordcloud
    

def test_cappuccino_line(self):
        date_format = "us"
        stopwords = ['english']
        skip = None
        plot_type = "line"
        ngram = 1
        time_freq = "M"
        max_words = 10
        numbers = True
        lower_case = True

        # Call the cappuccino function
        result_line = cappuccino(text=self.data['text'],
                                 time=self.data['time'],
                                 date_format = date_format, 
                                 stopwords = stopwords, 
                                 skip = skip, 
                                 plot = plot,
                                 ngram = ngram, 
                                 time_freq = time_freq, 
                                 max_words = max_words,
                                 numbers = numbers, 
                                 lower_case = lower_case)


        # Perform assertions based on the expected behavior
        self.assertIsNotNone(result_line)                  # Returns a line plot picture, assuming picture is not None when using line plot for monthly frequency


def test_cappuccino_heatmap(self):
        date_format = "us"
        stopwords = ['english']
        skip = None
        plot = "heatmap"
        ngram = 1
        time_freq = "M"
        max_words = 10
        numbers = True
        lower_case = True

        # Call the cappuccino function
        result_heatmap = cappuccino(text=self.data['text'],
                                    time=self.data['time'],
                                    date_format=date_format, 
                                    stopwords=stopwords, 
                                    skip=skip, 
                                    plot=plot,
                                    ngram=ngram, 
                                    time_freq=time_freq, 
                                    max_words=max_words,
                                    numbers=numbers, 
                                    lower_case=lower_case)        

        # Perform assertions based on the expected behavior
        self.assertIsNotNone(result_heatmap)  # Returns a heatmap picture, assuming picture is not None when using heatmap for monthly frequency

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
