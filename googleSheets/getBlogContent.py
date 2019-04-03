from bs4 import BeautifulSoup
import requests

page = requests.get("https://thebahblog.com")
soup = BeautifulSoup(page.content,"html.parser")

headers = soup.find(id="main").find_all("header")
blogHeaders = [
    {'title':header.find(class_='title').find('h2').get_text(),
    'desc':header.find(class_='title').find('p').get_text(),
    'pubDate': header.find(class_='meta').find('time').get_text(),
    'author': header.find(class_='meta').find('span').get_text(),
    'link':"https://thebahblog.com"+header.find(class_='title').find('h2').find('a').get('href')
    }
    for header in headers
][0:3]
