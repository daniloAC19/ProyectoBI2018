__author__ = 'danilo'

import couchdb
import sys
import urllib2
import elasticsearch as es

from couchdb import view

URL = 'localhost'
db_name = 'danilo_db'


'''========couchdb'=========='''
server = couchdb.Server('http://'+URL+':5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

view = "vistaQuito/vistaQuito"

LIMIT_OF_DOCUMENTS = 1000

client = es.Elasticsearch(hosts=[{'host' : 'localhost', 'port' : 9200}])

#while len(db.view(view, limit=LIMIT_OF_DOCUMENTS)) > 0:
for data in db.view(view, limit=LIMIT_OF_DOCUMENTS):
	json_data = {}
	json_data = db.get(data['id'])
	json = {}
	json['id'] = json_data['id']
	json['text'] = json_data['text']
	json['fecha'] = json_data['created_at']
	json['sentimiento'] = json_data ['sentimiento']
	try:
		client.index(index="Quito", doc_type="Quito",body=json,ignore=400)
	except es.exceptions.TransportError as e:
		if e.error != 'index_already_exists_exception':
			raise
