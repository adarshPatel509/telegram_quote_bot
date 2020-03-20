import re
import urllib
from bs4 import BeautifulSoup

def get_song_url(song_title):
    song_title = song_title.strip()
    song_title = song_title.replace(" ", "+")
    query_url = "https://search.azlyrics.com/search.php?q={}".format(song_title)

    try:
        #fetch song url from song_title
        content = urllib.request.urlopen(query_url).read()
        soup = BeautifulSoup(content, "html.parser")
        result = soup.select('div[class="panel"]')
        result = result[len(result) -1]
        
        soap = BeautifulSoup(str(result), "html.parser")
        lyrics_url = soap.select('table > tr > td > a[target="_blank"]')[0]["href"]
        
        return lyrics_url   
    except Exception as _:
        return "Error Occurred!"


def get_lyrics(song_title):
    lyrics_url = get_song_url(song_title)
    if lyrics_url == "Error Occurred!":
        return "Error Occurred!"

    try:
        content = urllib.request.urlopen(lyrics_url).read()
        soup = BeautifulSoup(content, 'html.parser')
        lyrics = str(soup)

        # lyrics lies between up_partition and down_partition
        up_partition = '<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->'
        down_partition = '<!-- MxM banner -->'
        lyrics = lyrics.split(up_partition)[1]
        lyrics = lyrics.split(down_partition)[0]
        lyrics = lyrics.replace('<br>','').replace('<br/>','').replace('</div>','').strip()
        lyrics = urllib.parse.quote_plus(lyrics)

        return lyrics
    except Exception as _:
        return "Error Occurred!"
