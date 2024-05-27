from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), unique=True)
    contrasena = db.Column(db.String(50))

class Articulo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), unique=True)
    ruta_pdf = db.Column(db.String(256))  # Ruta al archivo PDF
    autor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=True)
    autor = db.relationship('Usuario', backref=db.backref('articulos', lazy=True))
    nombre_autor = db.Column(db.String(128), nullable=True)  # Nombre del autor, si no es un usuario registrado
    referencias = db.Column(db.String(1024), nullable=True) # Referencias, en formato CSV
    abstract = db.Column(db.String(1024), nullable=True)  
    introduction = db.Column(db.String(1024), nullable=True)
    keywords = db.Column(db.String(1024), nullable=True)
    citation_velocity = db.Column(db.String(1024), nullable=True)
    doi = db.Column(db.Integer, nullable=True)
    venue = db.Column(db.String(1024), nullable=True)
    anio = db.Column(db.Integer, nullable=True)
    oppen_access = db.Column(db.Boolean, nullable=True)
    licensed = db.Column(db.Boolean, nullable=True)
    
class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True
        exclude = ("contrasena",)

class ArticuloSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Articulo
        load_instance = True
        include_fk = True
