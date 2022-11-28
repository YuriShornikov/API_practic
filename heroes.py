import requests

from pprint import pprint

url_base = 'https://akabab.github.io/superhero-api/api/'
url_all = 'all.json'
url = url_base + url_all
res = requests.get(url).json()

hero_list = ['Thanos', 'Hulk', 'Captain America']
dict_main_hero = {}
for hero in res:
    for main_hero in hero_list:
        if main_hero == hero['name']:
            dict_main_hero.update({hero['name']: hero['powerstats']['intelligence']})
            # print(hero['name'])
            # print(hero['powerstats']['intelligence'])

print(max(dict_main_hero, key=dict_main_hero.get))
            # for keys, values in dict_main_hero:
            #     keys = hero['name']
            #     values = hero['powerstats']['intelligence']
                # dict_main_hero.update(hero)
                # pprint(dict_main_hero)

            # dict_main_hero.update(hero)
            # print(dict_main_hero)


# heroes = list(filter(lambda hero: hero['name'] in ['Hulk', 'Captain America', 'Thanos'], res))
# pprint(heroes)

