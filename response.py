import urllib
from lyrcis import get_lyrics

def get_response_message(text):
    query = text.split(" ")
    command = query[0]
    avail_commands = ["/lyrics", "/q_hindi", "/q_english", "/help", "/start"]
    help_text = "Enter a command you want to search for:\n eg: \n /q_hindi zindagi \n /q_english love \n /lyrics You & I"
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
    
    options = {
        "/lyrics": get_lyrics(message),
        "/q_hindi": get_hindi_quotes(message),
        "/q_english": get_english_quotes(message),
        "/help": help_text,
        "/start": help_text
    }

    return options.get(command, "Invalid Command!\n{}".format(help_text))


def get_hindi_quotes(keywords):
    return keywords

def get_english_quotes(keywords):
    return keywords
