from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 커맨드 시프트 p
# Python: Select Interpreter