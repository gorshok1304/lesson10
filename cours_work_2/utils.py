import requests
import json
import random
from basic_word import BasicWord


def load_random_word():
    list_word = requests.get("https://jsonkeeper.com/b/M6Y4")
    list_word_json = list_word.json()
    random_word = random.choice(list_word_json)

    basicword = BasicWord(random_word["word"], random_word["subwords"])
    return basicword
