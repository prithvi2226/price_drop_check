import requests
from bs4 import BeautifulSoup as Soup
import smtplib
from re import sub
from decimal import Decimal


URL = "https://www.amazon.in/ASICS-Gel-Resolution-Illusion-Shoes-7-E701Y-407/dp/B07K7RVDP5/ref=sr_1_7?crid=16NNIEBN19HX0&dchild=1&keywords=tennis+shoes+mens&qid=1589297464&refinements=p_89%3AASICS&rnid=3837712031&sprefix=tennis+shoes%2Caps%2C263&sr=8-7"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}

def check_price():
	page = requests.get(URL, headers=headers)
	soup = Soup(page.content, 'html.parser')
	

	title = soup.find(id="productTitle").get_text()
#	print(title.strip())
	
	price = soup.find(id="priceblock_ourprice").get_text()
	price1 = Decimal(sub(r'[^\d.]', '', price))
	converted_price = float(price1)
	
#	print(converted_price)

	if(converted_price < 6500):
		send_mail()

	print(title.strip())
	print(converted_price)

	if(converted_price < 6500):
		send_mail()


def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('itsmeprithvi2000@gmail.com','qdaqzfqagojlbsmj')

	subject = 'PRICE FELL DOWN MANN!!'
	body = 'CHECK YOUR AMAZON PIDDI BOI : https://www.amazon.in/ASICS-Gel-Resolution-Illusion-Shoes-7-E701Y-407/dp/B07K7RVDP5/ref=sr_1_7?crid=16NNIEBN19HX0&dchild=1&keywords=tennis+shoes+mens&qid=1589297464&refinements=p_89%3AASICS&rnid=3837712031&sprefix=tennis+shoes%2Caps%2C263&sr=8-7'

	msg = f"Subject : {subject}\n\n{body}"

	server.sendmail(
		'itsmeprithvi2000@gmail.com',
		'imprithvi2001@gmail.com',
		msg
		)
	print('HEY EMAIL HAS BEEN SENT')

	server.quit()

check_price()
