from flask import Blueprint, jsonify
from derp import Yiffer


app_yiff = Blueprint('yiff', __name__)
yiffer = Yiffer()


@app_yiff.route('/yiff')
def get_yiff():
    """
    @api {get} /yiff Yiff route
    @apiVersion 0.1.0
    @apiName GetYiff
    @apiGroup Yiff

    @apiDescription The basic yiff me daddy route

    @apiSuccess {Number} code 200
    @apiSuccess {String} message "Yiff me daddy"

    @apiExample Example usage:
        curl -i http://localhost/yiff

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "code": 200, 
            "message": "Yiff me daddy"
        }

    """

    return jsonify(
        code=200,
        message='Yiff me daddy',
    )

@app_yiff.route('/yiff/<name>')
def get_yiff_name(name):
    """
    @api {get} /yiff/:name Yiff someone
    @apiVersion 0.1.0
    @apiName GetYiffName
    @apiGroup Yiff

    @apiDescription Use this route to yiff someone

    @apiParam {String} name The name to be yiffed

    @apiSuccess {Number} code 200
    @apiSuccess {String} message "I like to yiff <code>id</code> UwU"

    @apiExample Example usage:
        curl -i http://localhost/yiff/:name

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "code": 200, 
            "message": "I like to yiff SHeep UwU"
        }

    """

    return jsonify(
        code=200,
        message=yiffer.yiff_me(name)
)