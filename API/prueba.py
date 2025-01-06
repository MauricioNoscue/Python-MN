
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import psycopg2
import conexion

app = Flask(__name__)
CORS(app) 

@app.route('/enviar-datos', methods=['POST'])
def recibir_datos():
    datos = request.json 
    nombre = datos['nombre']
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nombre}')
    
    if response.status_code == 200:
        data = response.json()
        uno = data["name"]
        return jsonify({"mensaje": "el pokemon que tienes es ", "datos": uno})
    else:
        print(f"Error: {response.status_code}")
        return jsonify({"mensaje": "mensaje enviado pero pokemon no encontrado"})
    
    

if __name__ == "__main__":
    app.run(debug=True)



# cd = conexion.Conexion()
#         mostrar = cd.conectar()
#         # print(mostrar)