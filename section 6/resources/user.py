import sqlite3
from flask_restful import Resource, representations, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field ca not be left blank")
    parser.add_argument('password', type=str, required=True, help="This field ca not be left blank")
    def post(self):
        data=UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']) is not None:
            return {'message': 'An user with that username already exists'}, 400
        user=UserModel(**data)
        user.save_to_db()

        return {'message': 'the user has been created successfully'}, 201