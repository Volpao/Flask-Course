import os
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.store import Store, StoreList
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASEURL", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.secret_key = 'fokifoki'
api = Api(app)
jwt = JWT(app, authenticate, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
if __name__=='__main__':
    from db import db
    db.init_app(app)
    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()
            
    app.run(port=5000, debug=True)
