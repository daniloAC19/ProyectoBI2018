
__author__ = 'danilo'
import couchdb
import sys
import urllib2
import re

from couchdb import view

URL = 'localhost'
db_name = 'danilo_db'

#Conexion a la base de datos.
server = couchdb.Server('http://'+URL+':5984/') 
try:
    print (db_name)
    db = server[db_name]
    print ('conectado exitosamente')
except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

#Extraemos la vista creada
view = "vistaGuayaquil/vistaGuayaquil"

#Definimos la estructura de una URL, para limpiar las URL de los
#tweets con la ayuda de un regex
url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
url2= '(www\.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
emoticones= "['\&\-\.\/()=:;]+"
expresionRegularFiltrar = re.compile(emoticones+'|'+url+'|'+url2)

#Proceso de extraer cada tweets e ir limpiado de la base del couchdb.
if len(db.view(view)) > 0:
    for data in db.view(view):
        json_data = {}
        json_data = db.get(data['id'])
        json_data['text'] = expresionRegularFiltrar.sub('', data['value'])
        try:
            db.save(json_data)
        except:
            print "Data repeated..."

print ("acabado")
