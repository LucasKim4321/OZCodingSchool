from flask import Flask, request
from flask_restful import Api
from resources.item import Item


app = Flask(__name__)

api = Api(app)

api.add_resource(Item, '/item/<string:name>') # 경로 추가

if __name__ == "__main__":
    app.run(debug=True)



# 상대 임포트 (from .resources.item import Item)

# 의미:
# 점(.)은 현재 모듈이 속한 패키지를 기준으로 하여 임포트하라는 의미입니다.

# 전제 조건:
# 상대 임포트가 제대로 작동하려면,
# app.py가 패키지의 일부여야 하며
# 모듈이 패키지 컨텍스트 내에서 실행되어야 합니다.


# 절대 임포트 (from resources.item import Item)

# 의미:
# 이는 현재 PYTHONPATH(또는 현재 작업 디렉토리)를 기준으로 전체 경로에서 모듈을 찾으라는 의미입니다.

# 동작 방식:
# 작업 디렉토리가 flask라고 하더라도,
# 만약 app.py가 실제로 실행되는 위치가 flask/part2/03.restfulapi라면,
# 그리고 그 위치에 resources 폴더가 있다면,
# Python은 resources 폴더를 최상위 모듈처럼 인식하여 올바르게 Item 모듈을 찾게 됩니다.

# 안된 이유
# app.py를 단독 스크립트(즉, __name__이 "__main__"인 상태)로 실행하면,
# Python은 이 모듈이 어떤 패키지에 속해 있는지 알 수 없기 때문에
# 상대 임포트를 처리할 수 없습니다.