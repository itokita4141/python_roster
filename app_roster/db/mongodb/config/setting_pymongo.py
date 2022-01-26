# 参考
# mongodb+srv://<username>:<password>@cluster0.tx265.mongodb.net/test
# https://qiita.com/chenglin/items/ecf6f67e8f80c4750204
# mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[database][?options]]
# djongo://itokita41:itokita41pass@cluster0.tx265.mongodb.net:27017/?rosterdb?authSource=admin
from pymongo import MongoClient

# url = "mongodb://itokita41:itokita41pass@cluster02.tx265.mongodb.net:27017/rosterdb?authSource=admin"
# with MongoClient(url) as client:
#     rosterdb = client.rosterdb
#     app_roster_users = rosterdb.app_roster_users
#     name = app_roster_users(db=rosterdb, filter={id: 1})

class settingPymongo(object):

    def __init__(self, db_name, collection_name):
        # url = "mongodb://itokita41:itokita41pass@cluster02.tx265.mongodb.net:27017/rosterdb?authSource=admin"
        # url = "mongodb://itokita41:itokita41pass@cluster0-shard-00-02.tx265.mongodb.net"
        # self.client = MongoClient(url, 27017)
        # self.username = 'itokita41'
        # self.password = 'itokita41pass'
        # self.authSource = 'admin'
        # self.authMechanism = 'SCRAM-SHA-256'
        # uri = 'mongodb://itokita41:itokita41pass@cluster0-shard-00-02.tx265.mongodb.net:27017/rosterdb?ssl=false&authSource=admin'
        uri = 'mongodb://itokita41:itokita41pass@cluster0-shard-00-02.tx265.mongodb.net'
        self.client = MongoClient(uri,
                                  port=27017,
                                  ssl=False,
                                  username='itokita41',
                                  password='itokita41pass',
                                  authSource='admin',
                                  authMechanism='SCRAM-SHA-256'
                                  )
        # con = MongoClient(uri, port=27017)
        # db = con.rosterdb
        # print(db)
        # collections = db.app_roster_users
        # print(collections)
        # found = collections.find({'app_roster_users': True})  # find returns all entries
        # print(found)
        # for i in found:
        #     print(i)
        #
        # self.db = self.client[db_name]  # DB名を設定
        # # self.client = MongoClient(url, 27017)
        # self.ssl = False
        # self.username = 'itokita41'
        # self.password = 'itokita41pass'
        # self.authSource = 'admin'
        # self.authMechanism = 'SCRAM-SHA-256'
        self.db = self.client[db_name]  # DB名を設定
        self.collection = self.db.get_collection(collection_name)

    def find_one(self, projection=None,filter=None, sort=None):
        return self.collection.find_one(projection=projection,filter=filter,sort=sort)

    def find(self, projection=None,filter=None, sort=None):
        return self.collection.find(projection=projection,filter=filter,sort=sort)

    def collection_names(self):
        return self.db.collection_names()

    def list_collection_names(self):
        return self.db.list_collection_names()

        # # pymongo
        # mongo = settingPymongo('rosterdb', 'app_roster_users')
        # print('-----------------find_One-----------------')
        # print(type(findOne))
        # print(findOne)
        #
        # find = mongo.find()
        # print('-------------------find-------------------')
        # print(type(find))
        # for doc in find:
        #     print(doc)

    # def collection_names(self):
    #     return self.db.collection_names()
    #
    # def list_collection_names(self):
    #     return self.db.list_collection_names()
