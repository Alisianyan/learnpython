import time, datetime
name=input('как тебя зовут?')
print(f'Hello, {name}')
	
message = {
	'text':'text',
	'time':'timestamp',
	'name':'Nick'
}

db = [
	{
	'text':'1',
	'time':time.time(),
	'name':'masha'
	},
	{'text':'2',
    'time':time.time(),
    'name':'nick'
    }
]

def print_message(message):
	print(message['text'], message['time'], message['name])

def print_messages(db):
	for message in db:
			echo_message(message)
            
	
def send_message(name, text):
    message = {
        'text':text',
        'time':time.time()
        'name':name
        }
    db.append(message)
    
def get_messages(after):
    messages=[]
    for message in db:
        if message['time'] > after:
            messages.append(message)
        return messages
 
messages = get_messages(messages[-1]['time'])
print_messages(messages)
    