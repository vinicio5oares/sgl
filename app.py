from flask import Flask
from models import db
from config import Config
from controller import produto_bp

#def criar_app():
    
app = Flask(__name__)
    
app.config.from_object(Config)
    
db.init_app(app)
    
with app.app_context():
    db.create_all()
        
    
app.run()

#if __name__ == '__main__':
    #app = criar_app()