import BeautifulSoup

import urllib2 
url = urllib2.urlopen("http://www.google.com")

content = url.read()

soup = BeautifulSoup.BeautifulSoup(content)

links = soup.findAll("a")
c=0
for i in links:
    c +=1
    print i

print c
