from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Usuario(db.Model):
    
    usuario_id = db.Column(db.Integer, primary_key=True)
    usuario_login = db.Column(db.String(20), nullable=False, unique=True)
    usuario_senha = db.Column(db.String(20), nullable=False)