from flask import Flask, jsonify, request
from flask_cors import CORS
import db
import json
app = Flask(__name__)

CORS(app) 


with open('config.json', 'r') as file:
    config = json.load(file)

db_table = config['postgres'].get("db_table")

@app.route('/')
def home():
    return "Welcome to home boi!"

@app.route('/read', methods=['GET'])
def read():
    query = f"SELECT * FROM {db_table};"
    try:
        result = db.read_from_db(query)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/write', methods=['POST'])
def write():
    data = request.json
    query = f"INSERT INTO {db_table} (name, job_profile, phone) VALUES (%s, %s, %s);"
    params = (data['name'], data['job_profile'], data['phone'])
    try:
        db.write_to_db(query, params)
        return jsonify({'message':'data inserted'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)