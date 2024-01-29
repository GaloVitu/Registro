from utils.db import db

class Usuario(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(100))
    apellido= db.Column(db.String(100))
    correo= db.Column(db.String(100))
    contraseña= db.Column(db.String(100))


    def __init__(self, nombre, apellido, correo, contraseña):
        self.nombre= nombre
        self.apellido= apellido
        self.correo= correo
        self.contraseña= contraseña
       