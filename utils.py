import json, requests
from response import get_response_message

#read constants from config file
with open("./config.json") as config_file:
    data = json.load(config_file)

TOKEN = data['api_token']

#base api url
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

#util functions
def get_response_from_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    json_res = json.loads(content)
    return json_res

def get_message_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    res = get_response_from_url(url)
    return res

def send_text_reply(message, chat_id):
    #fetch response form 3rd party apis
    res_message = get_response_message(message)
    url = URL + "sendMessage?text={}&chat_id={}".format(res_message, chat_id)
    #send response to user
    get_response_from_url(url)

def reply_all_unresolved_updates(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat_id = update["message"]["chat"]["id"]
            send_text_reply(text, chat_id)
        except Exception as e:
            print(e)

def get_last_update_id(updates):
    updates = updates["result"]
    if len(updates) > 0:
        return updates[len(updates)-1]["update_id"]
    return None
