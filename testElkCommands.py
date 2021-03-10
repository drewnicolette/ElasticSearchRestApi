from elasticsearch import Elasticsearch
import json

es = Elasticsearch()
es = Elasticsearch(hosts=[{"host": "34.122.187.106", "port": 9200}])
user = "Mark Albert"
# search_param = {"_source": "name","query": {"match_all": {}}}

search_param = {"query": {"match": {"name": user}}}
response = es.search(index="verified_tweets1", body=search_param, size=10000)
# response = es.search(index="verified_tweets1", body=search_param)
# print(json.dumps(response, indent=4, sort_keys=True))
data = json.loads(json.dumps(response))["hits"]["hits"]
print(data)