from flask import Blueprint, request, jsonify
from models import db, pedido, Produto, detalhe_do_pedido

detalhePedido_bp = Blueprint('detalhepedidos', __name__)

@detalhePedido_bp.route('/detalhepedidos', methods=['POST'])
def criar_detalhe_pedidos():

    detalhe_do_pedido = request.json

    novo_detalhe_pedido = detalhe_do_pedido(dp_quantidade=detalhe_do_pedido['dp_quantidade'],
                                        dp_preco=detalhe_do_pedido['dp_preco'],
                                        dp_desconto=detalhe_do_pedido['dp_desconto'],
                                        dp_pedido_id=detalhe_do_pedido['dp_pedido_id'],
                                        dp_produto_id=detalhe_do_pedido['dp_produto_id'])
    
    db.session.add(novo_detalhe_pedido)
    db.session.commit()

    return jsonify({'id': novo_detalhe_pedido.dp_id})