# app.py

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, This is Kim's gardon"

@app.route('/about')
def about():
    return "This is about Kim's gardon"

# 동적으로 URL 파라미터 값을 받아서 처리해준다.
@app.route('/user/<username>')
def user_profile(username):
    return f"UserName : {username}"

@app.route('/number/<int:number>')
def number_test(number):
    return f"Number : {number}"

# post 요청 하는법
# (1) postman
# (2) requests
# ...

import requests  # pip3 install requests
@app.route('/test')
def test():
    url = 'http://127.0.0.1:5000/submit'
    data = 'test data'
    # response = requests.post(url=url)
    response = requests.post(url=url, data=data)

    return response.text

@app.route('/submit', methods=['GET','POST','PUT','DELETE'])
def submit():
    print(request.method)
    
    if request.method == 'GET':
        print("GET method")
    
    if request.method == 'POST':
        print("*** POST method ***", request.data)

    return Response("SucessFully subimtted", status=200)

# host='127.0.0.1'는 로컬에서만 접근 가능합니다. 다른 기기(외부 IP)에서 접속하려면 host='0.0.0.0'로 설정하세요.
# host = '127.0.0.1'
# port = '8000'

# __name__은 현재 실행 환경에선 __main__ 이고 모듈로 불려오면 파일이름이 표기된다.
if __name__ == "__main__":
    print("__name__ : ", __name__)
    app.run(debug=True)  # 디버그 모드 활성화. 파일이 수정되면 서버에 바로 적용됨
    # app.run(debug=True, host=host, port=port)
    
