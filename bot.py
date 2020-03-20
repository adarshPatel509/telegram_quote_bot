import time
from utils import get_message_updates, get_last_update_id, reply_all_unresolved_updates

def main():
    last_update_id = None

    while True:
        updates = get_message_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            reply_all_unresolved_updates(updates)
        else:
            last_update_id = None
        time.sleep(0.5)

if __name__ == '__main__':
    main()