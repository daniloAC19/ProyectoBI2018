
import couchdb
import sys
import textblob
import os
import re
import json

from couchdb import view
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import urllib3
import textblob
from couchdb import view
from textblob import TextBlob

URL = 'localhost'
db_name = 'danilo_db'
server = couchdb.Server('http://'+URL+':5984/')

try:
    print(db_name)
    db = server[db_name]
    print('conexion exitosa')
except:
    sys.stderr.write("Error: Base de datos no encontrado. Terminar\n")
    sys.exit()


view = "vistaCuenca/vistaCuenca"

with open('train.json','r') as fp:
   cl = NaiveBayesClassifier(fp, format="json")

#sys.stdout=open("Train1.json","w")
if len(db.view(view)) > 0:
    for data in db.view(view):
        json_data = {}
        json_data1 = {}
        json_data = db.get(data['id'])
        textoIngesado = data['value']
        textoIngesado1 =TextBlob(expresionRegularFiltrar.sub('', textoIngesado))
        polarity_value = textoIngesado1.sentiment.polarity * 100.0
        if polarity_value == 0:
           polarity = 'neu'
        elif polarity_value < 0:
           polarity = 'no'
        else:
           polarity = 'si'
	subjectivity = textoIngesado1.sentiment.subjectivity
	json_data['sentimiento'] = polarity
	try:
           db.save(json_data)
        except:
           print("Error al guardar")

