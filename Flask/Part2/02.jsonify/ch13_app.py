from flask import Flask,jsonify, request

app = Flask(__name__)

data = {'result':'success', 'data':{'feed1':'data1', 'feed2':'data2'}}

#GET
# (1) 전체 게시글을 불러오는 API
@app.route('/api/v1/feeds', methods=['GET'])
def show_all_feeds():

    return data
    # return jsonify(data) # 딕셔너리 형태가 아니면 jsonify를 해야함

# (2) 특정 게시글을 불러오는 API
@app.route('/api/v1/feeds/<int:feed_id>', methods=['GET'])
def show_one_feed(feed_id):
    print(feed_id)

    return data


# POST
# (1) 게시글을 작성하는 API
@app.route('/api/v1/feeds', methods=['POST'])
def create_one_feed():
    name = request.form['name']  # form data
    age = request.form['age']

    print(name, age)

    return jsonify({'result':'success'})
    
datas = [{"items" : [{"name": "item1", "price":10}]}]

@app.get('/api/v1/datas')
def get_datas():
    return {"datas": datas}

@app.post('/api/v1/datas')
def create_data():
    request_data = request.get_json()
    new_data = {"items" : request_data.get("items", [])}
    datas.append(new_data)

    return new_data, 201

if __name__ == "__main__":
    app.run(debug=True)