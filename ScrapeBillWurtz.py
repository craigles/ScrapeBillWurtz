import httplib2
import urllib.parse
from bs4 import BeautifulSoup
from bs4.element import SoupStrainer

http = httplib2.Http()
status, response = http.request("https://billwurtz.com/songs.html")

songLinks = BeautifulSoup(response, parse_only=SoupStrainer("a"))

for link in songLinks:
    if link.has_attr("href") and link["href"].endswith(".mp3"):
        songResponse, songData = http.request("https://billwurtz.com/" + link["href"])
        songPath = "songs/" + urllib.parse.unquote(link["href"])
        with open(songPath, 'wb') as f:
            f.write(songData)
        print("wrote: " + songPath)
