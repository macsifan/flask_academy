from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


dicts=[['user_type_id', 'user_type'],
 ['0', 'undefined_unverified'],
 ['1', 'owner'],
 ['2', 'specialist'],
 ['3', 'company'],
 ['4', 'residential_complex'],
 ['5', 'builder']]

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Hello, World!'})

@app.route('/dict', methods=['GET'])
def returnAll():
    return jsonify({'dicts' : dicts})



if __name__ == "__main__":
    app.run(host = '0.0.0.0', port ='5000')