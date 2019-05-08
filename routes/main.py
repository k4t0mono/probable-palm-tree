from flask import Blueprint, jsonify


app_main = Blueprint('main', __name__)


@app_main.route('/')
def get_hello():
    return jsonify(
        code=400,
        message='I don\'t think so'
    )