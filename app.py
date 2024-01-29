from flask import Flask
from routes.user import user
from flask_sqlalchemy import SQLAlchemy
from utils.db import db

app= Flask(__name__)
app.secret_key= "secret key"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/citasalud'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(user)