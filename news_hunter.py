import urllib2
from bs4 import BeautifulSoup

Newspaper = raw_input("""
Which one you want to read ?
1.THE HINDU
2.INDIAN EXPRESS
3.DECCAN CHRONICLE
4.THE TIMES OF INDIA
"""

if Newspaper == '1':
	newspaper_url = "http://www.thehindu.com/"

elif Newspaper == '2':
	newspaper_url = "http://indianexpress.com/"

elif Newspaper == '3':
	newspaper_url = "http://www.deccanchronicle.com/"

elif Newspaper == '4':
	newspaper_url = "http://timesofindia.indiatimes.com/"

else:
	print "Make suer you've entered the right number"

                       
