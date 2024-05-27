import os
import random
import pandas as pd
import json
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS
from modelos import db, Usuario, Articulo
from vistas import VistaSignIn, VistaLogIn, VistaArticulos, VistaArticulo, vistas_bp

# Extender DOCUMENTS para incluir pdf
DOCUMENTS += ('pdf',)

# Configuración de Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['UPLOADED_FILES_DEST'] = os.path.join(os.getcwd(), 'DescargasPDFs')  # Directorio absoluto para guardar los archivos subidos

# Crear el directorio de subidas si no existe
if not os.path.exists(app.config['UPLOADED_FILES_DEST']):
    os.makedirs(app.config['UPLOADED_FILES_DEST'])

# Configuración de Flask-Uploads
files = UploadSet('files', DOCUMENTS)
configure_uploads(app, files)

# Resto de la configuración
db.init_app(app)

# Configuración de CORS
cors = CORS(app)

# Función para crear artículos desde un archivo CSV
def crear_articulos_desde_csv(ruta_csv):
    df = pd.read_csv(ruta_csv)
    
    for _, row in df.iterrows():
        nombre = row['title']
        ruta_pdf = row['pdf_path']
        
        try:
            nombre_autor = json.loads(row['authors'])[0]['name']
        except (IndexError, KeyError):
            nombre_autor = "anonymous"
        
        referencias_list = json.loads(row['references'])
        referencias = ", ".join([ref['title'] for ref in referencias_list])

        nuevo_articulo = Articulo(
            nombre=nombre,
            ruta_pdf=ruta_pdf,
            nombre_autor=nombre_autor,
            referencias=referencias
        )
        db.session.add(nuevo_articulo)

    db.session.commit()
    print("Artículos añadidos exitosamente desde el CSV.")

with app.app_context():
    db.create_all()
    if not Articulo.query.first():  # Verifica si la tabla de artículos está vacía
        crear_articulos_desde_csv('archivo_entidades.csv')  # Reemplaza 'archivo_entidades.csv' con la ruta real

api = Api(app)
jwt = JWTManager(app)

api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaArticulos, '/articulos')
api.add_resource(VistaArticulo, '/articulo', '/articulo/<int:id_articulo>')

# Registrar el blueprint para las rutas adicionales
app.register_blueprint(vistas_bp)

if __name__ == "__main__":
    app.run(debug=True)
