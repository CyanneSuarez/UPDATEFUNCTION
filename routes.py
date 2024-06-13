# service/routes.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# Example data
items = {
    1: {"name": "Item 1", "availability": "In Stock"},
    2: {"name": "Item 2", "availability": "Out of Stock"},
}

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id in items:
        item = items[item_id]
        data = request.get_json()
        item.update(data)
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
