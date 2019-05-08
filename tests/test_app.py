import unittest
import json
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test__get_hello__success(self):
        res = self.app.get('/')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(200, res.status_code)
        self.assertEqual(400, data['code'])
        self.assertEqual("I don't think so", data['message'])
    
    def test__get_yiff_name__name(self):
        res = self.app.get('/yiff/democelot')
        data = json.loads(res.data.decode('utf-8'))

        self.assertEqual(200, res.status_code)
        self.assertEqual(200, data['code'])
        self.assertEqual('I like to yiff democelot UwU', data['message'])