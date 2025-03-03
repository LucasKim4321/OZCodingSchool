from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 임시 사용자 데이터
users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

@app.route('/')
def index():
    return render_template('index.html', users=users)

# 사용자 추가, 수정, 삭제 라우트 및 함수 작성...
@app.route('/add', methods=['GET','POST'])
def add_user():
    #사용자 추가 뷰
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        users.append({'username':username, 'name': name})
        
        return redirect (url_for('index'))
    
    return render_template('add_user.html')

@app.route('/edit/<username>', methods=['GET','POST'])
def edit_user(username):

    # 사용자 수정 뷰
    user = next((user for user in users if user['username'] == username), None)
    if not user:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        user['name'] = request.form['name']
        return redirect(url_for('index'))
    
    return render_template('edit_user.html', user=user)

@app.route('/delete/<username>')
def delete_user(username):
    global users
    users = [user for user in users if user['username'] != username]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)


### 요구 사항

# 1. **Flask 애플리케이션 및 라우트 설정**:
#     - 사용자 목록을 표시하는 라우트를 포함하여, 사용자 추가(**`'/add'`**), 수정(**`'/edit/<username>'`**), 삭제(**`'/delete/<username>'`**) 기능을 수행하는 라우트를 설정합니다.
#     - 사용자 데이터는 메모리 내에서 관리하거나 임시 데이터베이스를 사용합니다.
# 2. **Jinja 템플릿 작성 및 웹 페이지 디자인**:
#     - 사용자 목록, 추가, 수정, 삭제 기능을 위한 HTML 템플릿을 작성합니다.
#     - 사용자 추가 및 수정을 위한 폼을 포함합니다.
#     - 각 사용자에 대해 수정 및 삭제 옵션을 제공합니다.
# 3. **폼 데이터 처리 및 서버 측 로직 구현**:
#     - 사용자 추가 및 수정에 대한 폼 데이터를 처리하는 서버 측 로직을 구현합니다.
#     - 사용자 데이터의 유효성을 검증하고, 오류가 있을 경우 적절한 피드백을 제공합니다.
# 4. **애플리케이션 실행 및 테스트**:
#     - Flask 애플리케이션을 실행하고, 사용자 추가, 수정, 삭제 기능을 포함한 전체적인 기능을 테스트합니다.