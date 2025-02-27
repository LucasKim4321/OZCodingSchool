from flask import request, jsonify
from flask_smorest import Blueprint, abort

# API CRUD (create(post) read(get) update(put) delete(delete))

def create_posts_blueprint(mysql):
    posts_blp = Blueprint("posts", __name__, description="posts api", url_prefix="/posts")

    @posts_blp.route('/', methods=['GET','POST'])
    def posts():

        cursor = mysql.connection.cursor()

        # 게시글 조회
        if request.method == 'GET':
            sql = "SELECT * FROM posts"
            cursor.execute(sql)

            posts = cursor.fetchall()
            cursor.close()

            post_list = []

            for post in posts:
                post_list.append({
                    'id' : post[0],
                    'title' : post[1],
                    'content': post[2]
                })

            return jsonify(post_list)
        
        # 게시글 생성 
        elif request.method == 'POST':
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, message="Title or Content cannot be empty")

            # sql = "INSERT INTO posts (title, content, created_at) VALUES (%s, %s, NOW())"
            sql = 'INSERT INTO posts(title, content) VALUES (%s, %s)'
            cursor.execute(sql, (title, content))
            mysql.connection.commit()

            return jsonify({'msg':'successfully created post data', 'title':title, 'content':content}),201
            # return jsonify({'msg':'successfully created post data'}),201
    
    # 1번 게시글만 조회하고 싶은 경우
    # 게시글 수정 및 삭제

    @posts_blp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def post(id):
        cursor = mysql.connection.cursor()
        sql = f"SELECT * FROM posts WHERE id = {id}"
        cursor.execute(sql)
        post = cursor.fetchone()

        # 존재하지 않는 id값을 받으면 에러
        if not post:
            abort(404, "Not found post")

        if request.method == 'GET':
            # sql = f'SELECT * FROM posts WHERE id = {id}'
            # cursor.execute(sql)
            # post = cursor.fetchone()

            # data가 없으면 에러 표시
            # if not post:
            #     abort(404, "Not found post")

            return ({'id':post[0], 'title':post[1], 'content':post[2]})
        

        elif request.method == 'PUT':
            # data = request.json
            # title = data['title']

            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(400, "Not found title, content")

            # sql인젝션에 취약하다고 함 title값을 바꾸면 쿼리문이 바뀜.
            sql = f"UPDATE posts SET title='{title}', content='{content}' WHERE id={id}"
            
            # -- sql인젝션 예시.
            # 입력폼에서 이런 데이터를 받으면 의도와 다르게 실행됨
            # -- title = "Hacked', 'Malicious Code'); DROP TABLE posts; --"
            # -- content = "Safe Content"
            # INSERT INTO posts (title, content) VALUES ('Hacked', 'Malicious Code'); DROP TABLE posts; --', 'Safe Content');
            
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({'msg':'Successfully updated title & content'})

        elif request.method == 'DELETE':

            sql = f'DELETE FROM posts WHERE id={id}'
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({'msg':'Successfully deleted post'})
    
    # Blueprint 리턴
    return posts_blp