# 参考
# mongodb+srv://<username>:<password>@cluster0.tx265.mongodb.net/test
# https://qiita.com/chenglin/items/ecf6f67e8f80c4750204
# djongo://itokita41:itokita41pass@cluster0.tx265.mongodb.net:27017/?rosterdb?authSource=admin
from pymongo import MongoClient
url = "djongo://itokita41:itokita41pass@cluster0.tx265.mongodb.net:27017"
db = MongoClient.rosterdb
Users = db.Users



