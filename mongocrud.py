import pymongo
from bson import ObjectId
#connected database
connection = pymongo.MongoClient('localhost',27017)
#create database
database = connection['dbase']
#create collection
collection = database['table']
print("database connected")

def insert_record(data):
    document = collection.insert_one(data)
    return document.inserted_id

def update_or_create(document_id, data) :
    document = collection.update_one({'id': ObjectId(document_id)},{"$set":data}, upsert=True)
    return document.acknowledged


def update_existing(document_id, data):
    document = collection.update_one({'_id': ObjectId(document_id)},{"$set":data})
    return document.acknowledged

def get_single_record(document_id) :
    data=collection.find_one({'_id': ObjectId(document_id)})
    return data
def remove_record(document_id) :
    document = collection.delete_one({'_id' : ObjectId(document_id)})
    return document.acknowledged


connection.close()





#insert record
'''data={"name": "ravi","place":"kerala"}
id = insert_record(data)
print(id)'''

#retrieve specific record
'''document_id='60743b2e5c95be1d23dc8465'
record = get_single_record(document_id)
print(record) '''

#update specific
'''document_id = '60743b2e5c95be1d23dc8465'
data = {'name' : 'Athul'}
ack = update_existing(document_id , data)
print(ack)'''

'''document_id = '60743ac53390d2d29b6fa381'
data = {'name' : 'solo', 'place':'goa'}
ack = update_or_create(document_id , data)
print(ack)'''

document_id ='60743b2e5c95be1d23dc8465'
ack = remove_record(document_id)
print(ack)