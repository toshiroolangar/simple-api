from flask import Flask, jsonify, request
import json

app = Flask(__name__)
products = [
    {'id': 69, 'Name': 'Gago', 'Price': 2500},
    {'id': 70, 'Name': 'TY', 'Price': 500}
]

@app.route('/')
def welcome():
    return 'Welcome to the jungle!'
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == ('__main__'):
    app.run(host='0.0.0.0', port=5000)