from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 800,
        "quantity": 4
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 20,
        "quantity": 10
    },
    {
        "id": 3,
        "name": "Keyboard",
        "price": 40,
        "quantity": 6
    },
    {
        "id": 4,
        "name": "Monitor",
        "price": 200,
        "quantity": 3
    },
    {
        "id": 5,
        "name": "Printer",
        "price": 120,
        "quantity": 5
    },
    {
        "id": 6,
        "name": "Tablet",
        "price": 300,
        "quantity": 7
    },
    {
        "id": 7,
        "name": "Phone",
        "price": 500,
        "quantity": 2
    },
    {
        "id": 8,
        "name": "Headphones",
        "price": 50,
        "quantity": 8
    },
    {
        "id": 9,
        "name": "Speakers",
        "price": 100,
        "quantity": 4
    },
    {
        "id": 10,
        "name": "Microphone",
        "price": 70,
        "quantity": 6
    }
]

@app.route('/api/v1/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(port=8001, debug=True)
