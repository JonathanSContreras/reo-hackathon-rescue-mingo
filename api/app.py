# app.py
from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Load codes from JSON file
def load_codes():
    if not os.path.exists('codes.json'):
        raise FileNotFoundError("codes.json file not found.")
    with open('codes.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_code', methods=['POST'])
def check_code():
    try:
        user_code = request.form['code']
        codes = load_codes()
        
        if user_code in codes:
            return jsonify({'success': True, 'token': codes[user_code]})
        else:
            return jsonify({'success': False, 'message': 'Invalid code!'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
