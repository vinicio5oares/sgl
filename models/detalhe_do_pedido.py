from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class detalhePdito(db.Model):
    
    __tablename__ = 'detalhepedidos'

    dp_id = db.Column(db.Integer, primary_key=True)
    dp_quantidade = db.Column(db.Integer)
    dp_preco = db.Column(db.Numeric)
    dp_desconto = db.Column(db.Numeric)


    dp_pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.pedido_id'), nullable=False)
    dp_produto_id = db.Column(db.Integer, db.ForeignKey('produtos.produto_id'), nullable=False)

    pedido = db.relationship('Pedido', backref='detalhepedidos')
    produto = db.relationship('Produto', backref='detalhepedidos')
    


