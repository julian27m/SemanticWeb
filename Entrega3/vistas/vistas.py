from flask import request, send_file, Blueprint, current_app
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_uploads import UploadNotAllowed
import os
import hashlib

from modelos import db, Usuario, UsuarioSchema, Articulo, ArticuloSchema

usuario_schema = UsuarioSchema()
articulo_schema = ArticuloSchema()

vistas_bp = Blueprint('vistas', __name__)

class VistaSignIn(Resource):
    def post(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"]).first()
        if usuario is None:
            contrasena_encriptada = hashlib.md5(request.json["contrasena"].encode('utf-8')).hexdigest()
            nuevo_usuario = Usuario(usuario=request.json["usuario"], contrasena=contrasena_encriptada)
            db.session.add(nuevo_usuario)
            db.session.commit()
            token_de_acceso = create_access_token(identity=nuevo_usuario.id)
            return {"mensaje": "usuario creado exitosamente", "id": nuevo_usuario.id, "token": token_de_acceso}
        else:
            return {"mensaje": "El usuario ya existe"}, 404

class VistaLogIn(Resource):
    def post(self):
        contrasena_encriptada = hashlib.md5(request.json["contrasena"].encode('utf-8')).hexdigest()
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == contrasena_encriptada).first()
        if usuario is None:
            return {"mensaje": "El usuario no existe"}, 404
        else:
            token_de_acceso = create_access_token(identity=usuario.id)
            return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso, "id": usuario.id}

class VistaArticulos(Resource):
    @jwt_required()
    def get(self):
        articulos = Articulo.query.all()
        return [articulo_schema.dump(articulo) for articulo in articulos]

    @jwt_required()
    def post(self):
        archivo = request.files.get("archivo")

        if not archivo:
            return {"mensaje": "No se subió ningún archivo"}, 400

        if archivo.filename.split('.')[-1].lower() != 'pdf':
            return {"mensaje": "El archivo debe ser un PDF"}, 400

        # Añadir mensajes de registro para depuración
        print("Nombre del archivo:", archivo.filename)
        print("Tipo MIME del archivo:", archivo.mimetype)

        try:
            ruta = app.files.save(archivo)
        except UploadNotAllowed:
            return {"mensaje": "No se pudo guardar el archivo. Verifique que es un PDF válido."}, 400

        ruta_completa = os.path.join(current_app.config['UPLOADED_FILES_DEST'], ruta)

        nuevo_articulo = Articulo(
            nombre=archivo.filename,
            ruta_pdf=ruta_completa
        )
        db.session.add(nuevo_articulo)
        db.session.commit()
        return articulo_schema.dump(nuevo_articulo), 201

class VistaArticulo(Resource):
    @jwt_required()
    def get(self, id_articulo):
        articulo = Articulo.query.get_or_404(id_articulo)
        return articulo_schema.dump(articulo)

    @jwt_required()
    def delete(self, id_articulo):
        articulo = Articulo.query.get_or_404(id_articulo)
        db.session.delete(articulo)
        db.session.commit()
        return '', 204

# Ruta para descargar archivos PDF
@vistas_bp.route('/descargar/<path:filename>', methods=['GET'])
def download_file(filename):
    base_directory = os.path.join(current_app.root_path, 'DescargasPDFs')
    file_path = os.path.join(base_directory, filename)
    return send_file(file_path, as_attachment=True)
