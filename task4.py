import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

pop_url = "https://imdb-api.com/en/API/MostPopularMovies/k_pwnfqnbq"
review_url = "https://imdb-api.com/en/API/Reviews/k_pwnfqnbq/{id}"
films = requests.get(pop_url).json().get("items")[:5]

API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"



def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))


for film in films:
    true_count = 0
    neg_count = 0
    pos_count = 0
    neutral_count = 0
    print(f'{film.get("title")}')
    print(f'Оценка фильма - {film.get("imDbRating")}')
    reviews = requests.get(review_url.format(id=film.get("id"))).json().get("items")
    for review in reviews:
        content = review.get("content")[:512]
        rate_str = review.get("rate")
        if rate_str == '':
            continue
        else:
            rate = int(review.get("rate"))
        data = query({"inputs": f"{content}"})[0]
        if data[0]['score'] > 0.6:
            neg_count += 1
            if rate < 5:
                true_count += 1
        elif data[1]['score'] > 0.6:
            pos_count += 1
            if rate > 6:
                true_count += 1
        else:
            if rate == 5 or rate == 6:
                true_count += 1
            neutral_count += 1
    print(f"Точность оценки - {true_count / 25}")
    print(f"Процент положительных - {pos_count / 25}")
    print(f"Процент отрицательных - {neg_count / 25}")
    keks = 5
