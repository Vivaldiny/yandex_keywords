import requests
import pandas as pd
from os.path import exists

LINKS_FILE = "irecom_hexlet.csv"
links_df = pd.read_csv(LINKS_FILE, index_col=0)

URL = "https://irecommend.ru"
PATH = "html/hexlet"

for i, link in enumerate(list(links_df["link"])):
    if not exists(f"{PATH}/{i}.txt"):
        print(URL + link)
        r = requests.get(URL + link)
        print(r.status_code)
        if r.status_code == 200:
            with open(f"{PATH}/{i}.txt", "w", encoding="utf-8") as file:
                file.write(r.text)