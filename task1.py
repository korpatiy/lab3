from collections import Counter

import requests
import os
from bs4 import BeautifulSoup

wiki_url = 'https://ru.wikipedia.org/w/index.php?title=JSON&action=history'
ipstack_url = 'http://api.ipstack.com/{ip}?access_key={key}'

r = requests.get(wiki_url)
soup = BeautifulSoup(r.text, "lxml")
history_list = soup.find('section', {'id': 'pagehistory'}).find_all('ul')

ip_list = []

for item in history_list:
    actions = item.find_all('li', {'class': ['mw-tag-wikieditor', 'mw-tag-mobile_edit', 'mw-tag-mw-rollback']})
    for action in actions:
        user = action.find('span', {'class': 'history-user'}).find('a', {'class': 'mw-anonuserlink'})
        if user is not None:
            ip_list.append(user.find('bdi').text)

distinct_ip = list(set(ip_list))
print(distinct_ip)

country_list = []
for ip in distinct_ip:
    response = requests.get(ipstack_url.format(ip=ip, key=os.environ['API_KEY'])).json()
    country = response.get('country_name')
    country_list.append(country)
    print(ip + "-" + country)

print(Counter(country_list))
