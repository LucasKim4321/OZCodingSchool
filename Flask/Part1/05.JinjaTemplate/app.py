from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        'title':'Flask Jinja Template',
        'user':'taejin',
        'is_admin':True,
        'item_list':["Item1","Item2","Item3"]  # 이름을 items로 하면 딕셔너리의 메서드랑 겹쳐서 오류남
    }

    # (1) 렌더링 할 html 파일명 입력
    # (2) html로 넘겨줄 데이터 입력
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)  # 디버그 모드 활성화. 파일이 수정되면 서버에 바로 적용됨