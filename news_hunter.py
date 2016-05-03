import urllib2
from bs4 import BeautifulSoup

Newspaper = raw_input("""
Which one you want to read ?
1.THE HINDU
2.INDIAN EXPRESS
3.DECCAN CHRONICLE
4.THE TIMES OF INDIA
5.HINDUSTANTIMES
""")

if Newspaper == '1':
	newspaper_url = "http://www.thehindu.com/"
	requester = urllib2.Request(newspaper_url, headers={'User-Agent': "Magic Browser"})
	connector = urllib2.urlopen(requester)
	connector_reader = connector.read()
	soup = BeautifulSoup(connector_reader, "lxml")

	Headlines_div = soup.findAll("div", {"class" : "h-main-lead posRel"})
	
	PICKUP_HEADLINES = soup.findAll("div", {"class" : "mr15 onecolumn-car"})

	PICKUP_HEADLINES_LIST = []

	for div in PICKUP_HEADLINES:
		content = div.find('h3').find('a').contents[0]
		PICKUP_HEADLINES_LIST.append(content)

	print PICKUP_HEADLINES_LIST	

	HEADLINES_LIST = []

	for div in Headlines_div:
		content = div.find('h1').find('a').contents[0]
		HEADLINES_LIST.append(str(content))
		
	
elif Newspaper == '2':
	newspaper_url = "http://indianexpress.com/"
	
elif Newspaper == '3':
	newspaper_url = "http://www.deccanchronicle.com/"

elif Newspaper == '4':
	newspaper_url = "http://timesofindia.indiatimes.com/"

elif Newspaper == '5':
	newspaper_url = "http://http://www.hindustantimes.com/homepage/"

else:
	print "Make suer you've entered the right number"


# def url_opener(url):
# 	requester = urllib2.Request(url, headers={'User-Agent': "Magic Browser"}
# 	connector = urllib2.urlopen(requester)
# 	connector_reader = connector.read()
# 	return connector_reader

                       
