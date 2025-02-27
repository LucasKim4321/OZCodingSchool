from flask import Flask,render_template, jsonify
from flask_httpauth import HTTPBasicAuth  #pip3 install flask-httpauth

app = Flask(__name__)
auth = HTTPBasicAuth()


users = {
    'admin':'secret',
    'guest':'pw123'
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/protected")
@auth.login_required  # 로그인한 사용자만 접근 가능하게 설정  # 로그인이 안되어 있으면 로그인 창을 띄움
def protected():
    return render_template("secret.html")


# 로그아웃 구현 (401 반환하여 브라우저 인증 정보 삭제 시도)(401(Unauthorized) : 클라이언트가 인증되지 않았거나, 유효한 인증 정보가 부족하여 요청이 거부되었음을 의미)
# flask_httpauth의 HTTPBasicAuth는 세션을 사용하지 않고 브라우저 캐시에 인증정보를 저장함
@app.route('/logout')
def logout():
    return jsonify({"msg":"logged out"}), 401  # (unauthorized)

if __name__ == "__main__":
    app.run(debug=True)

