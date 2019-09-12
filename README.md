searchr = PostDocument.search().filter("term", title="the")


Index - Like a database

Document - JSON - like a DB record

Shard - horizontal partition

Replicas - ensure availability of systems

Node - a server

Cluster - collection of shards

ElasticSearch is RESTful, near realtime search engine.

Create an index

http://localhost:9200/test

```
PUT test
{
    "settings" : {
        "number_of_shards" : 1
    },
    "mappings" : {
        "type1" : {
            "properties" : {
                "field1" : { "type" : "text" }
            }
        }
    }
}
```

Response
```
{
    "acknowledged": true,
    "shards_acknowledged": true,
    "index": "test"
}
```

Delete Index
DELETE /twitter

Get Index
GET /twitter

Get mapping
test/_mapping/_doc/


Reindex
```
POST http://localhost:9200/_reindex/

{
  "source": {
    "index": "test"
  },
  "dest": {
    "index": "new_test"
  }
}
```

Document API

Install ES 6.2.0
```
docker pull docker.elastic.co/elasticsearch/elasticsearch:6.2.0
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.0
```

To Rebuild in the elastic search data use the below command
```
python manage.py search_index --rebuild
```

https://github.com/archatas/experiment-with-django-and-elasticsearch