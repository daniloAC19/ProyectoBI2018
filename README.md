#                                                    ESCUELA POLITÉCNICA NACIONAL

# ProyectoBI2018

# Diseño e Implementación de un modelo de clasificación de sentimientos utilizando machine learning

# Nombre: Danilo Angamarca Casa

# Objetivo General:

 Implementar e investigar el funcionamiento de un clasificador de sentimientos utilizando los algoritmos de aprendizaje vistos en clase y los datos recolectados de Twitter para identificar tendencias de opinión en las 3 ciudades más importantes del país por el tema de “CONSULTA POPULAR” del domingo 4 de febrero de 2018.
 
# Objetivos específicos: 

-	Crear un clasificador de sentimiento en español utilizando datos extraídos de Twitter para minar opinión pública en las ciudades de Quito, Guayaquil y Cuenca. 
-	Identificar y seleccionar las herramientas necesarias para procesar y analizar datos en tiempo real provenientes de Twitter.

# Herramientas

- CouchDB
- ElasticSearch
- Exel
- PyCharm

# FASES DEL PROYECT0

1) Adquisicion de Datos

Empezamos por la recoleccion o cosecha de tweets desde el inicio de curso, pero lo primordial fue recolectar tweets en la temporada de elleciones ya que es lo que nos importaba, para esta recoleccion utilizamos la base de datos no relacional CouchDB y con la ayuda de un script en lenguaje python donde debemos ingresar unas credenciiales que debemos obtener en la pagina de twitter previamente creando una cuenta en esta red social.

2) Pre-procesamiento de Datos

Una vez que tenemos una base de datos con nuestros tweets en CouchDB, las debemos filtrar los tweets por las tres ciudades en la cuales vamos a medir la tendencia de votos, para ellos se procede a una vista para cada ciudad, es decir tres vistas las cuales van a filtrar los tweets referentes a cada ciudad y en lenguaje español. Esto se lo realiza ingresado un sentencia de codigo en lenguaje javascript y a su vez vamos a declarar que nos retorne el id y el texto del tweet. 

3) Procesamiento de Datos

En esta parte vamos a limpiar los tweets de cada vista del couchDb mediante un script codificado en python para que por medio de expresiones regulares eliminemos todos los caracteres especiales y URLs que por defecto vienen en el texto de cada tweet. Este paso es fundamental ya que los Tweets deben estar en un texto claro y legible sin caracteres especiales ni emoticones para que haya un buen analisis de sentimientos posteriormente. tenemos un script de limpieza para cada vista, incluso y fundamentalmente para la vista que de tweets que nos serviran como train para nuestra maquina. 

4) Análisis de Datos

Procedemos a analizar el sentimientos de los tweets de cada vista mediante nuestro train que contiene tweets de todo el Ecuador y cuyos valores de sentimientos fueron ingresados manualmente, mediantes este train se analiza cada tweet y se lo devuelve al mismo couchDB solo que en este caso retorna con un campo adicional que es el sentimiento o polaridad, una ves que tenemos los tweets analizados y con su respectivo valor de sentimiento estan listos para migrar al ElasticSearch donde se realizara el ultimo filtro para determinar la tendencia del "Si", "Neutro" o del "No" en cada ciudad. 

5) Presentación de Datos

Una ves que los datos han sido migrados al elasticSearch estan listos para ser filtrados por palabras claves que determinen que los tweets pertenecen o hacen referencia a la consulta popular, una ves hecho esto se lo filtra mediante el atributo de sentimiento para poder derterminar el resultado final o porcentajes finales del "SI" o del "NO" en cada ciudad. Los datos fueron coherentes con los resultados oficiales de las elecciones.  
