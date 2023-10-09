import csv
from rake_nltk import Rake
import nltk
import re
from pymystem3 import Mystem
import pandas as pd
from string import digits, punctuation
import ast

reviews = pd.read_csv("data/hexlet_otzovik_ngrams.csv")
reviews_pos = reviews[reviews["Рекомендую друзьям"] == "ДА"].reset_index()
reviews_neg = reviews[reviews["Рекомендую друзьям"] == "НЕТ"].reset_index()

reviews_full = [" ".join(ast.literal_eval(reviews.iloc[i]["1-grams"])) for i in range(len(reviews))]
pos = [" ".join(ast.literal_eval(reviews_pos.iloc[i]["1-grams"])) for i in range(len(reviews_pos))]
neg = [" ".join(ast.literal_eval(reviews_neg.iloc[i]["1-grams"])) for i in range(len(reviews_neg))]

pos = " ".join(pos)
neg = " ".join(neg)
key_3grams_rake = []
all_reviews = ' '.join(reviews_full)

r = Rake(language='russian', max_length=1)
r.extract_keywords_from_text(pos)
key_words = r.get_ranked_phrases()
key_3grams_rake.append(key_words[:15])
r.extract_keywords_from_text(neg)
key_words = r.get_ranked_phrases()
key_3grams_rake.append(key_words[:15])

r = Rake(language='russian', max_length=5)
key_ngrams = []
remove_punct = str.maketrans('', '', digits + punctuation + '«»»»)(—…')
reviews_all = [reviews.iloc[i]["lower"].replace('\n', ' ') for i in range(len(reviews))]
a = " ".join(reviews_all)
a = a.translate(remove_punct)
r.extract_keywords_from_text(a)
key_words = r.get_ranked_phrases_with_scores()
print(key_words)
df_keys = pd.DataFrame(key_words, columns=["score", "keyphrase"])
df_keys.to_csv("keywords/keywords_full.csv", encoding="utf-8-sig")

pos = [reviews_pos.iloc[i]["lower"].replace('\n', ' ') for i in range(len(reviews_pos))]
a = " ".join(pos)
a = a.translate(remove_punct)
r.extract_keywords_from_text(a)
key_words = r.get_ranked_phrases_with_scores()
print(key_words)
df_keys = pd.DataFrame(key_words, columns=["score", "keyphrase"])
df_keys.to_csv("keywords/keywords_pos.csv", encoding="utf-8-sig")

neg = [reviews_neg.iloc[i]["lower"].replace('\n', ' ') for i in range(len(reviews_neg))]
a = " ".join(neg)
a = a.translate(remove_punct)
r.extract_keywords_from_text(a)
key_words = r.get_ranked_phrases_with_scores()
print(key_words)
df_keys = pd.DataFrame(key_words, columns=["score", "keyphrase"])
df_keys.to_csv("keywords/keywords_neg.csv", encoding="utf-8-sig")

# print(key_3grams_rake)
#
# all_key_words = r.get_ranked_phrases()
# print(all_key_words[:30])

# text_list = []
# pros_list = []
# cons_list = []
#
# with open("data/hexlet_otzovik_ngrams.csv", encoding="utf-8-sig") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         text_list.append(row['lemm'].replace('\n', ' '))
#
# print(text_list)


# # извлекаем ключевые триграммы методом Rake
# key_3grams_rake = []
# for t in text_list:
#     text = t
#
#     # Предобработка текста
#     text = text.lower()  # переводим в lowercase
#     text = re.sub('\d', '', text)  # убираем все цифры
#     extra_punctuation = ['«', '»', '».', '»,', ')', '(', '—']
#     for mark in extra_punctuation:
#         text = text.replace(mark, '')
#     # m = Mystem()
#     # text = m.lemmatize(text)
#     # text = [w for w in text if w != ' ']
#     # text = ' '.join(text)
#
#     # Извлечение ключевых слов
#     r = Rake(language='russian', max_length=3)
#     r.extract_keywords_from_text(text)
#     key_words = r.get_ranked_phrases()
#     key_3grams_rake.append(key_words[:5])
#
# print(key_3grams_rake)
#
# # делаем того же самое для всех отзывов, собранных в один текст
# all_reviews = ' '.join(text_list)
#
# all_text = all_reviews
#
# # Предобработка текста
# all_text = all_text.lower()  # переводим в lowercase
# all_text = re.sub('\d', '', all_text)  # убираем все цифры
# extra_punctuation = ['«', '»', '».', '»,', ')', '(', '—']
# for mark in extra_punctuation:
#     all_text = all_text.replace(mark, '')
#
#
# # Извлечение ключевых слов
# r = Rake(language='russian', max_length=5)
# r.extract_keywords_from_text(all_text)
# all_key_words = r.get_ranked_phrases()
# print(all_key_words[:30])
