import urllib
from bs4 import BeautifulSoup

def get_hindi_quotes(text):
    text = text.strip().replace(" ", "+")
    query_url = "https://www.shayarism.com/?s={}".format(text)
    
    try:
        content = urllib.request.urlopen(query_url).read()
        soup = BeautifulSoup(content, "html.parser")
        result = soup.select("div[class='post-entry']")

        if len(result) == 0:
            return "No results found :(\nSearch for something else :)"

        response = ""
        count = 0

        for res in result:
            response += res.getText()
            count += 1
            if count == 5:
                break
            response += "\n.......\n"
        
        response = urllib.parse.quote_plus(response)
        return response
    except Exception as _:
        return "Error Occurred!"