from flask import Flask, render_template, request, redirect, session, flash
from datetime import timedelta

app = Flask(__name__)

app.secret_key = 'flask-secret-key' # 실제로 배포시에는 .env or yaml 파일로 만들어 관리하고 깃에는 업로드 하지 않는다.
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  #유지시간 설정

# admin user
users = {
    'john':'pw123',
    'leo':'pw123'
}

@app.route('/')
def index():
    return render_template("login.html")
 
# 사용자가 login.html 폼을 통해 로그인 정보를 제출하면, login 뷰에서 이를 검증
# 검증이 성공하면, 사용자 이름을 세션에 저장하고 비밀 페이지로 리디렉션
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        session['username'] = username
        session.permanent = True #유지시간 적용
    
        return redirect('/secret')
    else:
        flash("Invalid username or password")
        return redirect("/")

# 인증된 사용자 페이지
# secret 뷰에서는 사용자가 로그인되어 있는지 세션을 통해 확인하고, 
# 로그인되지 않은 사용자는 로그인 페이지로 리디렉션합니다.
@app.route('/secret')
def secret():
    if 'username' in session:  # 로그인 했으면
        return render_template("secret.html")
    else:
        return redirect("/")
    
# 사용자가 로그아웃 링크를 클릭하면, 
# logout 뷰에서 세션에서 사용자 정보를 제거하고 초기 페이지로 리디렉션
@app.route("/logout")
def logout():
    session.pop('username',None)
    session.clear()  # 세션의 모든 데이터 제거
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)