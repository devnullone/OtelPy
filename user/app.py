import requests
from flask import Flask, jsonify

app = Flask(__name__)

print('Loading USER app.py')

@app.route('/user/profile')
def get_user_profile():
    user = {
        'userid': '1',
        'name': 'John Doe',
        'email': 'john.doe@example.com'
        }
    return jsonify(user)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)