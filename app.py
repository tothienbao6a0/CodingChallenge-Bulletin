from flask import Flask
import pymongo
mongodb_uri = "mongodb+srv://tothienbao6a0:tintom@bulletinchallenge.5ltdrpd.mongodb.net/?retryWrites=true&w=majority"


client = pymongo.MongoClient(mongodb_uri)


db = client.get_database("bulletinchallenge.5ltdrpd.mongodb.net/?retryWrites=true&w=majority")


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
