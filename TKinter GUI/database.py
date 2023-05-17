
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import urllib

uri = "mongodb+srv://abkoder:"+urllib.parse.quote("@AR.yusufi321db")+"@quizzy.elc67.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def saveData(data):
    try:
        print("Saving your data...")
        db = client['depression']
        collection = db['patients']
        patient_id = collection.insert_one(data).inserted_id
        print("Data Saved Successfully")
    except Exception as e:
        print("Error in saving data")
        print(e)



