import requests as req
from bs4 import BeautifulSoup as bs

def curl():
	return req.get('https://www.liputan6.com/indonesia-baru/feed/rss')

def get(link):
	return req.get(link)

gets = curl()
sop = bs(gets.text, 'xml')
items = sop.find_all('item')

for item in items:
	links = item.find_all('link')
	for link in links:
		p = get(link.text)
		sop = bs(p.text, 'html.parser') 
		print(' Link :',link.text,"\n")
		title = sop.find('h1',attrs={'class':'read-page--header--title entry-title'})
		print(' Title :',title.text,"\n")
		date = sop.find('time', attrs={'class':'read-page--header--author__datetime updated'})
		print(' Date :',date.text,"\n")
		ar = sop.find('div',attrs={'class':'article-content-body__item-content'})
		print(' Article :',ar.text,"\n")
