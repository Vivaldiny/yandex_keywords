import pandas as pd
import ast


def get_key_freq(df, keywords: str, n_gram: int):
    keywords_count = {}
    for i in range(len(df)):
        grams = ast.literal_eval(df.iloc[i][keywords])
        for gram in grams:
            if len(gram.split(" ")) == n_gram:
                if gram in keywords_count.keys():
                    keywords_count[gram] += 1
                else:
                    keywords_count[gram] = 1
            # else:
            #     continue
    key_df = pd.DataFrame.from_dict(keywords_count, orient="index", columns=["n"]).sort_values(by="n", ascending=False)
    return key_df


pos = pd.read_csv("keywords/pos.csv", encoding="utf-8-sig",
                  index_col=0)
neg = pd.read_csv("keywords/neg.csv", encoding="utf-8-sig",
                  index_col=0)

keygrams = get_key_freq(neg, "key5gram", 5)
# keygrams.to_csv("keywords/neg_5gram.csv", encoding="utf-8-sig")
