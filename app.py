from flask import Flask, render_template
import pymongo
from pymongo import MongoClient
mongodb_uri = "mongodb+srv://tothienbao6a0:tintom@bulletinchallenge.5ltdrpd.mongodb.net/?retryWrites=true&w=majority"


client = pymongo.MongoClient(mongodb_uri)


db = client.get_database("bulletinchallenge")


app = Flask(__name__)

@app.route('/')

def index():
    try:
      
        client = MongoClient(mongodb_uri)

      
        db = client['spotifyUsers']
        collection = db['spotifyData']

      
        data = collection.find()


        return render_template('index.html', data=data)

    except Exception as e:
        return f"An error occurred: {str(e)}"

    finally:
        
        client.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

