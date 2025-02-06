# api/app.py
from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

def load_codes():
    codes_path = os.path.join(os.path.dirname(__file__), '../codes.json')
    with open(codes_path, 'r') as f:
        return json.load(f)


@app.route('/')
def index():
    # html_path = os.path.join(os.path.dirname(__file__), '../index.html')
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
