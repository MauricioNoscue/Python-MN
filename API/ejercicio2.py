import psycopg2
import requests


class conexion:
    def __init__(self):
        self.servidor = "localhost"
        self.usuario = "postgres"
        self.password = "123456"
        self.puerto = "5432"
        self.nombre = "corredor"
        
    def conectar (self):
        print("holsa")