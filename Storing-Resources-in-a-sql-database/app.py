from flask import Flask,request
from flask_restful import Resource , Api, reqparse
from flask_jwt import JWT ,jwt_required
from security import authenticate,identity
from users import UserRegister
from item import Item,ItemsList

app = Flask(__name__)
app.secret_key = "keshav"
api = Api(app)

jwt = JWT(app, authenticate, identity)   # /auth



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(UserRegister, "/register")


if __name__ == "__main__":
    app.run(debug=True)
    