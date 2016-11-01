from bs4 import BeautifulSoup as bsoup
from urllib.request import Request, urlopen

baseLink = 'http://www.wuxiaworld.com/st-index/st-book-3-chapter-'
chapter = 1

req = Request(baseLink, headers={'User-Agent': 'Mozilla/5.0'})
sauce = urlopen(req).read()

soup = bsoup(sauce, 'lxml')

for i in range(1, 25):
    req = Request(baseLink + str(i), headers={'User-Agent': 'Mozilla/5.0'})
    sauce = urlopen(req).read()
    soup = bsoup(sauce, 'lxml')
    for paragraph in soup.find("div", {"itemprop":"articleBody"}).find_all('p'):
        print(paragraph.string)
