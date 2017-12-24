import pymongo
import json
import sys

client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = sys.argv[1]
