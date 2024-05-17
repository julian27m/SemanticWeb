from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS

from modelos import db, Usuario, Articulo
from vistas import VistaSignIn, VistaLogIn, VistaArticulos, VistaArticulo

import os

# Extender DOCUMENTS para incluir pdf
DOCUMENTS += ('pdf',)

# Configuración de Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['UPLOADED_FILES_DEST'] = os.path.join(os.getcwd(), 'uploads')  # Directorio absoluto para guardar los archivos subidos

# Crear el directorio de subidas si no existe
if not os.path.exists(app.config['UPLOADED_FILES_DEST']):
    os.makedirs(app.config['UPLOADED_FILES_DEST'])

# Configuración de Flask-Uploads
files = UploadSet('files', DOCUMENTS)
configure_uploads(app, files)

# Resto de la configuración
db.init_app(app)

with app.app_context():
    db.create_all()
    if not Articulo.query.first():  # Verifica si la tabla de artículos está vacía
        articulos = [
            {"nombre": "One size fits all” database architectures do not work for DSS", "ruta_pdf": "uploads/“One size fits all” database architectures do not work for DSS.pdf", "nombre_autor": "Clark D. French"},
            {"nombre": "ÆMPA: A Process Algebraic Description Language for thePerformance Analysis of software architectures", "ruta_pdf": "uploads/ÆMPA_ a process algebraic description language for the performance analysis of software architectures.pdf", "nombre_autor": "Marco Bernardo"},
            {"nombre": "YFilter: Efficient and Scalable Filtering of XML Documents", "ruta_pdf": "uploads/YFilter_ efficient and scalable filtering of XML documents.pdf", "nombre_autor": "Yanlei Diao"},
            {"nombre": "Z3: An Efficient SMT Solver", "ruta_pdf": "uploads/Z3_ An Efficient SMT Solver.pdf", "nombre_autor": "Leonardo de Moura"},
            {"nombre": "ZCS: A Zeroth Level Classifier System", "ruta_pdf": "uploads/ZCS_ A Zeroth Level Classifier System.pdf", "nombre_autor": "Stewart W. Wilson"}
        ]

        for articulo_info in articulos:
            autor_id = articulo_info.get("autor_id")
            if autor_id and not Usuario.query.get(autor_id):
                autor_id = None
            
            articulo = Articulo(
                nombre=articulo_info["nombre"],
                ruta_pdf=articulo_info["ruta_pdf"],
                autor_id=autor_id,
                nombre_autor=articulo_info.get("nombre_autor", None)
            )
            db.session.add(articulo)

        db.session.commit()
        print("Artículos añadidos exitosamente.")

cors = CORS(app)
api = Api(app)
jwt = JWTManager(app)

api.add_resource(VistaSignIn, '/signin')
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaArticulos, '/articulos')
api.add_resource(VistaArticulo, '/articulo', '/articulo/<int:id_articulo>')

if __name__ == "__main__":
    app.run(debug=True)
