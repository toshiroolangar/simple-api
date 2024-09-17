"""Simple API developed in Flask"""
from flask import Flask, jsonify

app = Flask(__name__)
products = [
    {'id': 69, 'Name': 'Gago', 'Price': 2500},
    {'id': 70, 'Name': 'TY', 'Price': 500}
]
"""Root path"""
@app.route('/')
def welcome():
    """Return root path"""
    return 'Welcome to the jungle!'
"""Products path"""
@app.route('/products', methods=['GET'])
def get_products():
    """Return products"""
    return jsonify(products)

if __name__ == ('__main__'):
    app.run(host='0.0.0.0', port=5000)
