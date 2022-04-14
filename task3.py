import requests

url = "https://rusvectores.org/{model}/{word}/api/{format}/"

MODEL = 'ruscorpora_upos_cbow_300_20_2019'
FORMAT = 'json'
WORD = 'Дом'

response = requests.get(url.format(model=MODEL, word=WORD, format=FORMAT)).json()

kek = 5

word_list = ['молоко', 'президент', 'учить', 'хороший']
