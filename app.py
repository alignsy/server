from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
url = "https://script.google.com/macros/s/AKfycbwfirVKiSEFtnn6Ac7KCf17b4P_Na5N3joeCnm2GpuhDSSpC4o56RZxj-vV8DDHBrB2cA/exec"

@app.route('/')
def home():
    return "hello alignsy!"

@app.route('/join-waitlist', methods=['POST'])
def join_waitlist():
    try:
        res = requests.post(url, json={
            'email': request.json.get("email")
        })
        if res.content==b'email already present':
            return jsonify(data="already present"),200
        return jsonify(data="success"), 200
    except Exception as e:
        return jsonify(data="error"), 400


if __name__ == '__main__':
    app.run()
