import unittest
import json
from app import app
from routes import app_main


class TestRoutesMain(unittest.TestCase):

    def setUp(self):
        app.register_blueprint(app_main)
        self.app = app.test_client()

    def test__get_hello__success(self):
        res = self.app.get('/')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(200, res.status_code)
        self.assertEqual(400, data['code'])
        self.assertEqual("I don't think so", data['message'])