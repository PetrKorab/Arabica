## Test for descriptive n-gram method: arabica_freq
## N-gram frequency matrix from arabica_freq is also used in the visualization method - cappuccino; its functionality is therefore essential


import unittest
import pandas as pd
from arabica import arabica_freq
from collections import Counter

class TestArabicaFreq(unittest.TestCase):
    # test data
    data = pd.DataFrame({
        'text': ["You may find yourself trying to decide between comparable crystallized ginger offerings from Reeds",
                 "Reed’s has a lovely raw cane sugar flavor, and is sweeter and more mellow than The Ginger People’s."],
        'time': ["2016-08-30", "2016-08-31"]})

    def calculate_ngram_frequencies(self, text_column):
        # Tokenize the text into words
        tokens = text_column.str.lower().str.split()

        # Calculate unigram, bigram, and trigram frequencies
        unigrams = Counter(token for sentence_tokens in tokens for token in sentence_tokens)
        bigrams = Counter(tuple(tokens[i:i+2]) for tokens in tokens for i in range(len(tokens)-1))
        trigrams = Counter(tuple(tokens[i:i+3]) for tokens in tokens for i in range(len(tokens)-2))

        # Create DataFrames from the Counter objects, showing only the first three n-grams
        unigrams_df = pd.DataFrame(list(unigrams.items())[:3], columns=['unigram', 'unigram_freq'])
        bigrams_df = pd.DataFrame(list(bigrams.items())[:3], columns=['bigram', 'bigram_freq'])
        trigrams_df = pd.DataFrame(list(trigrams.items())[:3], columns=['trigram', 'trigram_freq'])

        return unigrams_df, bigrams_df, trigrams_df


    def test_arabica_freq(self):
        date_format = "eur"
        stopwords = None
        skip = ["skip", "these"]
        time_freq = "ungroup"
        max_words = 3
        numbers = True
        lower_case = True

        # Call the function
        result = arabica_freq(text=self.data['text'],
                              time=self.data['time'],
                              date_format=date_format,
                              stopwords=None,
                              skip=skip,
                              time_freq=time_freq,
                              max_words=max_words,
                              numbers=numbers,
                              lower_case=lower_case)

        # Assert the result has the expected structure
        self.assertIsInstance(result, pd.DataFrame)
        # Calculate expected n-gram frequencies using the provided function
        unigrams_df, bigrams_df, trigrams_df = self.calculate_ngram_frequencies(self.data['text'])

        # Assert the DataFrames are equal
        pd.testing.assert_frame_equal(result['unigram_freq'].to_frame().reset_index(drop=True), result['unigram_freq'].to_frame().reset_index(drop=True))
        pd.testing.assert_frame_equal(result['bigram_freq'].to_frame().reset_index(drop=True), result['bigram_freq'].to_frame().reset_index(drop=True))
        pd.testing.assert_frame_equal(result['trigram_freq'].to_frame().reset_index(drop=True), result['trigram_freq'].to_frame().reset_index(drop=True))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
