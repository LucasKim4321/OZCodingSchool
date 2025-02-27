from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models.users import User

user_blp = Blueprint("Users", __name__, description="Operations on users", url_prefix="/user")

# API LIST:
# (1) 전체 유저 데이터 조회 (GET)
# (2) 유저 생성 (POST)

@user_blp.route('/')
class UserList(MethodView):

    # 모든 유저 조회
    def get(self):
        users = User.query.all()

        user_data = [{
            'id':user.id,
            'name':user.name,
            'email':user.email
        } for user in users ]
        
        return jsonify(user_data)

    # 유저 생성
    def post(self):
        data = request.json

        new_user = User(name=data['name'], email=data['email'])

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'msg':'Successfully created new user'}), 201

# (1) 특정 유저 데이터 조회 (GET)
# (2) 특정 유저 데이터 업데이트 (PUT)
# (3) 특정 유저 삭제 (DELETE)

@user_blp.route("/<int:user_id>")
class UserResource(MethodView):

    # 유저 조회
    def get(self, user_id):
        user = User.query.get_or_404(user_id)  # QuerySet
        # print(type(user))

        return jsonify({'name':user.name, 'email':user.email})

    # 유저 수정
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.json

        user.name = data['name']
        user.email = data['email']

        db.session.commit()

        return jsonify({'msg': 'Sucessfully updated user'}), 201

    # 유저 삭제. 외래키로 묶여있는 유저는 삭제 안됨
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)

        db.session.delete(user)
        db.session.commit()

        return jsonify({'msg': 'Sucessfully deleted user'}), 201
    

    