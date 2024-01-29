from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils.db import db
from models.usuario import Usuario

user= Blueprint('user',__name__)

@user.route('/')
def index():
    return render_template('index.html')

@user.post('/new')
def add_user():
    nombre= request.form['nombre']
    apellido= request.form['apellido']
    correo= request.form['correo']
    contraseña= request.form['contraseña']
    new_Usuario= Usuario(nombre, apellido, correo, contraseña)
    db.session.add(new_Usuario)
    db.session.commit()

    flash("Usuario creado con exito!")

    return redirect(url_for('user.index'))

