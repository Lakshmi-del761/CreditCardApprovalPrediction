from pymongo import MongoClient
import config

# Create MongoDB client
client = MongoClient(config.MONGO_URI)

# Select the database
db = client[config.DATABASE_NAME]

# Function to get any collection
def get_collection(collection_name):
    return db[collection_name]
