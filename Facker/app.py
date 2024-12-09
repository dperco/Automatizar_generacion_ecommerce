from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# Configuración de la conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Cambia la URL si usas MongoDB 
db = client['prueba_mongodb']  # Nombre de la base de datos
collection = db['products']  # Nombre de la colección
print ('Conexión a MongoDB establecida correctamente.')
# Ruta a la carpeta de imágenes
images_folder_path = 'images/'

@app.route('/')
def index():
    products = list(collection.find())
    return render_template('index.html', products=products)

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory(images_folder_path, filename)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.form['name']
        price = float(request.form['price'])
        category = request.form['category']
        year = int(request.form['year'])
        stock = int(request.form['stock'])
        imgFrontUrl = request.form['imgFrontUrl']
        imgBackUrl = request.form['imgBackUrl']

        # Crear un nuevo producto
        new_product = {
            'name': name,
            'price': price,
            'category': category,
            'year': year,
            'stock': stock,
            'imgFrontUrl': imgFrontUrl,
            'imgBackUrl': imgBackUrl
        }

        # Insertar el nuevo producto en la colección de MongoDB
        collection.insert_one(new_product)

        return redirect(url_for('index'))

    return render_template('add_product.html')

@app.route('/edit_product/<id>', methods=['GET', 'POST'])
def edit_product(id):
    product = collection.find_one({'_id': ObjectId(id)})

    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.form['name']
        price = float(request.form['price'])
        category = request.form['category']
        year = int(request.form['year'])
        stock = int(request.form['stock'])
        imgFrontUrl = request.form['imgFrontUrl']
        imgBackUrl = request.form['imgBackUrl']

        # Actualizar el producto
        updated_product = {
            'name': name,
            'price': price,
            'category': category,
            'year': year,
            'stock': stock,
            'imgFrontUrl': imgFrontUrl,
            'imgBackUrl': imgBackUrl
        }

        # Actualizar el producto en la colección de MongoDB
        collection.update_one({'_id': ObjectId(id)}, {'$set': updated_product})

        return redirect(url_for('index'))

    return render_template('edit_product.html', product=product)

@app.route('/delete_product/<id>', methods=['POST'])
def delete_product(id):
    # Eliminar el producto de la colección de MongoDB
    collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)