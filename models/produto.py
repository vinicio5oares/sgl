from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produto(db.Model):
    
    produto_id = db.Column(db.Integer, primary_key=True)
    produto_nome = db.Column(db.String, nullable=False)
    produto_preco = db.Column(db.Numeric, nullable=False)
