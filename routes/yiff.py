from flask import Blueprint, jsonify
from derp import Yiffer


app_yiff = Blueprint('yiff', __name__)
yiffer = Yiffer()


@app_yiff.route('/yiff')
def get_yiff():
    return jsonify(
        code=200,
        message='Yiff me daddy',
    )

@app_yiff.route('/yiff/<name>')
def get_yiff_name(name):
    return jsonify(
        code=200,
        message=yiffer.yiff_me(name)
)