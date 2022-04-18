from pymongo import MongoClient

class settingPymongo(object):

    def __init__(self, db_name, collection_name):
        uri = 'mongodb://itokita41:itokita41pass@cluster0-shard-00-02.tx265.mongodb.net'
        self.client = MongoClient(uri,
                                  port=27017,
                                  ssl=True,
                                  username='itokita41',
                                  password='itokita41pass',
                                  authSource='admin'
                                  # authMechanism='SCRAM-SHA-256'
                                  )
        self.ssl = True
        self.username = 'itokita41'
        self.password = 'itokita41pass'
        self.authSource = 'admin'
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
