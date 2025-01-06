import psycopg2

class Conexion:
    def __init__(self):
        self.servidor = "localhost"
        self.usuario = "postgres"
        self.password = "123456"
        self.puerto = "5432"
        self.base_datos = "corredor"
    
    def conectar(self):
        try:
  
            conexion = psycopg2.connect(
                host=self.servidor,
                user=self.usuario,
                password=self.password,
                port=self.puerto,
                dbname=self.base_datos
            )
            print("Conexión exitosa")
            
            # cursor = conexion.cursor()
            # cursor.execute("SELECT nombre_usuario FROM usuario")
            # version = cursor.fetchall()
            # # print(version)
            # for persona in version:
            #     print(persona[0])
            
            # return conexion
        except psycopg2.Error as e:
            print(f"Error de conexión: {e}")
            return None

# Ejemplo de uso
# bd = Conexion()
# conexion = bd.conectar()
