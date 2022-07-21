conversation1 = {
    'number1': '+91 99999 11111',
    'number2': '+91 99999 22222',
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
            'text': 'Thank you for understanding',
            'sender': '+91 99999 11111',
            'timeStamp': '12:55',
            'status': 3
        }

    ]
}

conversation3 = {
    'number1': '+91 99999 11111',
    'number2': '+91 99999 44444',
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

# Expected Result/Output
#my_whats_app = [conversation3, conversation1, conversation2]

def search_message_by_sender(phone_number):
    for idx in range(len(my_whats_app)): # Iterates in conversations
        for idx1 in range(len(my_whats_app[idx]['messages'])): # iterates in messages list in every conversation
            if my_whats_app[idx]['messages'][idx1]['sender'] == phone_number:
                print(my_whats_app[idx]['messages'][idx1])
                print("~~~~~~~~~~~~~~~~~~~~~")


def sort_conversations():
    n = len(my_whats_app)
    for idx1 in range(0, len(my_whats_app)): # 0, 1, 2, 3, 4
        for idx2 in range(0, n-idx1-1):

            if len(my_whats_app[idx2]['messages']) < len(my_whats_app[idx2+1]['messages']):
                my_whats_app[idx2], my_whats_app[idx2+1] = my_whats_app[idx2+1], my_whats_app[idx2]


def filter_conversations():
    for idx in range(len(my_whats_app)): # Iterates in conversations
        for idx1 in range(len(my_whats_app[idx]['messages'])): # iterates in messages list in every conversation
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(my_whats_app[idx]['messages'][idx1]['text'])
            print(my_whats_app[idx]['messages'][idx1]['sender'])
            print(my_whats_app[idx]['messages'][idx1]['timeStamp'])
            if my_whats_app[idx]['messages'][idx1]['status'] == 1:
                print('\u2713')
            else:
                print('\u2717')

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print()


# Menu Driven Program
print("Welcome to WhatsApp")
print("~~~~~~~~~~~~~~~~~~~")

choice = "yes"

while choice == "yes":
    print("1. [Search] Message By Sender")
    print("2. [Sort] the Conversations based on messages length")
    print("3. [Filter] the Conversations to display only messages or text inside messages")
    option = int(input("Enter Your Option (1, 2 or 3): "))

    if option == 1:
        print("Search Message By Sender")
        number = input("Enter the Phone Number: ")
        search_message_by_sender(phone_number=number)
    elif option == 2:
        print(" Sort the Conversations based on messages length")
        sort_conversations()
        print("SORTED CONVERSATIONS:")
        for idx in range(len(my_whats_app)):
            print(my_whats_app[idx])
            print("^^^^^^^^^^^^^^^^^^^^^")
            print()
    elif option == 3:
        print("Filter the Conversations to display only messages or text inside messages")
        filter_conversations()
    else:
        print("Invalid Option")

    choice = input("yes to continue and no to quit: ")

print("Thank You For using WhatsApp")

