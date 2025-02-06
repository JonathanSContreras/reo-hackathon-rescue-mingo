# api/app.py
from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Load codes from JSON file
def load_codes():
    with open('codes.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    # return "Welcome to the Code Crisis Hackathon!"
    return render_template('index.html')

@app.route('/check_code', methods=['POST'])
def check_code():
    user_code = request.form['code']
    codes = load_codes()
    
    if user_code in codes:
        return jsonify({'success': True, 'token': codes[user_code]})
    else:
        return jsonify({'success': False, 'message': 'Invalid code!'})

if __name__ == '__main__':
    app.run(debug=True)
