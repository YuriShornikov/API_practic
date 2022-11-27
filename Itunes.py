import requests
import pandas as pd
#pip install pandas

from pprint import pprint
#pip install pprint

# url = 'https://itunes.apple.com/search?term=jack+johnson'
#
# params = {
#     'term': 'Сергей Шнуров',
#     'limit': 200,
#     'country': 'ru',
#     'attribute': 'allArtistTerm'
# }
# response = requests.get(url, params)
# test = pd.DataFrame(response.json()['results'])
# print(test)
# pprint(response.json())
from bs4 import BeautifulSoup
#pip install bs4

res = requests.get('https://netology.ru/blog/')

soup = BeautifulSoup(res.text, features="html.parser")
news = soup.find_all('div', class_='posts__item')
# print(news)
# print(len(news))
for i in news:
    title = i.find('a', 'posts__link').text
    link = i.find('a', 'posts__link').get('href')
    date = i.find('div', 'posts__date').text
    category = i.find('a', 'tags__item').text
    # title = i.find('a', 'posts__link').parent
    print(title)
    print(link)
    print(date)
    print(category)
# print(soup)
# print(res.text)
#https://colab.research.google.com/drive/1iduDcq6CMWn8UkPLvVSJoAxEZ7X28QBo#scrollTo=O1HP4mc1P-JR&uniqifier=1