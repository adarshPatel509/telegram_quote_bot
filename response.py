import urllib
from lyrcis import get_lyrics
from hindi_quotes import get_hindi_quotes
from english_quotes import get_english_quotes

def get_response_message(text):
    query = text.split(" ")
    command = query[0]
    avail_commands = ["/lyrics", "/q_hindi", "/q_english", "/help", "/start"]
    help_text = urllib.parse.quote_plus("Enter a command you want to search for:\n eg: \n /q_hindi zindagi \n /q_english love \n /lyrics You & I")
    message = ""

    if len(query) > 1 and command in avail_commands:
        message = " ".join(query[1:])
    elif command in avail_commands:
        message = "Enter name/keyword you want to search for:\n eg: \n /q_hindi zindagi \n /q_english love \n /lyrics You & I"
        message = urllib.parse.quote_plus(message)
        return message
    else:
        message = "Invalid Command!\n{}".format(help_text)
        return message
    
    #do command specific action
    if command == "/lyrics":
        return get_lyrics(message)
    elif command == "/q_hindi":
        return get_hindi_quotes(message)
    elif command == "/q_english":
        return get_english_quotes(message)
    elif command == "/help" or command == "/start":
        return help_text
    else:
        return "Invalid Command!\n{}".format(help_text)
