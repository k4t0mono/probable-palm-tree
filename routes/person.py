from flask import Blueprint, jsonify, request
from controller import CtrlPerson
from models import Person


app_person = Blueprint('person', __name__)


@app_person.route('/person', methods=['POST'])
def post_person():
    """
    @api {post} /person New person
    @apiVersion 0.1.0
    @apiName PostPerson
    @apiGroup Person

    @apiDescription Add a new person

    @apiParam {String} name The unique name of the person

    @apiSuccess {Number} code 200
    @apiSuccess {Object} data The <code>person</code> object

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

    try:
        name = request.json['name']
        person = Person(name)
        res = CtrlPerson().add_person(person)
    except Exception as e:
        return jsonify(
            status=400,
            message=str(e)
        )

    return jsonify(
        status=200,
        data=res,
    )


@app_person.route('/person', methods=['get'])
def get_person():
    """
    @api {get} /person Get all people
    @apiVersion 0.1.0
    @apiName getPeople
    @apiGroup Person

    @apiDescription Get all people on the database

    @apiSuccess {Number} code 200
    @apiSuccess {Object} data A list of <code>person</code> objects

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

    all_person = Person.query.all()
    res = CtrlPerson().dump_people(all_person)

    return jsonify(
        status=200,
        data=res
    )


@app_person.route('/person/<idx>', methods=['get'])
def get_person_id(idx):
    """
    @api {post} /person/:id Get person
    @apiVersion 0.1.0
    @apiName GetPerson
    @apiGroup Person

    @apiDescription Get Person by id

    @apiParam {id} name The unique id of the person

    @apiSuccess {Number} code 200
    @apiSuccess {Object} data The <code>person</code> object

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

    res = CtrlPerson().get_person(idx)

    if not res:
        return jsonify(
        status=404,
        message='Could not found the person with id {}'.format(idx),
    )
    
    return jsonify(
        status=200,
        data=res,
    )