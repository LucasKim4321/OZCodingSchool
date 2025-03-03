from flask import Flask, jsonify, request

# Flask 애플리케이션 생성
app = Flask(__name__)

# 예제 데이터 정의: 기본적으로 성공 결과와 함께 두 개의 피드 데이터를 포함하는 딕셔너리
data = {
    'result': 'success',
    'data': {
        'feed1': 'data1',
        'feed2': 'data2'
    }
}

# ===========================
# GET 요청 처리
# ===========================

# (1) 전체 게시글을 불러오는 API
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():
    # 전체 데이터를 반환합니다.
    # Flask는 반환된 딕셔너리를 JSON 형태로 자동 변환하여 응답합니다.
    return data
    # 만약 반환 값이 딕셔너리가 아닐 경우, jsonify()를 사용해야 합니다.
    # return jsonify(data)

# (2) 특정 게시글을 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    # URL 경로에서 정수형 feed_id를 받아옵니다.
    # 디버깅을 위해 feed_id 값을 출력합니다.
    print(feed_id)
    
    # 실제로는 feed_id에 해당하는 특정 피드를 찾아 반환해야 합니다.
    # 현재는 예제로 전체 데이터를 그대로 반환합니다.
    return data


# ===========================
# POST 요청 처리
# ===========================

# (1) 게시글을 작성하는 API
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    # 클라이언트로부터 전송된 폼 데이터에서 'name'과 'age' 값을 추출합니다.
    name = request.form['name']
    age = request.form['age']

    # 추출한 데이터를 디버깅용으로 출력합니다.
    print(name, age)

    # 게시글 작성 후, 결과를 JSON 형태로 응답합니다.
    return jsonify({'result': 'success'})
    

# ===========================
# 추가 데이터 관련 API
# ===========================

# 초기 데이터: 'items' 리스트를 포함하는 딕셔너리를 리스트에 저장합니다.
datas = [{"items": [{"name": "item1", "price": 10}]}]

# GET 요청을 통해 저장된 데이터를 조회하는 API
@app.get('/api/v1/datas')
def get_datas():
    # 저장된 datas 리스트를 JSON 형태로 반환합니다.
    return {"datas": datas}

# POST 요청을 통해 새로운 데이터를 추가하는 API
@app.post('/api/v1/datas')
def create_data():
    # 클라이언트로부터 전송된 JSON 데이터를 파싱하여 파이썬 딕셔너리로 변환합니다.
    request_data = request.get_json()
    
    # 'items' 키의 값을 추출합니다.
    # 해당 키가 없으면 기본값으로 빈 리스트([])를 사용하여 새 데이터 딕셔너리를 만듭니다.
    new_data = {"items": request_data.get("items", [])}
    
    # 새 데이터를 datas 리스트에 추가하여 저장합니다.
    datas.append(new_data)

    # 새 데이터를 반환하고, HTTP 상태 코드 201 (Created)를 함께 응답합니다.
    return new_data, 201

# ===========================
# 메인 실행부
# ===========================
if __name__ == "__main__":
    # 디버그 모드로 Flask 개발 서버를 실행합니다.
    app.run(debug=True)
