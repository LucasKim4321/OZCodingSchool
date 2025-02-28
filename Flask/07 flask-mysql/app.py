from flask import Flask
from flask_mysqldb import MySQL
from flask_smorest import Api
from user_routes import create_user_blueprint

app = Flask(__name__)

# MYSQL 연동 설정
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'oz'

mysql = MySQL(app)

# Blueprint 설정 및 등록
# API 및 OpenAPI(Swagger) 관련 설정
app.config['API_TITLE'] = 'Book API'             # API 문서의 제목 설정
app.config['API_VERSION'] = 'v1'                   # API 버전 설정
app.config['OPENAPI_VERSION'] = '3.0.2'            # 사용할 OpenAPI의 버전 설정
app.config["OPENAPI_URL_PREFIX"] = "/"             # OpenAPI 문서가 위치할 URL 접두사 설정
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"  # Swagger UI가 제공될 경로 설정
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # Swagger UI 정적 자원의 URL 설정

# Flask 애플리케이션에 API 확장을 적용
api = Api(app)

user_blp = create_user_blueprint(mysql)
api.register_blueprint(user_blp)

# html 코드로 flaski-mysql 테스트
from flask import render_template
@app.route('/users_interface')
def user_interface():
    return render_template("users.html")


if __name__ == '__main__':
    # 디버그 모드로 Flask 개발 서버 실행
    app.run(debug=True)
