from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
url = "https://script.google.com/macros/s/AKfycby76jWCa-RJC8dPYtV6Rz8w_IRTHEC-lryvf8JIthu3iCiCrwpLFUTcZP5zGsV4v2AzOQ/exec"

@app.route('/')
def home():
    return "hello alignsy!"

@app.route('/join-waitlist', methods=['POST'])
def join_waitlist():
    requests.post(url, json={
        'email': request.json.get("email")
    })
    return jsonify(data="success"), 200


if __name__ == '__main__':
    app.run()
