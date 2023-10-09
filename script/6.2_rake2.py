import csv
from rake_nltk import Rake
import nltk
import re
from pymystem3 import Mystem
import pandas as pd
from string import digits, punctuation
import ast
from nltk.corpus import stopwords

reviews = pd.read_csv("data/hexlet_otzovik_ngrams.csv").loc[:, ["Автор", "Текст", "Рекомендую друзьям", "lower", "lemm"]]
# reviews_pos = reviews[reviews["Рекомендую друзьям"] == "ДА"].reset_index()
# reviews_neg = reviews[reviews["Рекомендую друзьям"] == "НЕТ"].reset_index()

ru_stopwords = list(stopwords.words("russian"))
add_stopwords = ["это", "хекслет", "хекслете", "т", "также", "школа"]

key1grams = []
r = Rake(language='russian', max_length=1, include_repeated_phrases=False,
         stopwords=ru_stopwords+add_stopwords)
for i in range(len(reviews)):
    review = reviews.iloc[i]["lemm"]
    r.extract_keywords_from_text(review)
    key_words = r.get_ranked_phrases()[:10]
    key1grams.append(key_words)

reviews["key1gram"] = key1grams

key2grams = []
r = Rake(language='russian', max_length=2, include_repeated_phrases=False,
         stopwords=ru_stopwords+add_stopwords)
for i in range(len(reviews)):
    review = reviews.iloc[i]["lower"]
    r.extract_keywords_from_text(review)
    key_words = r.get_ranked_phrases()[:10]
    key2grams.append(key_words)
reviews["key2gram"] = key2grams

key3grams = []
r = Rake(language='russian', max_length=3, include_repeated_phrases=False,
         stopwords=ru_stopwords+add_stopwords, punctuations=digits + punctuation + '«»»»)(—…–».')
for i in range(len(reviews)):
    review = reviews.iloc[i]["lower"]
    r.extract_keywords_from_text(review)
    key_words = r.get_ranked_phrases()[:10]
    key3grams.append(key_words)
reviews["key3gram"] = key3grams

key4grams = []
r = Rake(language='russian', max_length=4, include_repeated_phrases=False,
         stopwords=ru_stopwords+add_stopwords, punctuations=digits + punctuation + '«»»»)(—…–».')
for i in range(len(reviews)):
    review = reviews.iloc[i]["lower"]
    r.extract_keywords_from_text(review)
    key_words = r.get_ranked_phrases()[:10]
    key4grams.append(key_words)
reviews["key4gram"] = key4grams

key5grams = []
r = Rake(language='russian', max_length=5, include_repeated_phrases=False,
         stopwords=ru_stopwords+add_stopwords, punctuations=digits + punctuation + '«»»»)(—…–».')
for i in range(len(reviews)):
    review = reviews.iloc[i]["lower"]
    r.extract_keywords_from_text(review)
    key_words = r.get_ranked_phrases()[:10]
    key5grams.append(key_words)
reviews["key5gram"] = key5grams

reviews.to_csv("keywords/keywords.csv", encoding="utf-8-sig")

# freq_keys = {}
# for i in range(len(reviews)):
#     unigrams = reviews.iloc[i]["key1gram"]
#     for unigram in unigrams:
#         if unigram in freq_keys.keys():
#             freq_keys[unigram] += 1
#         else:
#             freq_keys[unigram] = 1
#
# counts = pd.DataFrame.from_dict(freq_keys, orient="index")
# counts.to_csv("keywords/freq.csv", encoding="utf-8-sig")

reviews_pos = reviews[reviews["Рекомендую друзьям"] == "ДА"].reset_index()
reviews_neg = reviews[reviews["Рекомендую друзьям"] == "НЕТ"].reset_index()

# reviews_pos.to_csv("keywords/pos.csv", encoding="utf-8-sig")
# reviews_neg.to_csv("keywords/neg.csv", encoding="utf-8-sig")
