import pandas as pd
from nltk.corpus import stopwords
from pymystem3 import Mystem
from tqdm import tqdm

reviews = pd.read_csv("data/hexlet_otzovik.csv")

mystem = Mystem()

reviews["lower"] = reviews["Текст"].str.lower()
reviews_lemm = []
for i in tqdm(range(len(reviews))):
    lemmas = mystem.lemmatize(reviews.iloc[i]["lower"])
    print("".join(lemmas))
    reviews_lemm.append("".join(lemmas))
reviews["lemm"] = reviews_lemm

reviews.to_csv("data/hexlet_otzovik_lemm.csv", encoding="utf-8-sig", index=False)
