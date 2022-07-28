"""
    Queries ?
    1. List of MovieTicket Objects -> Sorting Based on Seat Number
    2. Assignment Soln: WhatsApp Conversation Sorting
    3. OOPS Function Executions
    4.

    DS Algo Assignments
    10 - 20

"""

conversation1 = {
    'number1': '+91 99999 11111',
    'number2': '+91 99999 22222',
    'size': 0,
    'messages': [
        {
            'text': 'Hello',
            'sender': '+91 99999 11111',
            'timeStamp' : '16:10',
            'status': 1
        },
        {
            'text': 'Hi, How are you ?',
            'sender': '+91 99999 22222',
            'timeStamp': '16:10',
            'status': 2
        }

    ]
}

conversation2 = {
    'number1': '+91 99999 11111',
    'number2': '+91 99999 33333',
    'size': 0,
    'messages': [
        {
            'text': 'Python Kaisi Chal Rahi Hai',
            'sender': '+91 99999 11111',
            'timeStamp': '13:55',
            'status': 3
        },
        {
            'text': 'Baki Sab toh Badhiya Hai. recusrion ne he dimaag ghumaya hai',
            'sender': '+91 99999 33333',
            'timeStamp': '17:00',
            'status': 2
        },
        {
            'text': 'Hi',
            'sender': '+91 99999 11111',
            'timeStamp': '12:55',
            'status': 3
        }

    ]
}

conversation3 = {
    'number1': '+91 99999 11111',
    'number2': '+91 99999 44444',
    'size': 0,
    'messages': [
        {
            'text': 'Thank you for understanding',
            'sender': '+91 99999 11111',
            'timeStamp': '12:55',
            'status': 3
        }
    ]
}
# idx:              0               1               2
# message_length    2               3               1
my_whats_app = [conversation1, conversation2, conversation3]

for idx in range(len(my_whats_app)):
    for messageIdx in range(len(my_whats_app[idx]['messages'])):
        my_whats_app[idx]['size'] += len(my_whats_app[idx]['messages'][messageIdx]['text'])

for idx in range(len(my_whats_app)):
    print(my_whats_app[idx])

def sort_conversations():
    # n: 3
    n = len(my_whats_app)

    # idx1: 0, 1, 2
    for idx1 in range(0, len(my_whats_app)):
        # for idx1: 0, idx2: 0, 1
        # for idx1: 1, idx2: 0
        # for idx1: 2, idx2: NO
        for idx2 in range(0, n-idx1-1):
            # for idx1: 0, idx2: 0, 1
            if my_whats_app[idx2]['size'] < my_whats_app[idx2+1]['size']:
                my_whats_app[idx2], my_whats_app[idx2+1] = my_whats_app[idx2+1], my_whats_app[idx2]


sort_conversations()
print()
for idx in range(len(my_whats_app)):
    print(my_whats_app[idx])

sender = {
    'sender': my_whats_app[0]['messages'][0]['sender'],
    'text': my_whats_app[0]['messages'][0]['text'],
    'size': len(my_whats_app[0]['messages'][0]['text'])
}

for idx in range(len(my_whats_app)):
    for messageIdx in range(len(my_whats_app[idx]['messages'])):
        if len(my_whats_app[idx]['messages'][messageIdx]['text']) < len(sender['text']):
            sender['sender'] = my_whats_app[idx]['messages'][messageIdx]['sender']
            sender['text'] =  my_whats_app[idx]['messages'][messageIdx]['text']
            sender['size'] = len(my_whats_app[idx]['messages'][messageIdx]['text'])


print("MINIMUM SENDER")
print(sender)