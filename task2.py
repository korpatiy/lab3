import statistics

import requests


def getPage(page=0, area=1, currency='RUR'):
    params = {
        'text': 'kotlin',
        'area': area,
        'page': page,
        'per_page': 50
    }

    req = requests.get('https://api.hh.ru/vacancies', params).json()

    average_salary_list = []
    for item in req.get('items'):
        salary = item.get('salary')
        if salary is not None:
            if salary['currency'] == currency:
                s_from = salary['from']
                s_to = salary['to']
                if s_to and s_from is not None:
                    average_salary = (s_from + s_to) / 2
                elif s_from is not None:
                    average_salary = s_from
                elif s_to is not None:
                    average_salary = s_to
                average_salary_list.append(average_salary)
    return average_salary_list


cities = {'moscow': 1, "spb": 2, 'ekb': 3, 'perm': 72}
currency = 'RUR'
for city in cities:
    average_salary_city = []
    for page in range(0, 10):
        average_salary_city.extend(getPage(page=page, area=cities[city], currency=currency))
    print(city + " - " + str(round(statistics.mean(average_salary_city), 2)) + " " + currency)
