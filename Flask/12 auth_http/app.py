from flask import Flask,render_template, jsonify
from flask_httpauth import HTTPBasicAuth  #pip3 install flask-httpauth

app = Flask(__name__)
auth = HTTPBasicAuth()

# 사용자 정보
users = {
    'admin':'secret',
    'guest':'pw123'
}

# @auth.verify_password(사용자 인증)
# 사용자 이름과 비밀번호가 유효한지 확인하는 함수를 정의합니다.
# 여기서는 간단한 사전 users를 사용하여 사용자 이름과 비밀번호를 확인합니다.
# 실전 환경에서는 데이터베이스 또는 다른 안전한 저장소를 사용해야합니다.
@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    
@app.route('/')
def index():
    return render_template("index.html")

# @auth.login_required (라우트 보호)
# 인증된 사용자만 해당 라우트로 접근할 수 있도록하는 목적. 사용자 인증을 요구.
@app.route("/protected")
@auth.login_required  # 로그인한 사용자만 접근 가능하게 설정  # 로그인이 안되어 있으면 로그인 창을 띄움
def protected():
    return render_template("secret.html")

# @auth.error_handler`** (오류 핸들링)
# 인증에 실패했을 때의 동작을 정의

# 로그아웃 구현 (401 반환하여 브라우저 인증 정보 삭제 시도)(401(Unauthorized) : 클라이언트가 인증되지 않았거나, 유효한 인증 정보가 부족하여 요청이 거부되었음을 의미)
# flask_httpauth의 HTTPBasicAuth는 세션을 사용하지 않고 브라우저 캐시에 인증정보를 저장함
@app.route('/logout')
def logout():
    return jsonify({"msg":"logged out"}), 401  # (unauthorized)

if __name__ == "__main__":
    app.run(debug=True)


# 보안을 강화하기 위해서는 HTTPS를 사용하는 것이 좋으며, 실제 프로덕션 환경에서는 더 견고한 인증 방식(예: OAuth, JWT)을 사용하는 것이 권장됨.