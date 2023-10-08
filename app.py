from flask import Flask, render_template
import pymongo
from pymongo import MongoClient
mongodb_uri = "mongodb+srv://tothienbao6a0:tintom@bulletinchallenge.5ltdrpd.mongodb.net/?retryWrites=true&w=majority"


client = pymongo.MongoClient(mongodb_uri)


db = client.get_database("bulletinchallenge.5ltdrpd.mongodb.net/?retryWrites=true&w=majority")


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def index():
    try:
        # Connect to MongoDB
        client = MongoClient(mongodb_uri)

        # Access your database and collection
        db = client['your-database-name']
        collection = db['your-collection-name']

        # Query the collection and retrieve data
        data = collection.find()

        # Render an HTML template with the data
        return render_template('index.html', data=data)

    except Exception as e:
        return f"An error occurred: {str(e)}"

    finally:
        # Close the MongoDB connection
        client.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

