from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS

from modelos import db, Usuario, Articulo
from vistas import VistaSignIn, VistaLogIn, VistaArticulos, VistaArticulo, vistas_bp

import os

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

with app.app_context():
    db.create_all()
    if not Articulo.query.first():  # Verifica si la tabla de artículos está vacía
        articulos = [
            {"nombre": "One size fits all” database architectures do not work for DSS", "ruta_pdf": "DescargasPDFs/“One size fits all” database architectures do not work for DSS.pdf", "nombre_autor": "Clark D. French"},
            {"nombre": "ÆMPA: A Process Algebraic Description Language for thePerformance Analysis of Software Architectures", "ruta_pdf": "DescargasPDFs/ÆMPA_ a process algebraic description language for the performance analysis of software architectures.pdf", "nombre_autor": "Marco Bernardo"},
            {"nombre": "YFilter: Efficient and Scalable Filtering of XML Documents", "ruta_pdf": "DescargasPDFs/YFilter_ efficient and scalable filtering of XML documents.pdf", "nombre_autor": "Yanlei Diao"},
            {"nombre": "Z3: An Efficient SMT Solver", "ruta_pdf": "DescargasPDFs/Z3_ An Efficient SMT Solver.pdf", "nombre_autor": "Leonardo de Moura"},
            {"nombre": "ZCS: A Zeroth Level Classifier System", "ruta_pdf": "DescargasPDFs/ZCS_ A Zeroth Level Classifier System.pdf", "nombre_autor": "Stewart W. Wilson"},
            {"nombre": "A practical approach for 'zero' downtime in an operational information system", "ruta_pdf": "DescargasPDFs/A practical approach for 'zero' downtime in an operational information system.pdf", "nombre_autor": "John Doe"},
            {"nombre": "Agent-Mediated Electronic Commerce", "ruta_pdf": "DescargasPDFs/Agent-Mediated Electronic Commerce.pdf", "nombre_autor": "Jane Smith"},
            {"nombre": "An Expedited Forwarding PHB", "ruta_pdf": "DescargasPDFs/An Expedited Forwarding PHB.pdf", "nombre_autor": "Alice Johnson"},
            {"nombre": "Assured Forwarding PHB Group", "ruta_pdf": "DescargasPDFs/Assured Forwarding PHB Group.pdf", "nombre_autor": "Bob Brown"},
            {"nombre": "Automatic", "ruta_pdf": "DescargasPDFs/Automatic.pdf", "nombre_autor": "Charlie Davis"},
            {"nombre": "BGP Extended Communities Attribute", "ruta_pdf": "DescargasPDFs/BGP Extended Communities Attribute.pdf", "nombre_autor": "David Evans"},
            {"nombre": "Clarifying when Standards Track Documents may Refer Normatively to Documents at a Lower Level", "ruta_pdf": "DescargasPDFs/Clarifying when Standards Track Documents may Refer Normatively to Documents at a Lower Level.pdf", "nombre_autor": "Eve Foster"},
            {"nombre": "Computing TCP's Retransmission Timer", "ruta_pdf": "DescargasPDFs/Computing TCP's Retransmission Timer.pdf", "nombre_autor": "Frank Green"},
            {"nombre": "Massachusetts", "ruta_pdf": "DescargasPDFs/Massachusetts.pdf", "nombre_autor": "George Harris"},
            {"nombre": "One-way Loss Pattern Sample Metrics", "ruta_pdf": "DescargasPDFs/One-way Loss Pattern Sample Metrics.pdf", "nombre_autor": "Hannah Clark"},
            {"nombre": "RTP Payload Format for H.263 Video Streams", "ruta_pdf": "DescargasPDFs/RTP Payload Format for H.263 Video Streams.pdf", "nombre_autor": "Ivy Johnson"},
            {"nombre": "RTP Payload Format for JPEG-compressed Video", "ruta_pdf": "DescargasPDFs/RTP Payload Format for JPEG-compressed Video.pdf", "nombre_autor": "Jack Kelly"},
            {"nombre": "Seamless Image Stitching in the Gradient Domain", "ruta_pdf": "DescargasPDFs/Seamless Image Stitching in the Gradient Domain.pdf", "nombre_autor": "Karen Lee"},
            {"nombre": "Temporal Constraints: A Survey", "ruta_pdf": "DescargasPDFs/Temporal Constraints_ A Survey.pdf", "nombre_autor": "Leo Martinez"},
            {"nombre": "Terminology for Forwarding Information Base (FIB) based Router Performance", "ruta_pdf": "DescargasPDFs/Terminology for Forwarding Information Base (FIB) based Router Performance.pdf", "nombre_autor": "Mia Nelson"}
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

# Registrar el blueprint para las rutas adicionales
app.register_blueprint(vistas_bp)

if __name__ == "__main__":
    app.run(debug=True)
