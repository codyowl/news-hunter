import urllib2
from bs4 import BeautifulSoup

while True:
	Newspaper = raw_input("""
	Which newspaper you want to read ?
	1.THE HINDU
	2.INDIAN EXPRESS
	3.DECCAN CHRONICLE
	4.THE TIMES OF INDIA
	0.Exit
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
		
		Indian_express_headlines = soup.findAll("div", {"class": "other-article"})

		Must_read = soup.findAll("div", {"class": "top-news"})

		#Technology

		Technology = soup.findAll("div", {"class": "common-structure"}, "div", {"data-vr-zone": "technology"})

		
		INDIANEXPRESS_HEADLINES_LIST = []

		MUST_READ_LIST = []

		TECHNOLOGY_LIST = []
		
		for div in Indian_express_headlines:
			content = div.find('h3').find('a').contents[0]
			INDIANEXPRESS_HEADLINES_LIST.append(content)

		for div in Must_read:
			uls = div.find('ul')
			content = [lis.get_text() for lis in uls.findAll('li')]
			for contents in content:
				MUST_READ_LIST.append(contents)

		#Technology
		for div in Technology:
			news_div = soup.findAll("div", {"class": "news"})
			for divs in news_div:
				content = divs.find('h5').find('a').contents[0]
				TECHNOLOGY_LIST.append(str(content))

		for headlines, number in enumerate(INDIANEXPRESS_HEADLINES_LIST, 1):
			print headlines, number

		#printing Must read
		print "MUST READ:"
		for headlines, number in enumerate(MUST_READ_LIST, 1):
			print headlines, number		

		print "TECHNOLOGY:"
		for headlines, number in enumerate(TECHNOLOGY_LIST, 1):
			print headlines, number

	elif Newspaper == '3':
		newspaper_url = "http://www.deccanchronicle.com/"
		soup = url_crawler(newspaper_url)

		Deccan_chronicle_headlines = soup.findAll("div", {"class" : "main-header"})

		Top_stories = soup.findAll("h3", {"class" : "stry-hd-sml-led2"})

		TOP_STORIES_LIST = []

		for div in Top_stories:
			TOP_STORIES_LIST.append(div.text)

		for headlines, number in enumerate(TOP_STORIES_LIST, 1):
			print headlines, number	   
						

	elif Newspaper == '4':
		newspaper_url = "http://timesofindia.indiatimes.com/"
		soup = url_crawler(newspaper_url)

		Top_headlines = soup.findAll("div", {"class": "widget"})


		TOP_HEADLINES_LIST = []

		
		for ultag in soup.find_all('ul', {'class': 'list9'}):
			for litag in ultag.find_all('li'):
				texts = litag.text
				TOP_HEADLINES_LIST.append(texts)

		for headlines, numbers in enumerate(TOP_HEADLINES_LIST, 1):
			print headlines, numbers				
    	
		
	else:
		break


	                       

	    
