from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        'title':"Kim's Garden :b",
        'user':'taejin',
        'is_admin':True,
        'item_list':["Item1","Item2","Item3"]  # 이름을 items로 하면 딕셔너리의 메서드랑 겹쳐서 오류남
    }

    return render_template("index.html", data=data)

@app.route("/users")
def users():
    users = [
        {"username": "traveler", "name":"Alex", "age":"33"},
        {"username": "photographer", "name":"Sam", "age":"28"},
        {"username": "gourmet", "name":"Chris", "age":"24"}
    ]

    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)