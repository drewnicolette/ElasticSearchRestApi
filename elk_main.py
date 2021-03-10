from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch
import json

es = Elasticsearch(hosts=[{'host':"{}}", 'port':9200}])
app = Flask(__name__)
api = Api(app)



class Tweet(Resource):
    def get(self, user):
        search_param = {"query": {"match": {"name": user}}}
        response = es.search(index="verified_tweets1", body=search_param,size=10000)
        formatted_response = json.loads(json.dumps(response))["hits"]["hits"]
        if not formatted_response:
            abort(404, message=f"Could not find any tweets for {user}")
        return formatted_response

class Count_Documents(Resource):
    def get(self, idx):
        response = es.count(index=idx)
        if "status" in json.loads(json.dumps(response)):
            abort(404, message=f"Could not find {idx} index")
        return json.loads(json.dumps(response))

class GetAllVerifiedTweeters(Resource):
    def get(self, idx):
        search_param = {"_source": "name","query": {"match_all": {}}}
        response = es.search(index="verified_tweets1", body=search_param,size=10000)
        data = json.loads(json.dumps(response))["hits"]["hits"]
        all_users = []
        for member in data:
            user = member["_source"]["name"]
            all_users.append(user)
        return json.loads(json.dumps(all_users))

api.add_resource(Tweet, "/user_tweets/<string:user>")
api.add_resource(Count_Documents, "/count/<string:idx>")
api.add_resource(GetAllVerifiedTweeters, "/all_verified_users/<string:idx>")

if __name__ == "__main__":
    app.run(debug=True)