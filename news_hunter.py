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

def url_crawler(url):
	requester = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
	connector = urllib2.urlopen(requester)
	connector_reader = connector.read()
	soup = BeautifulSoup(connector_reader, "lxml")
	return soup	

if Newspaper == '1':
	newspaper_url = "http://www.thehindu.com/"
	soup = url_crawler(newspaper_url)
	
	Headlines_div = soup.findAll("div", {"class" : "h-main-lead posRel"})
	
	PICKUP_HEADLINES = soup.findAll("div", {"class" : "mr15 onecolumn-car"})

	PICKUP_HEADLINES_LIST = []

	for div in PICKUP_HEADLINES:
                content = div.find('h3').find('a').contents[0]
		PICKUP_HEADLINES_LIST.append(content)
	
	for headlines, number in enumerate(PICKUP_HEADLINES_LIST, 1):
		print headlines, number

	HEADLINES_LIST = []

	for div in Headlines_div:
		content = div.find('h1').find('a').contents[0]
		HEADLINES_LIST.append(str(content))

	print "MAIN HEADING :"
	for headlines in HEADLINES_LIST:
		print headlines
		
elif Newspaper == '2':
	newspaper_url = "http://indianexpress.com/"
	soup = url_crawler(newspaper_url)
	
	Indian_express_headlines = ("div", {"class": "left-part"})

	INDIANEXPRESS_HEADLINES_LIST = []
	
	for div in Indian_express_headlines:
		content = div.find('h3').find('a').contents[0]
		INDIANEXPRESS_HEADLINES_LIST.append(str(content))

	print INDIANEXPRESS_HEADLINES_LIST
		

elif Newspaper == '3':
	newspaper_url = "http://www.deccanchronicle.com/"
	soup = url_crawler(newspaper_url)

	Deccan_chronicle_headlines = ("div", {"class" : "main-header"})

	DECCAN_CHRONICLE_HEADLINES_LIST = []

	for div in Deccan_chronicle_headlines:
		content = div.find('h2').find('a').contents[0]
		DECCAN_CHRONICLE_HEADLINES_LIST.append(str(content))

	print DECCAN_CHRONICLE_HEADLINES_LIST

elif Newspaper == '4':
	newspaper_url = "http://timesofindia.indiatimes.com/"
	soup = url_crawler(newspaper_url)

elif Newspaper == '5':
	newspaper_url = "http://http://www.hindustantimes.com/homepage/"
	soup = url_crawler(newspaper_url)

else:
	print "Make suer you've entered the right number"


                       

    
