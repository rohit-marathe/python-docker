from pymongo import MongoClient
from flask import Flask

app = Flask(__name__)

# Connect to the MongoDB database
client = MongoClient("mongodb://localhost:27017/mypythonapp")
db = client["mydatabase"]
collection = db["mycollection"]

# Insert a document into the collection
document = {"message": "Hello from Python App!"}
collection.insert_one(document)

@app.route('/')
def hello_world():
    return 'Hello, World! This is the Python App connected to MongoDB.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

