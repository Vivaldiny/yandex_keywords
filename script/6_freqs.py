import ast
import pandas as pd


reviews = pd.read_csv("data/hexlet_otzovik_ngrams.csv")
reviews_pos = reviews[reviews["Рекомендую друзьям"] == "ДА"].reset_index()
reviews_neg = reviews[reviews["Рекомендую друзьям"] == "НЕТ"].reset_index()

# print(reviews.columns)

freqs = {}
for i in range(len(reviews)):
    grams = reviews.iloc[i]["5-grams"]
    for gram in ast.literal_eval(grams):
        gram = " ".join(gram)
        if gram in freqs.keys():
            freqs[gram] += 1
        else:
            freqs[gram] = 1

uni_freq = pd.DataFrame.from_dict(freqs, orient="index", columns=["n"]).sort_values(by="n", ascending=False)
uni_freq.to_csv("freqs/penta_full.csv", encoding="utf-8-sig")

freqs = {}
for i in range(len(reviews_pos)):
    grams = reviews_pos.iloc[i]["5-grams"]
    for gram in ast.literal_eval(grams):
        gram = " ".join(gram)
        if gram in freqs.keys():
            freqs[gram] += 1
        else:
            freqs[gram] = 1

uni_freq = pd.DataFrame.from_dict(freqs, orient="index", columns=["n"]).sort_values(by="n", ascending=False)
uni_freq.to_csv("freqs/penta_pos.csv", encoding="utf-8-sig")

freqs = {}
for i in range(len(reviews_neg)):
    grams = reviews_neg.iloc[i]["5-grams"]
    for gram in ast.literal_eval(grams):
        gram = " ".join(gram)
        if gram in freqs.keys():
            freqs[gram] += 1
        else:
            freqs[gram] = 1

uni_freq = pd.DataFrame.from_dict(freqs, orient="index", columns=["n"]).sort_values(by="n", ascending=False)
uni_freq.to_csv("freqs/penta_neg.csv", encoding="utf-8-sig")
