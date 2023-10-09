import ast
import pandas as pd
from nltk.corpus import stopwords
from nltk.util import ngrams
from string import punctuation, digits

reviews = pd.read_csv("data/hexlet_otzovik_tokens.csv")

ru_stopwords = set(stopwords.words("russian"))
rem = {"но", "не"}
ru_stopwords = ru_stopwords - rem
remove_digits = str.maketrans('', '', digits)

nostop = []
for i in range(len(reviews)):
    uni_nostop = [uni for uni in ast.literal_eval(reviews.iloc[i]["tokens_lemm"])
                  if uni not in ru_stopwords and len(uni) > 1]
    nostop.append(uni_nostop)
reviews["1-grams"] = nostop

bigrams_all = []
for i in range(len(reviews)):
    bigrams = list(ngrams(ast.literal_eval(reviews.iloc[i]["tokens_raw"]), 2))
    bigrams_all.append(bigrams)
reviews["2-grams"] = bigrams_all

trigrams_all = []
for i in range(len(reviews)):
    trigrams = list(ngrams(ast.literal_eval(reviews.iloc[i]["tokens_raw"]), 3))
    trigrams_all.append(trigrams)
reviews["3-grams"] = trigrams_all

tetragrams_all = []
for i in range(len(reviews)):
    tetragrams = list(ngrams(ast.literal_eval(reviews.iloc[i]["tokens_raw"]), 4))
    tetragrams_all.append(tetragrams)
reviews["4-grams"] = tetragrams_all

pentagrams_all = []
for i in range(len(reviews)):
    pentagrams = list(ngrams(ast.literal_eval(reviews.iloc[i]["tokens_raw"]), 5))
    pentagrams_all.append(pentagrams)
reviews["5-grams"] = pentagrams_all

print(reviews.iloc[0])

reviews.to_csv("data/hexlet_otzovik_ngrams.csv", encoding="utf-8-sig", index=False)
