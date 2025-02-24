# app.py

from flask import Flask
import ch09_test

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# host='127.0.0.1'는 로컬에서만 접근 가능합니다. 다른 기기(외부 IP)에서 접속하려면 host='0.0.0.0'로 설정하세요.
host = '127.0.0.1'
port = '8000'

# __name__은 현재 실행 환경에선 __main__ 이고 모듈로 불려오면 파일이름이 표기된다.
if __name__ == "__main__":
    print("__name__ : ", __name__)
    print("test.__name__ : ",ch09_test.__name__)
    # app.run()
    app.run(debug=True)  # 디버그 모드 활성화. 파일이 수정되면 서버에 바로 적용됨
    # app.run(debug=True, host=host, port=port)
    
