"""Simple API developed in Flask"""
from flask import Flask, jsonify

app = Flask(__name__)
products = [
    {'id': 69, 'Name': 'Gago', 'Price': 2500},
    {'id': 70, 'Name': 'TY', 'Price': 500}
]


@app.route('/')
def welcome():
    """Return welcome message in root path"""
    return 'Welcome to the jungle!'


@app.route('/products', methods=['GET'])
def get_products():
    """Return json response with the product list"""
    return jsonify(products)


if __name__ == ('__main__'):
    app.run(host='0.0.0.0', port=5000)
