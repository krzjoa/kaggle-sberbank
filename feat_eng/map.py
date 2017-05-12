
#https://geocode-maps.yandex.ru/1.x/?geocode=Moscow+Lva+Tolstogo+Street+16&lang=en_US

YANDEX_URL = "https://geocode-maps.yandex.ru/1.x"
STATIC = "/?format=json&lang=en_US&geocode="

import requests
import json

# response = requests.get("https://geocode-maps.yandex.ru/1.x/?format=json&geocode=Moscow+Lva+Tolstogo+Street+16&lang=en_US")
#
# print json.loads(response.content)


def geocode(name):
    response = requests.get(YANDEX_URL + STATIC + name)
    parsed_dict = json.loads(response.content)
    print parsed_dict['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']

geocode("Moscow+Lva+Tolstogo+Street+16")