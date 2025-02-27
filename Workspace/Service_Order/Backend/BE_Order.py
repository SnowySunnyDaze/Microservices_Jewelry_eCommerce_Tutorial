from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

orders = [
    {
        "id": 1,
        "product_id": 1,
        "quantity": 1,
        "customer_name": "Alice",
        "customer_address": "123 Main St"
    },
    {
        "id": 2,
        "product_id": 2,
        "quantity": 2,
        "customer_name": "Bob",
        "customer_address": "456 Elm St"
    },
    {
        "id": 3,
        "product_id": 3,
        "quantity": 3,
        "customer_name": "Charlie",
        "customer_address": "789 Oak St"
    },
    {
        "id": 4,
        "product_id": 4,
        "quantity": 4,
        "customer_name": "David",
        "customer_address": "1011 Pine St"
    },
    {
        "id": 5,
        "product_id": 5,
        "quantity": 5,
        "customer_name": "Eve",
        "customer_address": "1213 Cedar St"
    },
    {
        "id": 6,
        "product_id": 6,
        "quantity": 6,
        "customer_name": "Frank",
        "customer_address": "1415 Birch St"
    },
    {
        "id": 7,
        "product_id": 7,
        "quantity": 7,
        "customer_name": "Grace",
        "customer_address": "1617 Maple St"
    },
    {
        "id": 8,
        "product_id": 8,
        "quantity": 8,
        "customer_name": "Heidi",
        "customer_address": "1819 Walnut St"
    },
    {
        "id": 9,
        "product_id": 9,
        "quantity": 9,
        "customer_name": "Ivan",
        "customer_address": "2021 Chestnut St"
    }
]

@app.route("/api/v1/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)

if __name__ == "__main__":
    app.run(port=9001, debug=True)