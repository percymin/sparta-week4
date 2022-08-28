from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import certifi

ca = certifi.where();

client = MongoClient('mongodb+srv://sammymin:sammy0404@cluster0.gvkfzz2.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

app = Flask(__name__)


@app.route('/')
def home():


    return render_template('index.html')


@app.route("/mars", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']

    doc = {'name': name_receive,
           'address': address_receive,
           'size': size_receive
           }
    db.mars2.insert_one(doc)

    return jsonify({'msg': 'POST 연결 완료!'})


@app.route("/mars", methods=["GET"])
def web_mars_get():
    order_list = list(db.mars2.find({}, {'_id': False}))

    return jsonify({'orders': order_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
