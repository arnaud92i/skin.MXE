#!/usr/bin/env python
from mechanize import Browser
from BeautifulSoup import BeautifulSoup
import urllib, os

def extract(soup, year):
    table = soup.find("table", border=1)
    for row in table.findAll('tr')[1:]:
        col = row.findAll('td')
        rank = col[0].string
        artist = col[1].string
        album = col[2].string
        cover_link = col[3].img['src']
        record = (str(year), rank, artist, album, cover_link)
        print >> outfile, "|".join(record)
        save_as = os.path.join("C:\Music./", album + ".jpg")
        urllib.urlretrieve("http://www.palewire.com" + cover_link, save_as)
        print "Downloaded %s album cover" % album

outfile = open("albums.txt", "w")
mech = Browser()
url = "http://www.palewire.com/scrape/albums/2007.html"
page1 = mech.open(url)
html1 = page1.read()
soup1 = BeautifulSoup(html1)
extract(soup1, 2007)
page2 = mech.follow_link(text_regex="Next")
html2 = page2.read()
soup2 = BeautifulSoup(html2)
extract(soup2, 2006)
outfile.close()

