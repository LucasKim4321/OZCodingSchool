from flask import Flask
from flask_smorest import Api
from api import book_blp  # Book 관련 API를 담은 Blueprint 모듈을 임포트

app = Flask(__name__)  # Flask 애플리케이션 인스턴스 생성

# API 및 OpenAPI(Swagger) 관련 설정
app.config['API_TITLE'] = 'Book API'             # API 문서의 제목 설정
app.config['API_VERSION'] = 'v1'                   # API 버전 설정
app.config['OPENAPI_VERSION'] = '3.0.2'            # 사용할 OpenAPI의 버전 설정
app.config["OPENAPI_URL_PREFIX"] = "/"             # OpenAPI 문서가 위치할 URL 접두사 설정
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"  # Swagger UI가 제공될 경로 설정
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  # Swagger UI 정적 자원의 URL 설정

# Flask 애플리케이션에 API 확장을 적용
api = Api(app)

# Blueprint(여기서는 book_blp)를 등록하여, API 엔드포인트를 애플리케이션에 추가
api.register_blueprint(book_blp)

if __name__ == '__main__':
    # 디버그 모드로 Flask 개발 서버 실행
    app.run(debug=True)
