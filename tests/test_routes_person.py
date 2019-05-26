import unittest
import json
from app import app, db
from routes import app_person
from models import Person
from schemas import PersonSchema


class TestRoutesPerson(unittest.TestCase):

    def setUp(self):
        app.register_blueprint(app_person)
        self.app = app.test_client()
        db.create_all()
        self.person_schema = PersonSchema(strict=True)
        self.people_schema = PersonSchema(strict=True, many=True)
        self.people = [
            Person(name='KME', idx=1),
            Person(name='SLion', idx=2),
            Person(name='Demon', idx=3),
        ]

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def dump_person(self, person):
        return self.person_schema.dump(person).data
    
    def dump_people(self, people):
        return self.people_schema.dump(people).data
    
    def post_person(self, person):
        res = self.app.post(
            '/person',
            data=json.dumps(self.dump_person(person)),
            content_type='application/json'
        )
        return json.loads(res.data.decode('utf-8'))


    def test__post_person__success(self):
        p = self.people[0]
        data = self.post_person(p)

        self.assertEqual(200, data['status'])
        self.assertEqual(self.dump_person(p), data['data'])

    def test__get_person_idx__success(self):
        p = self.people[0]
        self.post_person(p)

        res = self.app.get('/person/1')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(200, data['status'])
        self.assertEqual(self.dump_person(p), data['data'])
    
    def test__get_person__success(self):
        for p in self.people:
            self.post_person(p)
        
        res = self.app.get('/person')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(200, data['status'])
        self.assertEqual(self.dump_people(self.people), data['data'])