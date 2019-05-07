import os
from flask import Flask, jsonify, abort, request
from derp import Yiffer


app = Flask(__name__)


@app.route('/api/hello')
def get_hello():
    return jsonify(
        code=200,
        message='I don\'t think so'
    )

@app.route('/api/hello/<name>')
def get_hello_name(name):
    return jsonify(
        code=200,
        message=yiffer.yiff_me(name)
    )


if __name__ == '__main__':
    port = os.getenv('PORT', 58913)
    yiffer = Yiffer()
    app.run(host='0.0.0.0', port=port, debug=True)