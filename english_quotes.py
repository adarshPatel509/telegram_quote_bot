import urllib, requests
from bs4 import BeautifulSoup

def get_english_quotes(text):
    print("fetching_q_english....")
    text = text.strip().replace(" ", "+")
    query_url = "https://www.brainyquote.com/search_results?q={}".format(text)

    try:
        html = requests.get(query_url)
        soup = BeautifulSoup(html.text, "html.parser")
        results = soup.select("div[class='clearfix'] > a")

        if len(results) == 0:
            return "No results found :(\nSearch for something else :)"
        
        response = ""
        count = 0

        for result in results:
            response += result.getText()
            count += 1
            if count == 8:
                break
            response += "\n\n........\n\n"
        
        response = urllib.parse.quote_plus(response)
        return response
    except Exception as e:
        return "Error Occurred!\n" + str(e)