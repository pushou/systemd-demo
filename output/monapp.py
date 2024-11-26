from flask import Flask,jsonify
import os

app = Flask(__name__)
version = os.environ.get("VERSION_MONAPP")

@app.route('/')
def hello_world():
    return jsonify("Le Python c'est bon mangez en")

@app.route('/version')
def hello_color():
    return jsonify(version)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
