from bs4 import BeautifulSoup as bsoup
from urllib.request import Request, urlopen

result = open("book.txt", "w")

baseLink = 'http://www.wuxiaworld.com/st-index/st-book-5-chapter-' #To change the book you're scrapping, change this line

for i in range(1, 35):
    req = Request(baseLink + str(i), headers={'User-Agent': 'Mozilla/5.0'})
    sauce = urlopen(req).read()
    soup = bsoup(sauce, 'lxml')
    for paragraph in soup.find("div", {"itemprop":"articleBody"}).find_all('p'):
        try:
            result.write(paragraph.string)
            result.write('\n')
        except:
            print ("something might not have been printed, but it's likely not important")
