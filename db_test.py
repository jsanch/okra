#db test

from pymongo import MongoClient
import datetime

def get_db_conection(db):
	client = MongoClient()
	return client[db]


db = get_db_conection("okra")



tab = {
		'invitation_id' : 1,
        'user_id' : 2,
        'tab_id' : 5,
        'tab_name': 'Wagamama'
      }
#getting tabs collection
tabs = db.tabs
tabs_id = tabs.insert(tab)


# print db.collection_names()

print tabs.find_one({"_id":tabs_id})


