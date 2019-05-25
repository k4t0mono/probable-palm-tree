from flask import Blueprint, jsonify


app_main = Blueprint('main', __name__)


@app_main.route('/')
def get_hello():
    """
    @api {get} / Home route
    @apiVersion 0.1.0
    @apiName GetHome
    @apiGroup General

    @apiDescription The route to the main page

    @apiExample Example usage:
        curl -i http://localhost/

    @apiSuccess {Number} code 400
    @apiSuccess {String} message "I don't think so"

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "code": 400, 
            "message": "I don't think so"
        }

    """

    return jsonify(
        code=400,
        message='I don\'t think so'
    )