import flask
from flask import request, jsonify
import json
import pymongo
import certifi
from bson import ObjectId
import datetime

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = flask.Flask(__name__)
app.config["DEBUG"] = True


URI = "mongodb+srv://obaidu467:obaidcool@cluster0.kurvu.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(URI, tlsCAFile=certifi.where())
db = client["fin_project"]
mo_data = db["movie_data"]



@app.route('/', methods=['GET'])
def home():
    return "<h1>Web Aggregator API.</p>"


@app.route('/api/search', methods=['POST'])
def search():
    payload = request.json
    #{ "$regex": ".*robert pattin.*" , "$options" : "i"}

    query = payload["query"]
    ret = {}

    #cursor = mo_data.find({"" : { "$regex": query, "$options" : "i"}  })

    # Finding movies
    movies = []

    cursor = mo_data.find( {"movie_title" : { "$regex": query, "$options" : "i"}  } ).limit(1)
    for document in cursor:
        movies.append(document)

    # Finding actors
    actors = []

    cursor = mo_data.find( {"crew" : { "$regex": query, "$options" : "i"}  } ).limit(1)
    for document in cursor:
        actors.append(document)

    ret["movie_title"] = movies
    ret["crew"] = actors
    return_payload = {"object_count" : len(ret), "data" : ret}
    #print((return_payload))
    return JSONEncoder().encode(return_payload)
    


@app.route('/api/search_with_parameter', methods=['POST'])
def search_with_parameter():
    payload = request.json
    #{ "$regex": ".*robert pattin.*" , "$options" : "i"}

    query1 = ".*{}.*".format(payload["year"] )
    query2 = ".*{}.*".format(payload["genre"] )
    ret = []

    if str(query1) == "" and str(query2) == "":
        JSONEncoder().encode(ret_err)
        ret_err = {"error" : "select al least one field"}
        SystemExit(0)

    else:
        
        cursor = mo_data.find({ "$and" : [
                                {"year" : { "$regex": query1, "$options" : "i"}  },
                                {"genre" : { "$regex": query2, "$options" : "i"} } ] 
                })
        for document in cursor:
            ret.append(document)


        return_payload = {"object_count" : len(ret), "data" : ret}
        #print((return_payload))
        return JSONEncoder().encode(return_payload)
     

app.run()