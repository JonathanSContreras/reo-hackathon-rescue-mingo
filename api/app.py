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

    # return "Welcome to the Code Crisis Hackathon!"
    return render_template('closed.html')

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

# from flask import Flask, request, jsonify, render_template, redirect, url_for
# import json
# import os
# from datetime import datetime
# import pytz  # Required for timezone handling

# app = Flask(__name__)

# # Set your closing time here (update the date and timezone accordingly)
# CLOSING_TIME = datetime(2025, 2, 8, 23, 59, 59)  # Year, Month, Day, Hour, Minute, Second
# TIMEZONE = pytz.timezone('America/Chicago')  # Change to your desired timezone
# CLOSING_TIME = TIMEZONE.localize(CLOSING_TIME)

# def load_codes():
#     codes_path = os.path.join(os.path.dirname(__file__), '../codes.json')
#     with open(codes_path, 'r') as f:
#         return json.load(f)

# @app.before_request
# def check_closing_time():
#     # Allow access to the closed page even after closing time
#     if request.endpoint == 'closed':
#         return
    
#     current_time = datetime.now(TIMEZONE)
#     if current_time >= CLOSING_TIME:
#         return redirect(url_for('closed'))

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/closed')
# def closed():
#     return render_template('closed.html')

# @app.route('/check_code', methods=['POST'])
# def check_code():
#     user_code = request.form['code']
#     codes = load_codes()
    
#     if user_code in codes:
#         return jsonify({'success': True, 'token': codes[user_code]})
#     else:
#         return jsonify({'success': False, 'message': 'Invalid code!'})

# if __name__ == '__main__':
#     app.run(debug=True)