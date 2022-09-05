"""
    1. Login to https://firebase.google.com/
    2. Go To Console
    3. Add a New Project
    4. Create DataBase in FirebaseFirestore Option
        > Create it in Test Mode

        if, region selection is asked, please choose india :)
    5. Open Firebase Docs and select the option Build
        (https://firebase.google.com/docs/build?authuser=0&hl=en)
    6. Install Firebase Admin Library
        pip install firebase-admin
    7. Go to Project Settings > Service Account > Generate a New Private Key
    8. Copy the JSON Key in your project. You can rename the JSON file as per your choice
    9. Copy the Firebase Initial Code from Google Firebase Servie Accounts Page and test it
    10. Perform CRUD Operations
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore # DataBase

from Session22A import Dish, Restaurant

cred = credentials.Certificate("service-account.json")
firebase_admin.initialize_app(cred)
print("Firebase Initialized :)")

db = firestore.client()

dish1 = Dish(name="Paneer Tikka", price=360)
dish2 = Dish(name="Veggie Burger", price=100)
dish3 = Dish(name="Veggie Supreme Pizza", price=575)

restaurant = Restaurant(name="Bistro 22", phone="+91 98765 22222",
                        email="contact@bistro.com", operatingHours="2PM - 11PM", ratings=4.7,
                        menu = [vars(dish1), vars(dish3)]
                        )

print(vars(restaurant))
document_to_update = vars(restaurant)

# Adding Data to Firestore DB
# db.collection('restaurants').add(document)
# print("Data Saved:)")

# Fetch all the documents
# documents = db.collection('restaurants').get()
# for document in documents:
#     print(document.id)
#     print(document.to_dict())

# Update the Document
# db.collection('restaurants').document('NxZqhyvvGms7X5KVzF7u').set(document_to_update)
# print("Document Updated..")

# Get Single Document
# document = db.collection('restaurants').document('NxZqhyvvGms7X5KVzF7u').get)()


# Delete the Document
db.collection('restaurants').document('NxZqhyvvGms7X5KVzF7u').delete()
print("Document Deleted...")