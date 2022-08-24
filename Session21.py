import pymongo


class Customer:

    def __init__(self, name=None, phone=None, email=None, age=None, gender=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender


class MongoDBHelper:

    def __init__(self):
        client = pymongo.MongoClient(
            "mongodb+srv://atpl:atpl@cluster0.eh8zx.gcp.mongodb.net/?retryWrites=true&w=majority")
        # Select the DataBase in MongoDB
        self.db = client['gw2022pd1']
        # From the MongoDB Select the Collection
        self.collection = self.db['customers']

    def insert(self, document):
        result = self.collection.insert_one(document)
        # print(result, type(result))
        print("Inserted Data:", result.inserted_id)

    def fetch(self):
        documents = self.collection.find()
        for document in documents:
            print(document, type(document))

    def fetch_selected(self, query):
        documents = self.collection.find(query)
        for document in documents:
            print(document)

    def delete(self, query):
        result = self.collection.delete_one(query)
        print(result.deleted_count)

    def update(self, document, query):
        update_query = {"$set": document}
        result = self.collection.update_one(query, update_query)
        print(result.modified_count)


def main():
    db_helper = MongoDBHelper()

    customer1 = Customer(name="Shawn", phone="7777755555",
                         email="shawn@example.com", age=23, gender="male")
    customer1.subjects = [
        {
            "name": "Physics",
            "marks": 90
        },
        {
            "name": "Maths",
            "marks": 90
        }
    ]

    customer_dictionary = vars(customer1)
    print(customer_dictionary, type(customer_dictionary))

    db_helper.insert(document=customer_dictionary)
    # db_helper.fetch()

    # query = {"phone": "9999955555"}
    # db_helper.fetch_selected(query)
    # db_helper.delete(query)

    # query = {"phone": "8888855555"}
    # db_helper.update(document=customer_dictionary, query=query)

    # query = {"age": {"$gte": 22}}
    # db_helper.fetch_selected(query)

if __name__ == "__main__":
    main()