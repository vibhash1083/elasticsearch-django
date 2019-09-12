  * Clone the project with ```git clone https://github.com/vibhash1083/elasticsearch-django.git```
  * Create a virtual environment and run ```pip install -r requirements.txt``` to install all the dependencies.
  * Install ElasticSearch 7.0.0:
```
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.0.0
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.0.0
```
  * Default port for ElasticSearch is ```http://localhost:9200```. Run the above command and see if it's working and giving the below output:
  ```
  {
  "name" : "5c1c348cdeb2",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "txO3ZdsJTNmB_7zQmOqrFg",
  "version" : {
    "number" : "7.0.0",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "b7e28a7",
    "build_date" : "2019-04-05T22:55:32.697037Z",
    "build_snapshot" : false,
    "lucene_version" : "8.0.0",
    "minimum_wire_compatibility_version" : "6.7.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
  ```
  * Do the migrations and run the django server which is ```http://localhost:8000``` by default.
  * Go to ```http://localhost:8000/search/``` as specified in ```urls.py``` and enter the search text you want to search for in the text box.
  * To Rebuild in the elastic search data use the below command
```
python manage.py search_index --rebuild
```
