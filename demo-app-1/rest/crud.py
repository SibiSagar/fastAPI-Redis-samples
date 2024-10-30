import requests
import redis
from fastapi import FastAPI
import json

#Redis object creation
try:
    redis_obj = redis.Redis(host="localhost", port=6379, db=0)
except redis.exceptions.ConnectionError as e:
    print(f"Error connecting to Redis: {e}")
    
app=FastAPI()

@app.get("/products")
def products():
    req = requests.get("https://dummyjson.com/products")
    req.raise_for_status()
    return req.json()

@app.get("/products/{id}")
def product(id:int):
    cache=redis_obj.get(id)
    if cache:
        print("CACHE HIT")
        return json.loads(cache)
    else:
        print("CACHE MISS")
        req = requests.get(f"https://dummyjson.com/products/{id}")
        req.raise_for_status()
        redis_obj.set(id,json.dumps(req.json()))
        return req.json()