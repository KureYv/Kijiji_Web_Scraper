from bs4 import BeautifulSoup
import requests
import re
import csv


csv_file = open('shoes.csv','w')
csv_writer = csv.writer(csv_file)

def kijiji(keyss):
    source = requests.get('https://www.kijiji.ca/b-mens-shoes/markham-york-region/page-'+keyss+'/c15117001l1700274').text
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

for i in range (1,10):
    counter = i
    counter = str(counter)
    kijiji(counter)


csv_file.close()
