import typing
import mysql.connector as mariadb
from dotenv import load_dotenv
import pymongo
import os

load_dotenv()

if typing.TYPE_CHECKING:
    from Clases.Cancion import Cancion


class ServicioCancionMongoDB:
    def __init__(self):
        #si la ip no conecta, conectarse a localhost
        self.mongo_host = "172.23.151.3"
        self.mongo_puerto = "27017"
        self.mongo_fuera = 1000
        self.mongo_uri = "mongodb://"+self.mongo_host+":"+self.mongo_puerto+"/"
        self.mongo_basedatos = "Spotify"
        self.mongo_coleccion = "cancion"
        try:
            self.cliente = pymongo.MongoClient(self.mongo_uri,serverSelectionTimeoutMs=self.mongo_fuera)
            self.baseDatos = self.cliente[self.mongo_basedatos]
            self.coleccion = self.baseDatos[self.mongo_coleccion]
            print("conexion exitosa con mongo")
        except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
            print("Tiempo exedido " + errorTiempo)
        except pymongo.errors.ConnectionFailure as errorConexion:
            print("Fallo al conectarse a mongodb " + errorConexion)

    def guardar(self, cancion: 'Cancion'):
        documento = {
            "nombre":cancion.name,
            "artista":cancion.author,
            "ranking":cancion.ranking,
            "pais":cancion.country,
            "fecha":cancion.date
        }
        self.coleccion.insert(documento)

    def guardar2(self):
        print("entro")
        documento = {
            "nombre": "algo",
            "artista": "algo",
            "ranking": "algo",
            "pais": "algo"
        }
        self.coleccion.insert_one(documento)



