import os
from flask import Flask, jsonify, abort, request
from derp import Yiffer


app = Flask(__name__)
yiffer = Yiffer()


@app.route('/')
def get_hello():
    return jsonify(
        code=400,
        message='I don\'t think so'
    )

@app.route('/yiff/<name>')
def get_yiff_name(name):
    return jsonify(
        code=200,
        message=yiffer.yiff_me(name)
    )


if __name__ == '__main__':
    port = os.getenv('PORT', 58913)
    app.run(host='0.0.0.0', port=port, debug=True)