
# Flask Product Management Application

Esta es una aplicación web simple para gestionar productos utilizando Flask y MongoDB. La aplicación permite agregar, modificar, borrar y ver productos.

## Requisitos

- Python 3.10 o superior
- MongoDB
- pip (gestor de paquetes de Python)

## Instalación

1. Clona este repositorio o descarga los archivos.

```sh
git clone https://github.com/tu-usuario/flask-product-management.git
cd flask-product-management
Crea un entorno virtual (opcional pero recomendado).
sh
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
Instala las dependencias.
sh
pip install -r requirements.txt
Asegúrate de que MongoDB esté en funcionamiento. Si estás usando una instalación local de MongoDB, puedes iniciarla con:
sh
mongod
Configuración
Abre el archivo app.py y asegúrate de que la configuración de la conexión a MongoDB sea correcta. Si estás usando MongoDB Atlas, actualiza la URL de conexión.
python
client = MongoClient('mongodb://localhost:27017/')  # Cambia la URL si usas MongoDB Atlas u otra configuración
db = client['mi_base_de_datos']  # Nombre de la base de datos
collection = db['productos']  # Nombre de la colección
Asegúrate de que la carpeta images exista en el directorio raíz del proyecto y que contenga las imágenes necesarias para los productos.
Ejecución
Ejecuta la aplicación Flask.
sh
python app.py
Abre tu navegador y navega a http://127.0.0.1:5000/ para ver la aplicación en funcionamiento.
Estructura del Proyecto
app.py: Archivo principal de la aplicación Flask.
templates/: Carpeta que contiene las plantillas HTML.
index.html: Página principal que muestra la lista de productos.
add_product.html: Página para agregar un nuevo producto.
edit_product.html: Página para editar un producto existente.
images/: Carpeta que contiene las imágenes de los productos.
Uso
Agregar un Producto
Haz clic en "Agregar Nuevo Producto" en la página principal.
Completa el formulario con los detalles del producto y haz clic en "Agregar Producto".
Editar un Producto
En la página principal, haz clic en "Editar" junto al producto que deseas modificar.
Actualiza los detalles del producto en el formulario y haz clic en "Actualizar Producto".
Eliminar un Producto
En la página principal, haz clic en "Eliminar" junto al producto que deseas borrar.
Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para cualquier mejora o corrección.

Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.


### Notas Adicionales

1. **requirements.txt**: Asegúrate de tener un archivo `requirements.txt` con las dependencias necesarias. Puedes generarlo con el siguiente comando:

```sh
pip freeze > requirements.txt
El contenido típico de requirements.txt para este proyecto podría ser:

Flask==2.0.2
pymongo==3.12.1
Estructura de Carpetas: Asegúrate de que la estructura de carpetas sea la siguiente:
flask-product-management/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── add_product.html
│   ├── edit_product.html
└── images/

