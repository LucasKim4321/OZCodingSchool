from flask import Flask, render_template
from flask_jwt_extended import JWTManager   # pip3 install flask-jwt-extended
from jwt_utils import configure_jwt
from routes.user import user_bp

app = Flask(__name__)

configure_jwt(app)

app.register_blueprint(user_bp, url_prefix='/user')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


# JWT-Extended는
# Flask라는 파이썬 웹 프레임워크에서 JWT(JSON Web Token)를 쉽게 사용할 수 있게 해주는 확장 라이브러리입니다.

# JWT (JSON Web Token) 🪙
# JWT는 사용자 인증을 위해 주로 사용되는 토큰입니다. 클라이언트(예: 웹 브라우저)가 서버에 로그인할 때, 서버는 클라이언트에게 JWT를 발급합니다. 이후 클라이언트는 이 JWT를 사용해 서버에 인증을 요청할 수 있습니다. 서버는 JWT를 검증해서 요청이 유효한 사용자인지 확인합니다.

# JWT-Extended의 주요 기능 🤓
#  간편한 JWT 생성 및 검증 : JWT를 쉽게 생성하고 검증할 수 있습니다. 로그인 시 토큰을 발급하고, 요청이 들어올 때마다 토큰을 검증하는 작업을 간단하게 할 수 있습니다.
#  액세스 토큰과 리프레시 토큰 : JWT-Extended는 짧은 유효기간을 가진 액세스 토큰과, 액세스 토큰을 재발급하기 위한 리프레시 토큰을 쉽게 사용할 수 있게 도와줍니다. 이를 통해 보안을 강화할 수 있습니다.
#  사용자 권한 관리 : JWT 안에 사용자 권한 정보를 넣어서, 특정 권한이 있는 사용자만 접근할 수 있는 API를 쉽게 만들 수 있습니다.
#  JWT 블랙리스트 : 토큰이 만료되기 전에 강제로 무효화(로그아웃 등)할 수 있게 블랙리스트 기능을 제공합니다.