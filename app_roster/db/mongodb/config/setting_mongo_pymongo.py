# 参考 z
# mongodb+srv://<username>:<password>@cluster0.tx265.mongodb.net/test
# djongo://itokita41:itokita41pass@cluster0.tx265.mongodb.net:27017/rosterdb?authrizrDB=admin
from pymongo import MongoClient
url = "djongo://itokita41:itokita41pass@cluster0.tx265.mongodb.net:27017"
db = MongoClient.rosterdb
Users = db.Users



