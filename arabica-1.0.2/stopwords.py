
"""
Removes stopwords with nltk.
List of provided languages:
from nltk.corpus import stopwords
print(stopwords.fileids())
"""

from nltk.corpus import stopwords as st

def remove_stopwords(text: str,
                     stopwords = []):

    for language in stopwords:
        stops= set(st.words(language))
        filtered_words = [word for word in text.split() if word.lower() not in stops]

    return " ".join(filtered_words)