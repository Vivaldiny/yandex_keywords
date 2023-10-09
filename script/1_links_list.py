import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://irecommend.ru"
REVIEWS_URL = "https://irecommend.ru/content/sait-netologiya"
r = requests.get(REVIEWS_URL)
print(r.status_code)

soup = BeautifulSoup(r.content, "html.parser")
review_list = soup.find("ul", {"class": "list-comments"})

reviews = review_list.find_all("li")

ratings_list = []
users_list = []
dates_list = []
titles_list = []
links_list = []
for i, review in enumerate(reviews):
    print(i)
    author_info = review.find("div", {"class": "authorSpace"})
    review_text = review.find("div", {"class": "reviewTextSnippet"})

    ratings_list.append(len(author_info.find("div", {"class": "starsRating"}).find_all("div", {"class": "on"})))
    users_list.append(author_info.find("div", {"class": "authorName"}).find("a")["href"])
    dates_list.append(author_info.find("div", {"class": "created"}).text)
    titles_list.append(review_text.find("div", {"class": "reviewTitle"}).a.text)

    review_link = review_text.find("div", {"class": "reviewTitle"}).a["href"]
    links_list.append(review_link)


reviews_df = pd.DataFrame({"user": users_list,
                           "creation_date": dates_list,
                           "rating": ratings_list,
                           "link": links_list,
                           "title": titles_list})
print(reviews_df)

FILE_NAME = "irecom_netologiya.csv"
# reviews_df.to_csv(FILE_NAME)
