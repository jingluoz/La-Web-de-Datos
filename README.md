# La Web de Datos

Para este proyecto, se trabajó con el dataset "The Movies Dataset" que se encuentra en [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?resource=download&select=movies_metadata.csv).

Partiendo por una limpieza mediante el archivo [preprocess.py](https://github.com/jingluoz/La-Web-de-Datos/blob/main/preprocess.py) para remover columnas con más del 50% de valores nulos, columnas con valores que poseen más de un 90% de un mismo valor y columnas que no se le encuentran un uso muy importante a simple vista. Generando el archivo [post.csv](https://github.com/jingluoz/La-Web-de-Datos/blob/main/post.csv)

Luego de una limpieza de datos, sigue la converción de estos mismos desde un formato CSV a RDF, cosa que se logró mediante la herramienta [Tarql](https://tarql.github.io), mediante la query que se encuentra en [query.sparql](https://github.com/jingluoz/La-Web-de-Datos/blob/main/query.sparql). Proceso que generó el archivo [OUTPUT.ttl](https://github.com/jingluoz/La-Web-de-Datos/blob/main/OUTPUT.ttl).

Por último, se probaron con diferentes metodos para realizar consultas, como por ejemplo, se trató de emplear en cc7220.dcc.uchile.cl:8900/sparql, tambien se probó mediante el servidor [Apache Jena Fuseki](https://jena.apache.org/documentation/fuseki2/), ambos metodos se descartaron por temas de que sólo una persona podía trabajar con esos metodos. Por ello, se realizó un proyecto en Python desde [Google Colab](https://colab.research.google.com) para poder trabajar de forma colaborativa, para las consultas, se realizaron mediante la librería [rdflib](https://rdflib.readthedocs.io/en/stable/). El proyecto se encuentra en este [enlace](https://colab.research.google.com/drive/1eLW4YQkXDFFzX6WoO1F-52_yfsKjShHR?usp=sharing).
