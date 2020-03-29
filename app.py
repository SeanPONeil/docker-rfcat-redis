import os
from redis import Redis

REDIS_HOST = os.environ['REDIS_HOST']
REDIS_PORT = os.environ['REDIS_PORT']

redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

p = redis.pubsub()
p.subscribe("rfcat")

for message in p.listen():
    print("message received: ")
    print(message)
