from flask import Flask
from flask_smorest import Api
from db import db  # db = SQLAlchemy()
from models import User, Board  # models를 불러와야 테이블이 생성됨
from flask_migrate import Migrate # 데이터베이스 마이그레이션 관리 모듈

# flask_migrate
# Alembic을 통해 SQLAlchemy 모델의 변경사항을 추적
# 데이터베이스 마이그레이션을 관리하는 모듈.
# pip3 install Flask-Migrate 설치.
# 터미널에서 프로젝트 경로에 flask db migrate 실행

# 모델에 변경사항이 있을때마다 새로운 마이그레이션 생성해야함
# flask db migrate  마이그레이션 생성
# flask db migrate -m "message"
# flask db upgrade  생성된 마이그레이션 적용. 업그레이드
# flask db downgrade 이전 마이그레이션 상태로. 다운그레이드


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/oz'  # DB유형+DB드라이버://아이디:비밀번호@접속경로/DB명
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 객체가 바뀔때마다 추적할지 설정

db.init_app(app)
migrate = Migrate(app, db)  # Flask애플리케이션 및 SQLAlchemy 데이터베이스를 Migrate객체에 담음.

# blueprint 설정
# API 및 OpenAPI(Swagger) 관련 설정
app.config['API_TITLE'] = 'Book API'             # API 문서의 제목 설정
app.config['API_VERSION'] = 'v1'                   # API 버전 설정
app.config['OPENAPI_VERSION'] = '3.0.2'            # 사용할 OpenAPI의 버전 설정
app.config["OPENAPI_URL_PREFIX"] = "/"             # OpenAPI 문서가 위치할 URL 접두사 설정
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"  # Swagger UI가 제공될 경로 설정
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # Swagger UI 정적 자원의 URL 설정


# Flask 애플리케이션에 API 확장을 적용
api = Api(app)

from routes.board import board_blp
from routes.user import user_blp

api.register_blueprint(board_blp)
api.register_blueprint(user_blp)

from flask import render_template

# 게시판
@app.route('/manage-boards')
def manage_boards():
    return render_template('boards.html')

# 유저
@app.route('/manage-users')
def manage_users():
    return render_template('users.html')

if __name__ == '__main__':
    # 모델을 만들었을 때 db연결도 하고 테이블 생성도 해주고 함.
    with app.app_context():
        db.create_all()

    app.run(debug=True)