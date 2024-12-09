import json
from pymongo import MongoClient

# Configuración de la conexión a MongoDB
client = MongoClient('localhost', 27017)  # Conexión local
db = client['prueba_mongodb']  # Nombre de la base de datos
collection = db['products']  # Nombre de la colección

# Ruta al archivo JSON
json_file_path = 'productos.json'

# Leer el archivo JSON
with open(json_file_path, 'r', encoding='utf-8') as f:
    products = json.load(f)

# Insertar los datos en la colección de MongoDB
collection.insert_many(products)

print("Datos insertados en MongoDB correctamente.")