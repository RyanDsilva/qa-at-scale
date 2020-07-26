# Local Development Guide 👨‍💻

1. Create virtual environment (I use pipenv)

```
pipenv --python 3.8
pipenv shell
```

2. Install Requirements

```
pip install -r requirements.txt
```

3. Start ElasticSearch

```
docker run -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.8.0
```

4. Start the FastAPI Server

```
uvicorn main:app
```

> The first time will take longer due to model download

5. Use Postman to make the Requests
