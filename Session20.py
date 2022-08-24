"""
    Install pymongo

    pip install pymongo
    pip install "pymongo[srv]"

    Pymongo Docs Tutorial
    https://pymongo.readthedocs.io/en/stable/tutorial.html

"""
import pymongo


# For Windows if SSL Error
# import certifi
# ca = certifi.where()
# client = pymongo.MongoClient("mongodb+srv://atpl:atpl@cluster0.eh8zx.gcp.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
client = pymongo.MongoClient("mongodb+srv://atpl:atpl@cluster0.eh8zx.gcp.mongodb.net/?retryWrites=true&w=majority")
db = client['gw2022pd1']
# db = client.gw2022pd1
print("MongoDB Connection Done...")

collections = db.list_collection_names()
print(collections)

documents = db['users'].find()
for document in documents:
    print(document)


