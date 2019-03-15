from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.ndtv.com/latest/').text
soup = BeautifulSoup(source, 'lxml')
article = soup.find('div', id='ins_storylist')

for news in article.find_all('li'):

	try:
		link = news.find('div', class_='new_storylising_img').a['href']
		image = news.find('div', class_='new_storylising_img').a.picture.img['src']
		headline = news.find('div', class_='nstory_header').text.strip()
		content = news.find('div', class_='nstory_intro').text

	except Exception as e:
		link = None

	if link != None:
		print("\nlink: " + link)
		print("\nimage: " + image)
		print("\nheadline: " + headline)
		print("\ncontent: " + content)
		print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
