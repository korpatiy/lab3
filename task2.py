import requests

params = {
    'text': 'python',
    'area': 72,
    'page': 0,
    'per_page': 50
}

req = requests.get('https://api.hh.ru/vacancies', params).json()
for item in req.get('items'):
    a = item
    kek = 4
req.close()
