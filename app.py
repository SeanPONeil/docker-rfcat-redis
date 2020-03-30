import bitstring
import os
from rflib import *
from redis import Redis
from dotenv import load_dotenv

load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST", "redisdb")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

def setup_rfcat(debug):
    if debug:
        d = RfCat()
        d.setMdmModulation(MOD_ASK_OOK)
        d.setFreq(RFCAT_FREQ)
        d.setMdmSyncMode(RFCAT_MDM_SYNC_MODE)
        d.setMdmDRate(RFCAT_BAUD)
        return d

#setup_rfcat()
redis = Redis(host=REDIS_HOST, port=REDIS_PORT)

p = redis.pubsub()
p.subscribe("rfcat")

for message in p.listen():
    print("message received: ")
    print(message)
