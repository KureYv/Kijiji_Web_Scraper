from bs4 import BeautifulSoup
import requests
import re
import csv

link = "Your link here"
csv_file = open('output.csv','w')
csv_writer = csv.writer(csv_file)
pagestart = "Page range start here"
pageend = "Page range end here"
param = "Input what you see at the ending part of the link, for example like this c37l1700273a29276001?ad=offering&unit-type=house"

def kijiji(keyss):
    source = requests.get(link +keyss+ param).text
    soup = BeautifulSoup(source,'lxml')
    b = soup.find('div', class_='price')
    for link in soup.find_all('a',class_ = 'title'):
        a = link.get('href')
        fulllink = a
        fulllink = a.split('/')[3]
        print(fulllink)
        c=b.prettify()
        c = c.replace('<div class="price">', "")
        c = c.replace('</div>', "")
        c = c.strip()
        csv_writer.writerow([fulllink,c])

for i in range (pagestart,pageend):
    counter = i
    counter = str(counter)
    kijiji(counter)


csv_file.close()
