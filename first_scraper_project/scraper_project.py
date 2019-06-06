# Libraries:

# -requests
# -inflection
# -beautifulsoup

# pip install requests
# pip install inflection
# pip install beautifulsoup4

# www.dailysmarty.com/topics/python
# scrape the post links and convert them into "Nice looking strings"
# https://bottega.devcamp.com/12/guide/1512
import pprint
import requests
from inflection import titleize
from bs4 import BeautifulSoup


def titles_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)



    for link in links:
        post_formatter(link['href'])

    return titles


r = requests.get('https://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.findAll("a")

titles = titles_generator(links)

for title in titles:
    print(title)