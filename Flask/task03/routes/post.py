from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models.posts import Post

post_blp = Blueprint('Posts', __name__, description='Operations on posts', url_prefix='/post')

# API List
# /post

# 전체 게시글 불러오기 (GET)
# 게시글 작성(POST)
@post_blp.route('/')
class PostList(MethodView):

    def get(self):
        posts = Post.query.all()  #  model을 통해 post테이블 데이터를 불러옴
        print(posts)

        # for post in posts:
        #     print('id', post.id)
        #     print('title', post.title)
        #     print('content', post.content)
        #     print('user_id', post.user_id)
        #     print('author', post.author)  # User가 나옴

        return jsonify([{'id':post.id,
                         'title':post.title, 
                         'content':post.content, 
                         'user_id':post.author.id,
                         'author_name':post.author.name,
                         'author_email': post.author.email
                         } for post in posts])

    def post(self):

        data = request.json  # 유저가 보낸 정보를 json데이터로 받음

        new_post = Post(title=data['title'], content=data['content'], user_id=data['user_id'])
        print(new_post)

        db.session.add(new_post) # 추가할 게시글 추가
        db.session.commit() # 커밋

        return jsonify({'msg': 'success create post'}), 201

# /post/<int: post_id>
# 하나의 게시글 불러오기(GET)
# 특정 게시글 수정하기(PUT)
# 특정 게시글 삭제하기(DELETE)
@post_blp.route("/<int:post_id>")
class PostResource(MethodView):
    def get(self, post_id):
        post = Post.query.get_or_404(post_id)  # 특정한 게시글 정보를 불러옴

        return jsonify({'id': post.id, 
                        'title': post.title, 
                        'content': post.content,
                        'author_name': post.author.name})

    def put(self, post_id):
        post = Post.query.get_or_404(post_id)  
        data = request.json

        post.title = data['title']
        post.content = data['content']

        db.session.commit()

        return jsonify({'msg':'Successfully updated post data'}), 201

    def delete(self, post_id):
        post = Post.query.get_or_404(post_id)

        db.session.delete(post)
        db.session.commit()

        return jsonify({'msg':'Successfully deleted post data'}), 201