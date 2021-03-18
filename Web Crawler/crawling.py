import requests
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('crawling.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS Crawl''')
c.execute('''CREATE TABLE Crawl(name TEXT, links TEXT)''')

import csv
# f = csv.writer(open('coursesdetail.csv','w'))
# f.writerow(['CourseName','Link'])

# url = 'https://www.learningcrux.com/programming/course/1'
def Crawl(url):
    for i in range(1,5):
        url = 'https://www.learningcrux.com/programming/course/'+str(i)
        r = requests.get(url)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent,'html.parser')
        for link in soup.find_all('a'):
                if link.get('name'):
                    links = "https://www.learningcrux.com"+link.get('href')
                    name = link.get('name')
                    c.execute('''INSERT INTO Crawl VALUES(?,?)''', (name,links))
    return

Crawl('https://www.learningcrux.com/programming/course/1')
conn.commit()
print('Complete')
