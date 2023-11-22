from flask import jsonify
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'x' in data and 'y' in data:
        result = data['x'] + data['y']
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Missing x or y parameter'}), 400

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    if 'x' in data and 'y' in data:
        result = data['x'] - data['y']
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Missing x or y parameter'}), 400

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    if 'x' in data and 'y' in data:
        result = data['x'] * data['y']
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Missing x or y parameter'}), 400

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    if 'x' in data and 'y' in data:
        if data['y'] != 0:
            result = data['x'] / data['y']
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'Division by zero is not allowed'}), 400
    else:
        return jsonify({'error': 'Missing x or y parameter'}), 400

if __name__ == '_main_':
    app.run(debug=True)