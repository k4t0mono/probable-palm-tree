from flask import Blueprint, jsonify, request
from controller import CtrlSona
from models import Sona


app_sona = Blueprint('sona', __name__)


@app_sona.route('/sona', methods=['POST'])
def post_sona():
    """
    @api {post} /sona New sona
    @apiVersion 0.1.0
    @apiName PostSona
    @apiGroup Sona

    @apiDescription Add a new sona

    @apiParam {String} name The unique name of the sona
    @apiParam {String} specie Their specie
    @apiParam {String} owner_id Their owner <code>id</code>

    @apiSuccess {Number} code 200
    @apiSuccess {Object} data The <code>sona</code> object
    """

    try:
        name = request.json['name']
        sona = Sona(name)
        res = CtrlSona().add_sona(sona)
    except Exception as e:
        return jsonify(
            status=400,
            message=str(e)
        )

    return jsonify(
        status=200,
        data=res,
    )


@app_sona.route('/sona', methods=['get'])
def get_sona():
    """
    @api {get} /sona Get all people
    @apiVersion 0.1.0
    @apiName getPeople
    @apiGroup Sona

    @apiDescription Get all people on the database

    @apiSuccess {Number} code 200
    @apiSuccess {Object} data A list of <code>sona</code> objects

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "status": 200,
            "data": [{
                "name": "treta",
                "Sonas": [],
                "idx": 9
            }]
        }
    """

    all_sona = Sona.query.all()
    res = CtrlSona().dump_people(all_sona)

    return jsonify(
        status=200,
        data=res
    )


@app_sona.route('/sona/<idx>', methods=['get'])
def get_sona_id(idx):
    """
    @api {post} /sona/:id Get sona
    @apiVersion 0.1.0
    @apiName GetSona
    @apiGroup Sona

    @apiDescription Get Sona by id

    @apiParam {id} name The unique id of the sona

    @apiSuccess {Number} code 200
    @apiSuccess {Object} data The <code>sona</code> object

    @apiSuccessExample Success-Response:
        HTTP/1.1 200 OK
        {
            "status": 200,
            "data": {
                "name": "treta",
                "Sonas": [],
                "idx": 9
            }
        }
    """

    res = CtrlSona().get_sona(idx)

    if not res:
        return jsonify(
        status=404,
        message='Could not found the sona with id {}'.format(idx),
    )
    
    return jsonify(
        status=200,
        data=res,
    )