#! /usr/bin/env python
# Made by: Ali Ahmer AKA King Ali
#contact: king.ali.1331@gmail.com

import urllib
from bs4 import BeautifulSoup
import urlparse
import mechanize
import time
import re

# Set the startingpoint for the spider and initialize 
# the a mechanize browser object

url = raw_input('Enter Site e.g. http://site.com : ')
br = mechanize.Browser()

# create lists for the urls in que and visited urls
urls = [url]
visited = [url]

print '[+] Please Wait, Web Crawling has been started.'

crawl_result = open('Crawl_Result.txt' , 'w+')

# Since the amount of urls in the list is dynamic
#   we just let the spider go until some last url didn't
#   have new ones on the webpage
while len(urls)>0:
    try:
        br.open(urls[0])
        urls.pop(0)
        for link in br.links():
            newurl =  urlparse.urljoin(link.base_url,link.url)
            #print newurl
            if newurl not in visited and url in newurl:
                visited.append(newurl)
                urls.append(newurl)
                if '#' in newurl:
                    m = re.search("#", newurl)
                    newurl = newurl[:m.start()]
                elif '%' in newurl:
                    m = re.search("%20", newurl)
                    newurl = newurl[:m.start()]
                print newurl
                crawl_result.write(newurl+'\r\n')
    except:
        print "(!) Error in Network Connection"
        urls.pop(0)

print '\r\n Crawler result saved in Crawl_Result.txt File.'
crawl_result.close()
print './done'
