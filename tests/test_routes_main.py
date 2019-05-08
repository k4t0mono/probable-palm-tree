import unittest
import json
from app import app


class TestRoutesMain(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test__get_hello__success(self):
        res = self.app.get('/')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(200, res.status_code)
        self.assertEqual(400, data['code'])
        self.assertEqual("I don't think so", data['message'])