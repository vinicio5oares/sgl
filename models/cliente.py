from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class Cliente(db.Model):
  
    __tablename__ = 'clientes'

    cliente_id = db.Column(db.Integer, primary_key=True)
    cliente_nome = db.Column(db.String)
    cliente_email = db.Column(db.String)