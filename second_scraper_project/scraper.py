# import pprint
import requests
from inflection import titleize
from bs4 import BeautifulSoup

# def titles_generator(links):
#     titles = []

#     def post_formatter(url):
#         if 'posts' in url:
#             url = url.split('/')[-1]
#             url = url.replace('-', ' ')
#             url = titleize(url)
#             titles.append(url)
def title_generator(links):
    titles = []

    def post_formatter(url):
        if 'https' in url:
            # url = url.split('/')[-1]
            titles.append(url)


    for link in links:
        post_formatter(link['href'])

    return titles


r = requests.get('https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48')
soup = BeautifulSoup(r.text, 'html.parser')
# links = soup.find('div', attrs={'class': 'item-info'})
links = soup.findAll('a', attrs={'class': 'item-title'})

# titles = []
titles = title_generator(links)
# links = []
for title in titles:
    print(title)