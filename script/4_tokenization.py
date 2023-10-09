import string
import pandas as pd

reviews = pd.read_csv("data/hexlet_otzovik_lemm.csv")

reviews["tokens_raw"] = reviews["lower"].str.split()
unis = []
for i in range(len(reviews)):
    unis_clean = []
    for uni in reviews.iloc[i]["tokens_raw"]:
        uni = uni.strip(string.punctuation + '«»»»)(—…')
        if uni != '':
            unis_clean.append(uni)
    unis.append(unis_clean)
reviews["tokens_raw"] = unis

reviews["tokens_lemm"] = reviews["lemm"].str.split()
unis = []
for i in range(len(reviews)):
    unis_clean = []
    for uni in reviews.iloc[i]["tokens_lemm"]:
        uni = uni.strip(string.punctuation + '«»»»)(—…')
        if uni != '':
            unis_clean.append(uni)
    unis.append(unis_clean)
reviews["tokens_lemm"] = unis

reviews.to_csv("data/hexlet_otzovik_tokens.csv", encoding="utf-8-sig", index=False)
