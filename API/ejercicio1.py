
from flask import Flask, request, jsonify
import requests



nombre = input("ingrese el nombre del pokemon: ")

response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{nombre}')
if response.status_code == 200:
    data = response.json()
    uno = data["name"]
    print(uno)
else:
    print(f"Error: {response.status_code}")



