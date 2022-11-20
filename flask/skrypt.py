from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

#Lst of dict for get_stores
stores =[
    {
        'name' : 'My store',
        'items' : [
            {
                'name' : 'Item1',
                'price' : 99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST /store
@app.route('/store', methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)
        else:
            return jsonify({'message' : 'No data'})

#GET store
@app.route('/store')
def get_stores():
    return jsonify({'stores' : stores})

#POST /sotre/<string:name>/item {name:, price}
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if name == store['name']:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message' : 'Store not found'})

#GET /sotre/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store['items'])
        else:
            return jsonify({'message' : 'No data'})

app.run(port=5099)
