from datetime import datetime
import requests

def print_message(message):
    message_time = datetime.fromtimestamp(message['time'])
    message_time = message_time.strftime('%Y/%m/%d %H:%M:%S')
    print(message_time, message['name'])
    print(message['text'])
    print()
    
after = 0

while True:
    responce - requests.get(http://127.0.0.1/messages, params={'after':after})
    messages = responce.json().['messages']
    
    for message in messages:
        print_message(message)
        after = message['time']