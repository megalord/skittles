import os
import time
from slackclient import SlackClient


sc = SlackClient(os.environ['SLACK_API_TOKEN'])


def handle_event(event):
    print(event)
    if event['type'] == 'message':
        text = event.get('text', '')
        user = event.get('user', '')
        if 'funny' in text:
            sc.rtm_send_message('random', 'I hear that Johnny guy is pretty funny')
        elif user == 'UFMQUEJR4':
            sc.rtm_send_message('random', 'H-E-B')
    else:
        print(event)


def main():
    if sc.rtm_connect():
        while sc.server.connected:
            for event in sc.rtm_read():
                try:
                    handle_event(event)
                except Exception as e:
                    print('Caught exception handling event:')
                    print(event)
                    print(e)
            time.sleep(1)
    else:
        print('Connection Failed')


if __name__ == '__main__':
    main()
